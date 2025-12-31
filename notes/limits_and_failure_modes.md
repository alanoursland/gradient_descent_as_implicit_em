# Limits and Failure Modes (Revised)

## Purpose of This Document

This note delineates the **true limits and failure modes** of the implicit-EM-via-gradients framework, incorporating the perspective that **standard ReLU networks already implement distance-based geometry**.

The goal is to:
- avoid overstating conditional assumptions
- clarify what is structural vs optional
- identify genuine failure modes
- prevent misinterpretation of scope

This work does not claim universality, but its domain of applicability is **broader than initially stated**.

---

## What Is Structural (Not Assumed)

Based on prior work, we treat the following as **facts about standard neural networks**, not modeling choices:

- Affine layers + ReLU compute signed distances to learned hyperplanes
- Logits and attention scores are energies, not confidences
- Normalization (explicit or implicit) changes scale, not interpretation

Therefore, the distance-based perspective is **inherent to standard architectures**, not a special case.

The limits of this framework arise **after** this geometric layer.

---

## Core Conditions for Implicit EM Dynamics

Given distance-based representations (which standard networks already compute), EM-like dynamics arise when the **objective introduces competition and normalization**.

Specifically, the framework relies on:

1. **Exponentiation of Energies**
   - e.g. softmax, log-sum-exp, Gaussian kernels
   - converts distances into relative likelihoods

2. **Competition Between Prototypes**
   - outputs must be normalized across alternatives
   - independent channels do not produce responsibilities

3. **Gradient-Based Optimization**
   - learning proceeds via backpropagation
   - responsibilities appear as gradients

If these are present, implicit EM dynamics follow necessarily.

---

## Genuine Failure Modes

### Lack of Competition

If outputs do not compete (e.g., independent sigmoids without normalization):

- no responsibilities are formed
- gradients do not gate learning by assignment
- specialization must be externally enforced

This is the **primary structural failure mode**.

---

### Objectives Without Log-Sum-Exp Structure

Losses that:
- operate on bounded probabilities directly
- lack an underlying energy interpretation
- do not induce log-sum-exp coupling

do not generate responsibility-weighted gradients.

The failure is objective-level, not architectural.

---

### Vanishing-Gradient Regimes

Certain distance-based objectives (e.g., Gaussian kernels, correntropy):

- intentionally suppress gradients for large distances
- ignore outliers by design
- can stall learning if initialization is poor

This is a **robustness–learnability tradeoff**, not a contradiction of the theory.

---

### Scale and Volume Pathologies

While distances are structural, **scale is not automatically controlled**.

Failure modes include:
- collapsing metrics (all distances → 0)
- exploding metrics (all distances → ∞)
- degenerate directions in learned metrics

Neural networks often manage this implicitly via:
- normalization layers
- weight decay
- architectural constraints

The framework explains *why* these issues arise, but does not eliminate them.

---

## Supervision-Specific Limits

### Hard Supervision Overrides Assignment

In fully supervised cross-entropy:

- labels impose external assignments
- latent mixture structure is partially overridden
- EM equivalence becomes conditional

The framework still applies, but inference is **constrained by labels**.

---

### Closed-World Assumptions

Softmax classification:
- forces every input to be assigned
- lacks an explicit rejection option
- can mis-handle out-of-distribution inputs

This is a limitation of the objective, not of distance-based geometry.

---

## Attention-Specific Caveats

### Finite Capacity and Entanglement

While attention implements responsibility-weighted updates:

- heads have limited capacity
- multiple latent causes may be entangled
- clean mixture separation is not guaranteed

The framework predicts assignment behavior, not perfect disentanglement.

---

### Non-Metric Energies

Attention scores:
- may violate symmetry or triangle inequality
- need not define a true metric

The theory applies to **energies**, not strictly metrics. Metric violations do not break the framework.

---

## What This Framework Does Not Attempt to Explain

This work does **not** address:

- generalization bounds
- scaling laws
- long-horizon planning
- symbolic reasoning
- emergent capabilities

It isolates and explains one mechanism: **assignment via gradients**.

---

## Summary

With the distance interpretation treated as structural:

- the framework applies to standard ReLU networks
- EM-like dynamics are broadly unavoidable under common objectives
- true failure modes arise from lack of competition, not lack of geometry

The limits of the theory are **objective-level and scale-related**, not architectural.

Understanding these limits sharpens the framework rather than weakening it.
