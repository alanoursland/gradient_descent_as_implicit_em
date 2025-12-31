# Prior Work: Aggarwal et al. (2025a) — The Bayesian Geometry of Transformer Attention

## Purpose of This Document

This note clarifies how the current work (*implicit EM via gradients*) relates to:

> **The Bayesian Geometry of Transformer Attention** (Aggarwal et al., 2025)

The goal is to:
- identify genuine overlap vs complementarity
- clarify differences in scope and claims
- explain why the present work adds explanatory depth
- avoid redundancy or priority confusion

The two works are strongly aligned but operate at **different explanatory levels**.

---

## Summary of Aggarwal et al. (2025a)

Aggarwal et al. investigate **what trained transformer attention layers represent**.

Core findings:
- Attention heads encode low-dimensional Bayesian belief manifolds
- Residual stream representations correspond to posterior belief states
- Internal activations track entropy and uncertainty
- Transformers trained with cross-entropy perform approximate Bayesian inference

Key characteristics:
- Empirical and mechanistic
- Post-hoc analysis of trained models
- Focus on representational geometry
- Bayesian interpretation of internal states

The paper answers:
> *What structure do transformers learn?*

---

## What Aggarwal et al. Do *Not* Derive

Critically, Aggarwal et al. do **not**:

- derive attention behavior from the training objective
- explain why cross-entropy induces Bayesian geometry
- connect attention to density estimation or mixture modeling
- show how responsibilities arise mathematically
- provide a variational or likelihood-level explanation

They explicitly treat Bayesian behavior as an *emergent property* of training, not as a necessary consequence of the objective.

---

## Scope of the Current Work

The current work addresses the **objective-level cause** of the phenomena observed by Aggarwal et al.

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

| Aspect | Aggarwal et al. (2025a) | Current Work |
|------|-------------------------|--------------|
| Question | What geometry do transformers exhibit? | What objective forces this geometry? |
| Method | Empirical probing & analysis | Analytical derivation |
| Level | Representation-level | Objective-level |
| Focus | Belief manifolds | Responsibilities & gradients |
| Training loss | Assumed (cross-entropy) | Analyzed directly |

Aggarwal et al. describe **the result**.  
The current work explains **the cause**.

---

## Responsibilities vs Belief Geometry

Aggarwal et al. show that:
- internal representations align with posterior distributions
- belief states evolve smoothly during inference

The current work shows that:
- posterior-like quantities arise as normalized exponentials of distances
- these quantities are identical to gradients of log-sum-exp objectives
- assignment and specialization are unavoidable consequences of the loss

Thus, belief geometry is not incidental—it is **structurally induced**.

---

## Attention as a Special Case

Aggarwal et al. analyze attention mechanisms specifically.

The current work generalizes:
- attention scores as negative energies or distances
- attention weights as responsibilities
- value vectors as prototypes updated by responsibility-weighted gradients

This reframes attention not as a special Bayesian mechanism, but as:
> one instantiation of a general distance-based inference pattern.

---

## Complementarity, Not Redundancy

Aggarwal et al.:
- demonstrate Bayesian structure empirically
- validate that inference-like representations exist

The current work:
- derives why such structure must emerge
- shows that EM-like dynamics are embedded in gradient descent
- applies beyond transformers to any distance-based objective

Neither paper subsumes the other.

---

## Why This Work Adds to Aggarwal et al.

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

> *Aggarwal et al. (2025a) empirically demonstrate that transformer attention layers represent Bayesian belief geometry. The present work provides an objective-level explanation for this phenomenon, showing that distance-based log-sum-exp objectives necessarily induce responsibility-weighted, EM-like learning dynamics under gradient descent.*

This positions the papers as complementary layers of explanation.

---

## Summary

- Aggarwal et al. (2025a): **What** Bayesian structure appears in transformers
- Current work: **Why** such structure is unavoidable given the objective
- Shared worldview: geometry-first, inference-as-learning
- Distinct contributions: observation vs derivation

The current work should be read as an **explanatory foundation** for the phenomena documented by Aggarwal et al., not as a reinterpretation or extension of their empirical results.
