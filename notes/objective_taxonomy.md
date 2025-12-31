# Objective Taxonomy

## Purpose of This Document

This note provides a **taxonomy of common learning objectives**, organized by their **geometric structure and gradient behavior**, rather than by task (classification vs regression) or historical lineage.

The goal is to:
- show how many losses differ only in geometry
- clarify which objectives induce responsibility structure
- identify tradeoffs between robustness and learnability
- support the unification narrative at the objective level

This is a classificatory document, not a proposal.

---

## Organizing Principle

Objectives are classified by three structural properties:

1. **Energy / Distance Representation**
   - Does the objective operate on energies or distances?
2. **Exponentiation**
   - Are energies exponentiated to form relative likelihoods?
3. **Normalization / Competition**
   - Are alternatives normalized against each other?

These properties determine whether:
- responsibilities emerge
- gradients gate learning by assignment
- EM-like dynamics occur

---

## Category I — Log-Sum-Exp Objectives (Implicit EM)

### Structural Form

\[
L = \log \sum_j \exp(-d_j)
\]

### Properties

- Energies: ✔
- Exponentiation: ✔
- Normalization: ✔
- Responsibilities: ✔
- EM-like dynamics: ✔
- Strong competition: ✔

### Examples

- Unsupervised mixture likelihood
- Cross-entropy (discriminative variant)
- Attention softmax
- Energy-based models with partition functions

### Characteristics

- Soft assignment is unavoidable
- Gradients are responsibility-weighted
- Specialization emerges naturally
- Stable learning for misassigned points

This category defines the **core mechanism** of the current work.

---

## Category II — Discriminative Log-Sum-Exp (Supervised EM)

### Structural Form

\[
L = d_y + \log \sum_k \exp(-d_k)
\]

### Properties

- Energies: ✔
- Exponentiation: ✔
- Normalization: ✔
- Responsibilities: ✔ (constrained)
- EM-like dynamics: ✔ (clamped)
- External supervision: ✔

### Examples

- Softmax cross-entropy
- Multi-class logistic regression

### Characteristics

- Assignment is partially overridden by labels
- Competition is preserved
- Learning remains responsibility-weighted
- Closed-world assumption enforced

This is the most common objective in practice.

---

## Category III — Local Kernel Objectives (Robust, Non-Competitive)

### Structural Form

\[
L = 1 - \exp(-d^2 / \sigma^2)
\]

(or equivalent)

### Properties

- Energies: ✔
- Exponentiation: ✔
- Normalization: ✖
- Responsibilities: ✖
- EM-like dynamics: ✖
- Locality: ✔

### Examples

- Maximum correntropy
- Welsch / Leclerc loss
- Gaussian kernel regression

### Characteristics

- Robust to outliers
- Vanishing gradients for large distances
- No competition between hypotheses
- No assignment structure

These objectives trade global correction for robustness.

---

## Category IV — Metric Learning Objectives (Explicit Margins)

### Structural Form

- Contrastive loss
- Triplet loss
- Margin-based objectives

### Properties

- Energies: ✔
- Exponentiation: ✖ (often)
- Normalization: ✖
- Responsibilities: ✖
- EM-like dynamics: ✖
- Explicit margins: ✔

### Examples

- Triplet loss
- Contrastive loss
- Large-margin nearest neighbor

### Characteristics

- Distances are optimized directly
- Assignment is imposed externally (pairs/triples)
- No implicit mixture structure
- Requires careful sampling

These objectives encode geometry but not inference.

---

## Category V — Quadratic Objectives (Global, Non-Probabilistic)

### Structural Form

\[
L = \|y - \hat{y}\|^2
\]

### Properties

- Energies: ✖ (implicit)
- Exponentiation: ✖
- Normalization: ✖
- Responsibilities: ✖
- EM-like dynamics: ✖
- Global influence: ✔

### Examples

- Mean squared error
- Least squares regression

### Characteristics

- Penalizes outliers heavily
- No competition
- No assignment
- Simple but brittle

These objectives minimize energy, not uncertainty.

---

## Comparative Summary Table

| Objective Type | Competition | Responsibilities | Robustness | EM-like |
|---------------|-------------|------------------|------------|---------|
| Log-sum-exp | ✔ | ✔ | ✖ | ✔ |
| Cross-entropy | ✔ | ✔ (clamped) | ✖ | ✔ |
| Correntropy | ✖ | ✖ | ✔ | ✖ |
| Metric learning | ✖ | ✖ | ✖ | ✖ |
| MSE | ✖ | ✖ | ✖ | ✖ |

---

## Key Insight

The presence or absence of **normalization across alternatives** is the decisive factor.

- Exponentiation without normalization → robustness
- Normalization without supervision → latent inference
- Supervision without normalization → independent prediction
- All three → implicit EM

Loss functions differ primarily in **what geometry they impose**, not in what task they nominally solve.

---

## Summary

This taxonomy shows that:

- many objectives differ only in structural details
- EM-like behavior is not ubiquitous, but conditional
- competition and normalization are essential
- robustness and inference trade off

Understanding objectives geometrically clarifies both their behavior and their limits.
