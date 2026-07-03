# The Internal-Softmax Gradient: Where the LSE Sits Changes the Identity

## Purpose of This Document

This note derives the exact gradient structure for a softmax that sits **inside the
network** (as in attention) rather than **in the loss** (as in mixture likelihood or
cross-entropy), and states precisely how Theorem 1 does and does not transfer.

This resolves the main mathematical overreach in the current draft. Theorem 1
(\( \partial L / \partial d_j = -r_j \)) holds when the log-sum-exp **is the objective**.
In a transformer, the attention softmax is in the **forward pass**; the loss is
cross-entropy at the output. The gradient of the loss with respect to an attention score is
therefore *not* \( -\alpha_j \), and the paper must not imply that it is. The exact result
is different, still clean, and arguably more interesting.

---

## Setup

An internal softmax module:

- scores \( s_j \) (equivalently distances \( d_j = -s_j 
\)), \( j = 1, \dots, K \)
- weights \( \alpha_j = \dfrac{\exp(s_j)}{\sum_k \exp(s_k)} \) (responsibilities)
- values \( v_j \in \mathbb{R}^m \)
- module output \( o = \sum_j \alpha_j v_j \) — the responsibility-weighted mean,
  \( o = \mathbb{E}_\alpha[v] \)
- a downstream loss \( L \) that depends on the module only through \( o \).

Let \( g \equiv \partial L / \partial o \in \mathbb{R}^m \) be the backpropagated error, and
define the **alignment** (downstream usefulness) of each value:

\[
a_j \equiv g^\top v_j,
\qquad
\bar{a} \equiv \sum_k \alpha_k a_k = \mathbb{E}_\alpha[a].
\]

---

## Result 1: Value Gradients Are Exactly Responsibility-Weighted

\[
\frac{\partial L}{\partial v_j} = \alpha_j \, g
\]

Immediate from \( o = \sum_j \alpha_j v_j \). No approximation. Each value receives the
downstream error **scaled exactly by its responsibility**. This is the M-step statement for
internal softmaxes, and it is an identity of the same strength as Theorem 1. This is the
rigorous content behind "values are prototypes updated by responsibility": it holds
verbatim, per gradient step, for any loss.

## Result 2: Score Gradients Are Responsibility-Gated and Mean-Centered

Using the softmax Jacobian \( \partial \alpha_k / \partial s_j = \alpha_j(\delta_{jk} - \alpha_k) \):

\[
\frac{\partial L}{\partial s_j}
= \sum_k (g^\top v_k) \frac{\partial \alpha_k}{\partial s_j}
= \alpha_j \left( a_j - \bar{a} \right)
\]

Equivalently, in distance form:

\[
\frac{\partial L}{\partial d_j} = -\,\alpha_j \left( a_j - \bar{a} \right)
\]

This is a **covariance identity**: for a Boltzmann distribution
\( \alpha = \mathrm{softmax}(s) \), the gradient of the expectation
\( \mathbb{E}_\alpha[a] \) with respect to \( s_j \) is
\( \mathrm{Cov}_\alpha(a, \mathbb{1}_j) = \alpha_j(a_j - \bar{a}) \). Agarwal et al. (2025b)
derive exactly this form for transformer attention and call it the *advantage-based routing
law*; it holds for **any** internal softmax, not just attention.

---

## Interpretation: Three Ways the Identity Appears

The slogan "responsibilities are gradients" is correct, but the precise statement depends on
**where the LSE sits**:

| Location of LSE | Gradient identity | E/M reading |
|---|---|---|
| **In the loss** (mixture likelihood) | \( \partial L / \partial d_j = -r_j \) — gradient *is* the responsibility | E-step and M-step fused; proximity drives assignment |
| **In the loss, clamped** (cross-entropy) | \( \partial L / \partial d_j = r_j - \mathbb{1}[j=y] \) | E-step overridden by the label |
| **Inside the network** (attention) | \( \partial L / \partial v_j = \alpha_j g \) (exact M-step); \( \partial L / \partial s_j = \alpha_j (a_j - \bar{a}) \) (advantage-gated E-step) | responsibilities gate *all* learning, but the E-step's target is downstream usefulness, not likelihood |

