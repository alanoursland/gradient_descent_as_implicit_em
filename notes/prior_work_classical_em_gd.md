# Prior Work: The Classical EM–Gradient-Descent Bridge

## Purpose of This Document

This note documents the **classical statistics and machine learning literature that already
connects gradient methods to EM**, assesses precisely how much of the paper's central claim
is anticipated by it, and states what daylight remains for the present contribution.

This is the most important risk-management document in the project. The paper's prior-work
section previously stated that the gradient/responsibility connection was *"not, to our
knowledge, previously stated as a formal identity."* **That statement was false and has been
removed in the 2026-07 revision.** The connection is classical, has a name (Fisher's
identity), and has been extended and refined repeatedly. A knowledgeable reviewer would have
cited the results below within minutes.

The correct response is not better rhetoric but repositioning: cite the classical line
prominently, and claim what is actually new — the framing, the regime taxonomy, and the
application to standard neural objectives.

---

## I. The Core Identity Is Classical

### Fisher's Identity

For any latent-variable model \( p(x, z; \theta) \):

\[
\nabla_\theta \log p(x; \theta)
= \mathbb{E}_{z \sim p(z \mid x; \theta)} \left[ \nabla_\theta \log p(x, z; \theta) \right]
\]

The gradient of the incomplete-data (marginal) log-likelihood **is** the posterior-expected
complete-data gradient. For a mixture model, the posterior over \( z \) is exactly the vector
of responsibilities, so the marginal-likelihood gradient is exactly the
responsibility-weighted complete-data gradient.

This is the general form of "responsibilities are gradients." It is standard in the EM
literature (see e.g. Cappé & Moulines, 2009, *Online EM for latent data models*, JRSS-B,
where it is used by name), and it predates the deep learning era entirely.

**Consequence for the paper:** Theorem 1 (\( \partial L / \partial d_j = -r_j \)) is the
special case of Fisher's identity for a uniform-prior mixture with component likelihoods
\( \exp(-d_j) \), differentiated with respect to the distances themselves. The derivation is
correct, but it cannot be presented as a new identity.

### The Textbook Mixture Gradient

Bishop (*Pattern Recognition and Machine Learning*, 2006, §9.2) derives, en route to EM,
that the gradient of the Gaussian-mixture log-likelihood with respect to a component mean is

\[
\frac{\partial \mathcal{L}}{\partial \mu_k} = \sum_n r_{nk} \, \Sigma_k^{-1} (x_n - \mu_k)
\]

— a responsibility-weighted sum. The observation that mixture-likelihood gradients are gated
by responsibilities is textbook material.

---

## II. Gradient Descent vs. EM: The Relationship Is Precisely Characterized

### Xu & Jordan (1996)

*On Convergence Properties of the EM Algorithm for Gaussian Mixtures*, Neural Computation
8(1):129–151.

Xu & Jordan prove that the EM update for Gaussian mixtures is a **preconditioned gradient
step** on the log-likelihood:

\[
\theta^{(t+1)} - \theta^{(t)} = P(\theta^{(t)}) \, \nabla_\theta \mathcal{L}
\]

with an explicit positive-definite projection matrix \( P \). For the means (fixed
covariances and weights), \( P_j = \Sigma_j / \sum_i r_{ij} \), so the EM step and the
gradient step point in related but **not identical** directions — they differ by a
responsibility-dependent, positive-definite rescaling.

