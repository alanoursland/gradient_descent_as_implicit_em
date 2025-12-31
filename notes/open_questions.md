# Open Questions

## Purpose of This Document

This note enumerates **open questions and unresolved issues** raised by the implicit EM via gradients framework.

The goal is to:
- distinguish what is explained from what is not
- identify directions for future work
- clarify where theory ends and empirical behavior begins
- avoid implying completeness

These questions do not undermine the framework; they define its frontier.

---

## Objective-Level Questions

### 1. What Happens Without Normalization?

The framework relies critically on normalization across alternatives.

Open questions:
- Are there objectives that induce soft assignment without explicit normalization?
- Can approximate normalization (e.g., local competition) suffice?
- How much normalization is required for responsibilities to emerge meaningfully?

---

### 2. Intermediate Objectives

Between:
- fully normalized log-sum-exp objectives
- fully local kernel objectives (e.g., correntropy)

lie many hybrid losses.

Open questions:
- Is there a smooth spectrum between inference and robustness?
- Can objectives interpolate continuously between EM-like and robust regimes?
- How does this affect convergence and specialization?

---

## Geometry and Scale

### 3. Learned Volume Control

Standard EM includes covariance and determinant terms.

Open questions:
- Can neural networks learn volume terms implicitly?
- When does normalization substitute for explicit volume control?
- How do architectures implicitly regulate metric scale?

---

### 4. Degenerate Metric Avoidance

While distances are structural, metrics can become degenerate.

Open questions:
- What mechanisms prevent metric collapse in practice?
- Are there objective-level regularizers that enforce healthy geometry?
- How do normalization layers interact with metric degeneracy?

---

## Training Dynamics

### 5. Initialization Sensitivity

Some distance-based objectives exhibit vanishing gradients far from solutions.

Open questions:
- How sensitive is implicit EM to initialization?
- Are there principled warm-start strategies?
- Can curriculum or annealing recover lost gradients?

---

### 6. Optimization Schedules

EM is classically alternating; gradient descent is continuous.

Open questions:
- When do EM-style phase separations appear in gradient descent?
- Are there regimes where implicit EM fails to stabilize?
- How do learning rates and batch sizes affect assignment dynamics?

---

## Supervision and Labels

### 7. Partial and Noisy Supervision

Cross-entropy clamps assignments.

Open questions:
- How does label noise interact with responsibility structure?
- Can partial supervision be modeled as soft assignment constraints?
- Is there a principled bridge between supervised and unsupervised regimes?

---

### 8. Open-Set and Unknown Classes

Standard objectives enforce closed-world assumptions.

Open questions:
- How can objectives relax forced assignment?
- Can implicit EM support explicit rejection?
- What objective structures induce “none-of-the-above” behavior?

---

## Attention-Specific Questions

### 9. Capacity vs Assignment

Attention heads have limited capacity.

Open questions:
- How many effective prototypes can a head support?
- When do responsibilities entangle multiple latent causes?
- Does head specialization reflect stable mixture components?

---

### 10. Temporal Stability of Assignments

Attention assignments are transient.

Open questions:
- Can persistent latent components emerge?
- How do responsibilities evolve across layers?
- What stabilizes long-term component identity?

---

## Empirical Validation

### 11. Observable Markers of Implicit EM

Open questions:
- How can responsibility emergence be measured directly?
- What diagnostics distinguish implicit EM from heuristic routing?
- Can assignment dynamics be visualized meaningfully?

---

### 12. Failure Mode Detection

Open questions:
- How can metric collapse be detected early?
- What signals indicate broken competition?
- Are there training-time indicators of assignment degeneration?

---

## Broader Theoretical Questions

### 13. Relationship to Variational Inference

Open questions:
- Can implicit EM be formalized variationally?
- Is there an implicit variational objective being optimized?
- How does this relate to ELBO-style formulations?

---

### 14. Limits of Unification

Open questions:
- Which phenomena definitively lie outside this framework?
- Are there inference-like behaviors with no objective explanation?
- What mechanisms are orthogonal to assignment dynamics?

---

## Summary

This framework resolves a central question:
> *Why do EM-like and Bayesian behaviors arise under standard training?*

It opens many others.

These open questions define a research agenda focused on:
- objective design
- geometry control
- inference under supervision
- empirical diagnostics

Answering them would extend, not revise, the core theory.
