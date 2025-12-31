# Relation to Cross-Entropy

## Purpose of This Document

This note clarifies how the current work relates to **cross-entropy loss**, which is the dominant training objective in modern neural networks.

The goal is to:
- situate cross-entropy within the implicit EM framework
- explain what carries over and what changes under supervision
- address common objections preemptively
- avoid mischaracterizing cross-entropy as an exception

Cross-entropy is not a counterexample to this work. It is the **most important special case**.

---

## Cross-Entropy as a Distance-Based Objective

In standard classification, the model produces logits \( z_j(x) \), and cross-entropy loss is defined as:

\[
L = -\log \frac{\exp(z_y)}{\sum_k \exp(z_k)}
\]

Under the distance-based interpretation:

- logits \( z_j \) are **negative energies or distances**
- \( d_j = -z_j \)
- softmax is normalization over exponentiated distances

Thus, cross-entropy has the same structural form as:

\[
L = d_y + \log \sum_k \exp(-d_k)
\]

This is a **discriminative log-sum-exp objective**.

---

## Responsibilities in Cross-Entropy

Softmax probabilities:

\[
p_j = \frac{\exp(z_j)}{\sum_k \exp(z_k)}
\]

are exactly:

\[
p_j = \frac{\exp(-d_j)}{\sum_k \exp(-d_k)}
\]

which are the same responsibilities derived in the unsupervised case.

The difference is not the mechanism, but the **source of constraint**.

---

## Gradient Structure Under Cross-Entropy

The gradient of cross-entropy with respect to logits is:

\[
\frac{\partial L}{\partial z_j} = p_j - \mathbb{1}[j = y]
\]

Equivalently, in distance form:

\[
\frac{\partial L}{\partial d_j} =
\begin{cases}
p_j - 1 & j = y \\
p_j & j \neq y
\end{cases}
\]

This has a clear interpretation:

- the model assigns responsibility mass to all classes
- the correct class is externally forced to take full responsibility
- incorrect classes are penalized in proportion to their responsibility

Thus, **cross-entropy overrides latent assignment with labels**, but does not eliminate the responsibility structure.

---

## Cross-Entropy as Constrained EM

From the perspective of this work:

- unsupervised log-sum-exp: responsibilities are latent
- cross-entropy: one responsibility is clamped to 1

This corresponds to a **partially observed mixture model**, where:
- component identity is observed for each sample
- but competition and normalization remain intact

Cross-entropy is EM with **hard supervision injected into the E-step**.

---

## What Changes Under Supervision

Supervision introduces three important changes:

1. **Assignments are no longer free**
   - the correct component must dominate
   - latent mixture structure is constrained

2. **Inference is asymmetric**
   - only the correct class receives positive reinforcement
   - others are repelled regardless of geometry

3. **Mixture interpretation is limited**
   - per-class distributions need not be faithful densities
   - calibration is not guaranteed

The underlying mechanism remains the same.

---

## What Does Not Change

Even under cross-entropy:

- outputs still compete
- responsibilities still gate gradients
- specialization still occurs
- assignment still emerges from normalization

Cross-entropy does not replace the implicit EM mechanism — it **directs it**.

---

## Why Cross-Entropy “Just Works”

From this perspective, cross-entropy is effective because:

- it preserves competition
- it preserves responsibility-weighted gradients
- it avoids vanishing gradients for wrong predictions
- it enforces strong separation early in training

Its success is structural, not accidental.

---

## Limitations of Cross-Entropy

Cross-entropy also inherits limitations:

- closed-world assumption
- forced assignment for all inputs
- poor handling of unknowns
- limited robustness to outliers

These are consequences of **hard responsibility constraints**, not failures of distance-based geometry.

---

## Summary

Cross-entropy fits cleanly into the implicit EM framework:

- logits are energies
- softmax induces responsibilities
- gradients are responsibility-weighted
- supervision clamps assignments

The difference between unsupervised EM and cross-entropy is **not mechanism**, but **constraint**.

Understanding this reframes cross-entropy as a constrained inference process, not merely a classification loss.
