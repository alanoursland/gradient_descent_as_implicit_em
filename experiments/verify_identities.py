"""Numerical verification of every identity claimed in the paper and notes.

Each check compares an analytic gradient claim against central finite differences.
Run:  python3 experiments/verify_identities.py

Checks
------
1. Loss-level LSE:            dL/dd_j = -r_j                       (Theorem 1)
2. Cross-entropy (clamped):   dL/dd_j = r_j - 1[j=y]
3. Internal softmax, values:  dL/dv_j = alpha_j * g                (exact M-step)
4. Internal softmax, scores:  dL/ds_j = alpha_j * (a_j - a_bar)    (advantage law)
5. Forward-pass LSE (Hopfield): grad_q lse(q.K^T) = sum_j alpha_j k_j
6. EM step = preconditioned gradient step on GMM means (Xu & Jordan 1996):
   mu_new - mu = (Sigma / N_j) * dL/dmu_j   with N_j = sum_i r_ij
"""

import numpy as np

rng = np.random.default_rng(0)
EPS = 1e-6
TOL = 1e-7


def num_grad(f, x):
    """Central finite-difference gradient of scalar f at x (flattened)."""
    x = x.astype(float)
    g = np.zeros_like(x)
    it = np.nditer(x, flags=["multi_index"])
    while not it.finished:
        i = it.multi_index
        xp, xm = x.copy(), x.copy()
        xp[i] += EPS
        xm[i] -= EPS
        g[i] = (f(xp) - f(xm)) / (2 * EPS)
        it.iternext()
    return g


def softmax(s):
    e = np.exp(s - s.max())
    return e / e.sum()


def report(name, analytic, numeric):
    err = np.max(np.abs(analytic - numeric))
    status = "PASS" if err < 1e-5 else "FAIL"
    print(f"  [{status}] {name}: max abs err = {err:.3e}")
    assert err < 1e-5, name


# ----------------------------------------------------------------------------
print("1. Loss-level LSE: dL/dd_j = -r_j")
K = 7
d = rng.normal(size=K)
r = softmax(-d)
L = lambda dd: np.log(np.sum(np.exp(-dd)))
report("Theorem 1", -r, num_grad(L, d))

# ----------------------------------------------------------------------------
print("2. Cross-entropy in distance form: dL/dd_j = 1[j=y] - r_j")
# NOTE: the 2025-12 draft stated r_j - 1[j=y]; converting the standard logit
# gradient dL/dz_j = p_j - 1[j=y] to distances d = -z negates it. This check
# caught that sign error; the correct distance-form identity is 1[j=y] - r_j.
y = 3
onehot = np.eye(K)[y]
L = lambda dd: dd[y] + np.log(np.sum(np.exp(-dd)))
report("clamped identity", onehot - r, num_grad(L, d))

# ----------------------------------------------------------------------------
print("3. Internal softmax, value gradients: dL/dv_j = alpha_j * g")
K, m = 5, 4
s = rng.normal(size=K)
V = rng.normal(size=(K, m))
w = rng.normal(size=m)          # arbitrary downstream loss L = w . tanh(o)
alpha = softmax(s)


def downstream(o):
    return float(w @ np.tanh(o))


def loss_of_V(Vf):
    return downstream(softmax(s) @ Vf.reshape(K, m))


o = alpha @ V
g = w * (1 - np.tanh(o) ** 2)   # dL/do
analytic_V = np.outer(alpha, g)
report("dL/dv_j = alpha_j g", analytic_V, num_grad(loss_of_V, V.flatten()).reshape(K, m))

# ----------------------------------------------------------------------------
print("4. Internal softmax, score gradients: dL/ds_j = alpha_j (a_j - a_bar)")
a = V @ g
abar = alpha @ a
analytic_s = alpha * (a - abar)


def loss_of_s(sf):
    return downstream(softmax(sf) @ V)


report("advantage law", analytic_s, num_grad(loss_of_s, s))
print(f"       zero-sum check: sum_j dL/ds_j = {analytic_s.sum():+.3e}")

# ----------------------------------------------------------------------------
print("5. Forward-pass LSE (Hopfield): grad_q lse(K q) = sum_j alpha_j k_j")
n, dk = 6, 3
Kmat = rng.normal(size=(n, dk))
q = rng.normal(size=dk)
alpha_q = softmax(Kmat @ q)
lse = lambda qq: np.log(np.sum(np.exp(Kmat @ qq)))
report("forward-pass identity", Kmat.T @ alpha_q, num_grad(lse, q))

# ----------------------------------------------------------------------------
print("6. Xu-Jordan: EM mean update = (Sigma/N_j) * gradient of log-likelihood")
# Spherical GMM, fixed covariance sigma2*I and uniform weights; means free.
Kc, dim, N = 3, 2, 40
X = rng.normal(size=(N, dim)) * 2.0
mu = rng.normal(size=(Kc, dim))
sigma2 = 0.7


def loglik(mu_flat):
    m_ = mu_flat.reshape(Kc, dim)
    d2 = ((X[:, None, :] - m_[None, :, :]) ** 2).sum(-1)  # (N, Kc)
    # log sum_j exp(-d2/(2 sigma2)) + const, summed over data
    z = -d2 / (2 * sigma2)
    return float(np.log(np.exp(z - z.max(1, keepdims=True)).sum(1)).sum()
                 + z.max(1).sum())


d2 = ((X[:, None, :] - mu[None, :, :]) ** 2).sum(-1)
z = -d2 / (2 * sigma2)
resp = np.exp(z - z.max(1, keepdims=True))
resp /= resp.sum(1, keepdims=True)                        # (N, Kc)
Nj = resp.sum(0)                                          # (Kc,)
mu_em = (resp.T @ X) / Nj[:, None]                        # EM M-step means

grad = num_grad(loglik, mu.flatten()).reshape(Kc, dim)    # dL/dmu_j
precond_step = (sigma2 / Nj)[:, None] * grad              # P_j = sigma2 I / N_j
report("EM step = P * grad", mu_em - mu, precond_step)

print("\nAll identities verified.")
