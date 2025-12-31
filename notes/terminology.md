# Terminology

## Purpose of This Document

This note defines the **canonical terminology** used throughout this project.

Its goals are to:
- ensure consistent usage across notes and drafts
- avoid overloaded or misleading terms
- align language with the underlying geometry
- prevent accidental reintroduction of rejected interpretations

Terms defined here should be used consistently. Deviations should be intentional.

---

## Core Terms

### Distance
A scalar quantity measuring deviation from a learned reference structure.

- May be signed or unsigned
- May be scaled by learned parameters
- Need not satisfy metric axioms globally

Used interchangeably with **energy** when sign conventions differ.

---

### Energy
A scalar quantity whose exponentiated negative defines relative likelihood.

- Lower energy = higher likelihood
- Energies are primary; probabilities are derived
- Logits are treated as negative energies

Energy emphasizes probabilistic interpretation; distance emphasizes geometry.

---

### Prototype
A learned reference component against which distances are computed.

- Not necessarily a point in input space
- May be a surface, region, or implicit structure
- Parameterized by network weights

Avoids the implication of a “template” or exemplar.

---

### Component
Synonym for prototype when emphasizing mixture structure.

Used when discussing EM, responsibilities, or latent assignments.

---

### Responsibility
A normalized, non-negative weight indicating the degree to which a component explains an input.

- Sums to 1 across competing components
- Emerges as a gradient of log-sum-exp objectives
- Identical to attention weights in attention mechanisms

Responsibilities are **not auxiliary variables**.

---

### Assignment
The process by which responsibility mass is distributed across components.

- Soft by default
- Hard only when externally constrained (e.g., labels)

Assignment is implicit, continuous, and objective-driven.

---

## Objective-Level Terms

### Log-Sum-Exp Objective
An objective of the form:

\[
L = \log \sum_j \exp(-d_j)
\]

- Induces competition
- Produces responsibilities
- Central to implicit EM dynamics

---

### Cross-Entropy
A supervised discriminative variant of log-sum-exp.

- Clamps one assignment via labels
- Preserves competition and responsibility structure
- Enforces closed-world assumptions

Cross-entropy is not treated as fundamentally distinct.

---

### Normalization
Any operation that rescales energies across alternatives.

- Softmax
- Log-sum-exp
- Partition functions

Normalization induces competition and assignment.

---

## Optimization and Dynamics

### Implicit EM
The phenomenon where gradient descent on certain objectives produces EM-like dynamics.

- No explicit E-step or M-step
- Continuous rather than alternating
- Responsibilities arise as gradients

“Implicit” refers to absence of algorithmic separation, not approximation.

---

### Gradient Descent
The standard optimization procedure used to minimize objectives.

- Backpropagation computes gradients
- Gradients encode responsibility structure
- Optimization performs inference

No specialized optimizer is assumed.

---

## Attention-Specific Terms

### Attention Score
An unnormalized energy measuring compatibility between a query and a key.

- Interpreted as negative distance
- Not a confidence score

---

### Attention Weight
The normalized exponentiation of attention scores.

- Identical to responsibilities
- Gates value contribution and learning

---

### Value
A parameter or representation updated proportionally to attention weights.

- Acts as a prototype
- Specializes via responsibility-weighted updates

---

## Terms Explicitly Avoided

### Confidence
Avoided because:
- implies calibrated belief
- conflates magnitude with certainty
- obscures geometric interpretation

Use **energy**, **distance**, or **likelihood** instead.

---

### Template
Avoided because:
- implies point matching
- suggests cosine similarity
- conflicts with region- or surface-based interpretation

Use **prototype** instead.

---

### Bayesian (Unqualified)
Avoided unless carefully scoped.

The work explains **Bayesian-like dynamics**, not full Bayesian inference.

---

## Summary

This terminology enforces three principles:

1. Geometry precedes probability
2. Assignment is objective-induced, not heuristic
3. Inference emerges from optimization

Consistent language is essential to keeping the theory coherent.