**Consequence for the paper:** the claim "gradient descent on LSE objectives **is exactly**
EM" is stronger than what is true, and weaker results are already published with more
precision. The defensible statement is: *the instantaneous gradient is the
responsibility-weighted update direction (Fisher's identity); the EM step is that same
gradient under a specific positive-definite preconditioner (Xu & Jordan).* Gradient descent
and EM share update structure, not trajectories — which the paper's own Zhang et al. (2020)
citation already concedes at the level of convergence behavior.

### Neal & Hinton (1998)

*A View of the EM Algorithm that Justifies Incremental, Sparse, and Other Variants*, in
Jordan (ed.), Learning in Graphical Models.

Neal & Hinton show that E and M steps are **coordinate ascent on a single free-energy
objective** \( F(q, \theta) \). The "discrete, alternating" character of EM is an algorithmic
choice, not a structural fact; partial, incremental, and continuous variants all ascend the
same objective.

**Consequence for the paper:** the framing "classical EM is discrete and alternating; we
show the separation is not fundamental" (sec-geometric-substrate §2.3, sec-main-result §3.2)
re-derives the conceptual content of Neal & Hinton. The paper must cite them and inherit
their language rather than appear to discover the point.

### Salakhutdinov, Roweis & Ghahramani (2003)

*Optimization with EM and Expectation-Conjugate-Gradient*, ICML 2003.

Uses precisely the expected-gradient identity to build direct gradient optimizers for
latent-variable models, and characterizes when EM behaves like a quasi-Newton method (small
missing information) versus when it converges slowly. The gradient/EM relationship is here
an engineering tool, fifteen years before the transformer.

---

## III. Neural Instances That Already Make the EM/Attention Connection

- **Ramsauer et al. (2020), *Hopfield Networks is All You Need*.** The modern Hopfield
  energy is \( E(\xi) = -\mathrm{lse}(\beta, X^\top \xi) + \tfrac{1}{2}\xi^\top\xi + \text{const} \),
  and the transformer attention update is the retrieval dynamics on this energy. In
  particular \( \nabla_\xi \, \mathrm{lse}(\beta, X^\top \xi) = X \,\mathrm{softmax}(\beta X^\top \xi) \):
  **the attention output is the gradient of an LSE energy with respect to the query.**
  "Responsibilities are gradients" therefore already has a published instantiation *inside
  the forward pass* of attention.
- **Greff, van Steenkiste & Schmidhuber (2017), *Neural Expectation Maximization*, NeurIPS.**
  Unrolls EM on a spatial mixture whose components are parameterized by neural networks;
  differentiable clustering as explicit EM-in-a-network.
- **Li et al. (2019), *Expectation-Maximization Attention Networks*, ICCV (oral).** Builds an
  attention module that literally iterates E and M steps, explicitly framing attention maps
  as E-step responsibilities.
- **Hinton, Sabour & Frosst (2018), *Matrix Capsules with EM Routing*, ICLR.** Routing by
  explicit EM between capsule layers.
- **Jacobs et al. (1991) / Jordan & Jacobs (1994), Mixtures of Experts.** Gating as
  responsibilities, trained both by gradient methods and by EM; the equivalence of the two
  trainings was studied at the time.

The pattern: the field has repeatedly *built* EM into attention-like modules and *observed*
that softmax modules behave like E-steps. What is rarer is the objective-level statement that
standard training already contains the structure without modification — that is the space
the present paper occupies, and it must be claimed precisely.

---

## IV. What Daylight Remains

After the classical results are cited honestly, the paper retains the following genuine
contributions:

1. **The substrate connection.** Fisher's identity is about generative latent-variable
   models. The paper's claim is that *standard discriminative training on standard
   architectures* instantiates the same structure, because (a) neural outputs admit a
   distance/energy reading (Oursland 2024) and (b) softmax cross-entropy and attention have
   LSE form. Nobody in the classical line claims that a ReLU classifier trained with
   cross-entropy is running mixture-model inference. This is a framing contribution, and it
   should be presented as one.

2. **The three-regime taxonomy.** Latent (unsupervised LSE), conditional (attention),
   clamped (cross-entropy) as one mechanism under different observation patterns. This
   organization of GMMs, attention, and classification under a single gradient structure is
   not in the classical literature.

3. **The normalization boundary.** The taxonomy of objectives by
   exponentiation/normalization — with the correntropy contrast showing that exponentiation
   without competition buys robustness and forfeits assignment — is a clean, teachable
   design-space result.

4. **The location-of-the-LSE distinction (new; see `internal_softmax_gradient.md`).** Where
   the LSE sits changes the identity: in the loss, \( \partial L / \partial d_j = -r_j \)
   exactly; inside the network, value gradients are exactly responsibility-weighted
   (\( \partial L / \partial v_j = \alpha_j g \)) while score gradients are
   responsibility-gated and mean-centered (\( \partial L / \partial s_j = \alpha_j (a_j - \bar{a}) \)).
   Agarwal et al. (2025b) derive this for transformer attention; the paper can state it as
   the general rule for any internal softmax and use it to place attention honestly within
   the framework.

5. **The synthesis itself.** Connecting Fisher's identity → Xu–Jordan → Neal–Hinton to the
   2025 empirical observations of Bayesian geometry in transformers, and explaining those
   observations as consequences of objective structure, is a service to the field even
   though each link is individually known or knowable.

---

## V. Required Edits to the Paper

1. **Remove the overclaim** in sec-prior-work ("not, to our knowledge, previously stated as
   a formal identity"). Replace with an explicit acknowledgment that the identity is
   Fisher's identity specialized to LSE objectives.
2. **Add a subsection on the classical bridge** (Fisher, Xu–Jordan, Neal–Hinton,
   Salakhutdinov et al.) and reposition the contribution as framing + regimes + substrate.
3. **Moderate "is exactly EM"** in sec-main-result: exact statement is
   gradient = responsibility-weighted update direction; EM = the same gradient under a
   positive-definite preconditioner (Xu & Jordan). Keep the existing "implicit EM ≠
   coordinate ascent EM" hedge and strengthen it with the citation.
4. **Fix the attention regime** with the exact internal-softmax gradients (see
   `internal_softmax_gradient.md`), citing Agarwal et al. (2025b) for the attention-specific
   derivation and Ramsauer et al. (2020) for the forward-pass energy view.
5. **Cite the neural-EM lineage** (N-EM, EMANet, EM routing) as prior art for the
   attention/EM connection at the architectural level.
6. **Fix the author name**: the 2025 empirical papers are by **Agarwal**, Dalal & Misra
   (arXiv 2512.22471, 2512.22473), not "Agarwal." The bib and all prose must be corrected.
7. **Decouple the theorem from Oursland (2024)**: state the identity for arbitrary
   energies (it is purely algebraic), then offer the distance reading as an interpretation.
   The substrate paper motivates the semantics; it must not appear load-bearing for the math.

---

## Summary

- "Responsibilities are gradients" is **Fisher's identity** — classical, named, standard.
- "Gradient descent is (implicit) EM" is **Xu & Jordan (1996)** with more precision: EM is
  preconditioned gradient ascent.
- "E/M separation is not fundamental" is **Neal & Hinton (1998)**.
- The attention/EM connection at the module level is **Ramsauer / Greff / Li / Hinton**.
- What remains ours: the substrate framing, the three-regime taxonomy, the normalization
  boundary, the loss-level vs. internal-softmax distinction, and the synthesis explaining
  the 2025 transformer observations.

The paper survives this literature — but only if it stands on it instead of beside it.
