# Prior Work: Agarwal et al. (2025a) — The Bayesian Geometry of Transformer Attention

## Purpose of This Document

This note clarifies how the current work (*implicit EM via gradients*) relates to:

> **The Bayesian Geometry of Transformer Attention** (Agarwal et al., 2025)

The goal is to:
- identify genuine overlap vs complementarity
- clarify differences in scope and claims
- explain why the present work adds explanatory depth
- avoid redundancy or priority confusion

The two works are strongly aligned but operate at **different explanatory levels**.

---

## Summary of Agarwal et al. (2025a)

Agarwal et al. investigate **what trained transformer attention layers represent**.

Core findings (corrected 2026-07 after reading the paper):
- In "Bayesian wind tunnels" (closed-form posteriors, memorization impossible), small
  transformers match analytic posterior entropy position-by-position to 10^-3–10^-4 bits;
  capacity-matched MLPs "fail catastrophically" (~618x worse on the bijection task)
- **Value representations** unfold into low-dimensional manifolds parameterized by
  posterior entropy (the manifold lives in the values/residual stream, not in the
  attention weights)
- Mechanistic division of labor: residual stream = belief substrate, feed-forward
  networks = numerical posterior update, attention = content-addressable routing
- NOTE: they frame attention as *routing*, not as responsibilities or soft assignment —
  responsibility language is ours, not theirs
- They prove an endpoint theorem: the population optimum of cross-entropy is the Bayes
  posterior predictive (architecture-agnostic)

Key characteristics:
- Empirical and mechanistic
- Post-hoc analysis of trained models
- Focus on representational geometry
- Bayesian interpretation of internal states

The paper answers:
> *What structure do transformers learn?*

---

## What Agarwal et al. Do *Not* Derive

Critically, Agarwal et al. (2025a) do **not**:

- explain the training-dynamics mechanism in this paper (they defer gradient dynamics to
  the companion paper, 2025b — so "they don't derive it" is only true of 2025a in
  isolation, and must not be asserted of the pair)
- connect attention to density estimation or mixture modeling
- describe attention weights as responsibilities or soft assignments (their frame is
  content-addressable routing)
- provide a variational or likelihood-level interpretation of the intermediate quantities

Their population-optimum theorem *is* an objective-level statement — it explains why the
optimum is Bayesian. What it does not address (and what they flag as architecture's role)
is why transformers reach that optimum while MLPs do not, and what the internal quantities
mean along the way.

---

## Scope of the Current Work

The current work addresses the **objective-level cause** of the phenomena observed by Agarwal et al.

Core focus:
- distance / energy-based objectives
- exponentiation and normalization
- log-sum-exp structure
- gradient flow
- emergence of responsibilities

Key question answered:
> *Why do standard neural objectives produce inference-like behavior at all?*

---

## Relationship Between the Two Works

The relationship can be summarized as:

| Aspect | Agarwal et al. (2025a) | Current Work |
|------|-------------------------|--------------|
| Question | What geometry do transformers exhibit? | What objective forces this geometry? |
| Method | Empirical probing & analysis | Analytical derivation |
| Level | Representation-level | Objective-level |
| Focus | Belief manifolds | Responsibilities & gradients |
| Training loss | Assumed (cross-entropy) | Analyzed directly |

Agarwal et al. describe **the result**.  
The current work explains **the cause**.

---

## Responsibilities vs Belief Geometry

Agarwal et al. show that:
- internal representations align with posterior distributions
- belief states evolve smoothly during inference

The current work shows that:
- posterior-like quantities arise as normalized exponentials of distances
- these quantities are identical to gradients of log-sum-exp objectives
- assignment and specialization are unavoidable consequences of the loss

Thus, belief geometry is not incidental—it is **structurally induced**.

---

## Attention as a Special Case

Agarwal et al. analyze attention mechanisms specifically.

The current work generalizes:
- attention scores as negative energies or distances
- attention weights as responsibilities
- value vectors as prototypes updated by responsibility-weighted gradients

This reframes attention not as a special Bayesian mechanism, but as:
> one instantiation of a general distance-based inference pattern.

---

## Complementarity, Not Redundancy

Agarwal et al.:
- demonstrate Bayesian structure empirically
- validate that inference-like representations exist

The current work:
- derives why such structure must emerge
- shows that EM-like dynamics are embedded in gradient descent
- applies beyond transformers to any distance-based objective

Neither paper subsumes the other.

---

## Why This Work Adds to Agarwal et al.

The present work adds:

1. **Objective-level necessity**
   - Bayesian geometry is forced by the loss, not learned accidentally

2. **Mechanism-level explanation**
   - responsibilities arise as gradients
   - no auxiliary inference procedure is required

3. **Broader generality**
   - applies to mixture models, energy-based models, metric learning, and CE
   - not transformer-specific

4. **Clarification of scope**
   - distinguishes representational geometry from learning dynamics

---

## Recommended Positioning Language

A clean way to relate the two works:

> *Agarwal et al. (2025a) empirically demonstrate that transformer attention layers represent Bayesian belief geometry. The present work provides an objective-level explanation for this phenomenon, showing that distance-based log-sum-exp objectives necessarily induce responsibility-weighted, EM-like learning dynamics under gradient descent.*

This positions the papers as complementary layers of explanation.

---

## Summary

- Agarwal et al. (2025a): **What** Bayesian structure appears in transformers
- Current work: **Why** such structure is unavoidable given the objective
- Shared worldview: geometry-first, inference-as-learning
- Distinct contributions: observation vs derivation

The current work should be read as an **explanatory foundation** for the phenomena documented by Agarwal et al., not as a reinterpretation or extension of their empirical results.