Consequences of the internal form:

1. **Responsibilities still gate everything.** Both gradients carry the factor
   \( \alpha_j \): a component with no responsibility learns nothing and routes nothing.
   The gating claim of the paper survives fully.
2. **The competition is over usefulness, not proximity.** The centered factor
   \( a_j - \bar{a} \) means a score rises only if its value is *more useful to the
   downstream error than the current attention-weighted average*. In the loss-level case,
   competition is for likelihood; in the internal case, competition is for advantage.
3. **Zero-sum structure.** \( \sum_j \partial L / \partial s_j = 0 \) — internal softmax
   gradients redistribute; they cannot uniformly raise or lower all scores. (In the
   loss-level case the gradients sum to \(-1\): total responsibility is conserved instead.)
4. **Two-timescale dynamics fall out.** Once \( \alpha \) concentrates
   (\( \alpha_{j^*} \approx 1 \)), the advantage \( a_{j^*} - \bar{a} \to 0 \), so score
   updates vanish while value updates (\( \alpha_{j^*} g \)) persist. Attention stabilizes
   early; values keep refining. This is exactly the empirical observation of Agarwal et al.
   (2025b), and here it is a one-line consequence of the gradient forms.

---

## The Forward-Pass Identity (Hopfield Connection)

There is a second, exact sense in which attention computes a gradient of an LSE — in the
**forward pass** rather than the backward pass. For query \( q \) and keys \( \{k_j\} \):

\[
\nabla_q \, \log \sum_j \exp(q^\top k_j) = \sum_j \alpha_j k_j
\]

The attention read-out (over keys) is the gradient of an LSE energy with respect to the
query. Ramsauer et al. (2020) develop this view: transformer attention is the retrieval
dynamics of a modern Hopfield network whose energy contains \( -\mathrm{lse}(\beta, X^\top \xi) \).

Together with Results 1–2 this gives a symmetric statement the paper can own:

> **The forward pass takes an LSE gradient with respect to the *state* (inference: the
> E-step as an energy-descent read-out). The backward pass takes responsibility-gated
> gradients with respect to the *parameters* (learning: the M-step). Both passes are
> gradients of log-sum-exp structures; responsibilities appear in both, in different roles.**

---

## What This Changes in the Paper

1. **Section 4.2 (attention regime)** must not lean on Theorem 1 directly. It should state
   Results 1–2, note that Result 1 is the exact analogue of Theorem 1 for internal
   softmaxes, cite Agarwal et al. (2025b) for the attention-specific derivation, and derive
   the two-timescale observation as a consequence.
2. **The "prototype is \( W_V \)" discussion** stays, but is now grounded: by the chain
   rule, \( \partial L / \partial W_V = \sum_j (\alpha_j g) x_j^\top \) (per query) — the
   projection accumulates exactly responsibility-weighted outer products. The function-space
   M-step becomes a derived equation instead of a verbal patch.
3. **The taxonomy gains a dimension.** Regimes differ not only in what is observed
   (latent / conditional / clamped) but in **where the LSE sits** (loss vs. network
   interior). This is a sharper organizing axis and it is honest about the difference.

---

## Verification

All identities in this note are verified numerically against finite differences in
`experiments/verify_identities.py` (Checks 3–5).

---

## Summary

- In the loss: gradient **equals** negative responsibility (Theorem 1; Fisher's identity).
- Inside the network: value gradients are **exactly** responsibility-weighted; score
  gradients are responsibility-gated **advantages**, with zero-sum competition and
  automatic two-timescale dynamics.
- In the forward pass: the attention output **is** an LSE gradient with respect to the query
  (Hopfield view).

The unifying claim survives in a stronger, honest form: **every appearance of log-sum-exp —
in the loss, in the interior, in the forward pass — turns differentiation into
responsibility computation. What varies is which quantity the responsibilities weight.**
