# Claims

## Purpose of This Document

This document enumerates the **explicit claims** of the current work.

Its goals are to:
- precisely state what is being asserted
- distinguish derivations from interpretations
- prevent accidental overclaiming
- provide a checklist against which the paper can be audited

If a statement does not appear here, it should not be implied in the paper.

---

## Primary Claim (Core Result)

**Claim 1 — Responsibilities as Gradients**

For objectives of the form:

\[
L(x) = \log \sum_j \exp(-d_j(x))
\]

the gradient of the loss with respect to each distance \( d_j \) is:

\[
\frac{\partial L}{\partial d_j} = - \frac{\exp(-d_j)}{\sum_k \exp(-d_k)}
\]

This quantity is exactly the posterior responsibility of component \( j \).

**Therefore:**
> Responsibilities arise directly as gradients of distance-based log-sum-exp objectives.

This claim is fully derived and requires no auxiliary assumptions beyond differentiability.

---

## Secondary Claims (Derived Consequences)

**Claim 2 — Implicit EM Dynamics**

Gradient descent on distance-based log-sum-exp objectives implements EM-like learning dynamics implicitly:

- Forward pass computes unnormalized likelihoods
- Normalization induces soft assignments
- Backpropagation produces responsibility-weighted updates

No explicit E-step or M-step is required.

---

**Claim 3 — Inference and Optimization Are Unified**

For objectives satisfying the above structure:

- inference (assignment of data to components)
- learning (parameter updates)

are the same process viewed at different levels.

There is no separation between inference and optimization.

---

**Claim 4 — Assignment Is Objective-Induced, Not Architectural**

The emergence of responsibilities depends on:

- the objective’s geometric structure
- exponentiation and normalization

It does **not** depend on:
- architectural motifs
- explicit mixture modeling
- auxiliary latent variables

---

## Generality Claims

**Claim 5 — Architectural Generality**

The derived mechanism applies to any model that:
- computes distances or energies
- uses exponentiation and normalization
- is trained by gradient descent

This includes (but is not limited to):
- standard ReLU networks
- attention mechanisms
- energy-based models
- metric learning models
- mixture models

---

**Claim 6 — Cross-Entropy as a Special Case**

Cross-entropy classification is a discriminative special case of the same objective structure:

- logits act as negative energies
- softmax induces responsibilities
- gradients gate learning by assignment

Supervision constrains, but does not eliminate, the underlying mechanism.

---

## Interpretive Claims (Clearly Marked)

The following claims are **interpretive**, not formal theorems:

**Claim 7 — EM Is Not an Algorithmic Add-On**

EM-like behavior in neural networks is not:
- an emergent coincidence
- an architectural trick
- a training heuristic

It is a necessary consequence of common objectives.

---

**Claim 8 — Geometry Precedes Probability**

Distances or energies are primary quantities.  
Probabilities are derived via exponentiation and normalization.

This reframes probability as an output of geometry, not an input.

---

## Claims Explicitly *Not* Made

The paper does **not** claim:

- that all neural networks are mixture models
- that training converges to true EM optima
- that models learn correct Bayesian posteriors
- that EM-like behavior guarantees good performance
- that distance-based objectives are universally optimal
- that this explains all Bayesian phenomena in deep learning

---

## Conditional Claims (Scope-Limited)

The following claims hold **only when stated conditions are met**:

- EM equivalence requires competition between outputs
- Responsibilities require normalization across alternatives
- Robust objectives trade learnability for outlier resistance

These conditions are documented in `limits_and_failure_modes.md`.

---

## Dependency on Prior Work

The following are **assumed**, not re-derived:

- Standard ReLU networks compute distances
- Outputs are energies, not confidences
- Normalization preserves geometric interpretation

These assumptions are detailed in `assumptions_from_prior_work.md`.

---

## Summary

The paper makes one core claim:

> **Responsibilities are gradients of distance-based log-sum-exp objectives.**

All other claims are consequences, interpretations, or scope clarifications of this result.

Anything beyond this is explicitly out of scope.
