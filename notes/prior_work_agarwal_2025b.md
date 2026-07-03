# Prior Work: Agarwal et al. (2025b) — Gradient Dynamics of Attention

## Purpose of This Document

This note clarifies how the current work (*implicit EM via gradients*) relates to:

> **Gradient Dynamics of Attention: How Cross-Entropy Sculpts Bayesian Manifolds**  
> Agarwal et al., 2025

The goal is to:
- identify genuine overlap vs complementarity
- distinguish mechanism-level analysis from objective-level derivation
- explain what the present work adds conceptually
- avoid redundancy or misattribution of results

The two works are closely aligned but operate at **different explanatory depths**.

---

## Summary of Agarwal et al. (2025b)

Agarwal et al. analyze **how gradients flow through attention layers trained with cross-entropy**.

Core contributions:
- Derivation of first-order gradients for attention scores and values
- Demonstration that attention weights behave like soft assignments
- Identification of two-timescale dynamics:
  - attention weights stabilize early
  - value vectors continue to refine
- EM-like interpretation of attention updates

Key characteristics:
- Mechanistic and analytical
- Focused specifically on attention layers
- Grounded in cross-entropy training
- Concerned with *how* gradients behave during training

The paper answers:
> *How does cross-entropy shape attention dynamics during training?*

---

## What Agarwal et al. Do *Not* Establish

**Correction (2026-07, after reading the actual paper):** an earlier version of this note
said their "derivation is not attempted" and their framing is "not objective-derived."
That was wrong. They **do** derive the gradient laws from cross-entropy — the advantage
routing law \( \partial L/\partial s_{ij} = \alpha_{ij}(b_{ij} - \mathbb{E}_{\alpha_i}[b]) \)
and the responsibility-weighted value update \( \Delta v_j = -\eta \sum_i \alpha_{ij} u_i \)
are boxed core results of their paper. The mechanics are theirs and exact.

What they decline is the **probabilistic interpretation**:

- they do not interpret the dynamics via a likelihood or density model over inputs — in
  their words (§5.2), values move to explain the error geometry "rather than to maximize a
  likelihood over inputs. The analogy is structural rather than variational"
- they present the EM connection as a "mechanistic correspondence," "not as a literal
  optimization of an explicit latent-variable likelihood"
- they do not generalize beyond attention mechanisms
- they do not connect gradient behavior to distance-based objectives
- they do not identify responsibilities as posteriors of an implicit mixture

The quote "structural rather than variational" appears specifically in the context of
value updates being driven by the backpropagated error \( u_i \) rather than by observed
data. **Cite it with that context** — it is a scoped caveat, not a global disclaimer.

---

## Scope of the Current Work

The current work addresses a deeper causal layer:

- distance- or energy-based objectives
- exponentiation and normalization
- log-sum-exp structure
- emergence of responsibilities as gradients
- equivalence between gradient descent and EM

Key question answered:
> *Why do EM-like gradient dynamics arise at all, rather than something else?*

This question is orthogonal to architectural details.

---

## Relationship Between the Two Works

The relationship can be summarized as:

| Aspect | Agarwal et al. (2025b) | Current Work |
|------|-------------------------|--------------|
| Primary question | How do gradients behave in attention? | Why do gradients encode responsibilities? |
| Level | Mechanism-level | Objective-level |
| Method | Gradient analysis | Objective derivation |
| Scope | Attention-specific | Architecture-agnostic |
| EM framing | Analogy | Necessary consequence |

Agarwal et al. show **what happens**.  
The current work explains **why it must happen**.

---

## Responsibilities vs Gradient Modulation

Agarwal et al. show that attention gradients take the form:
- attention weight × advantage-like error term
- responsibility-weighted updates to values

The current work shows that:
- normalized exponentials of distances *are* responsibilities
- these quantities appear directly as gradients
- no additional structure is required

Thus, the gradient forms derived by Agarwal et al. are a **special case** of a more general phenomenon.

---

## EM Analogy vs EM Equivalence

Agarwal et al. describe attention learning as *EM-like*:
- E-like phase: attention weights settle
- M-like phase: values update

and are explicit that for attention the correspondence is structural (values chase error
geometry, not likelihood).

The current work **delimits rather than overturns** their caveat:
- **at the loss level** (mixture likelihood, output-layer cross-entropy) the EM
  correspondence is an *identity* — Fisher's identity; responsibilities are posteriors of
  an implicit mixture, and the variational reading is exact
- **inside the network** (attention) their structural caveat is correct, and our
  internal-softmax analysis (`internal_softmax_gradient.md`) gives it precise form:
  competition is over downstream usefulness, not likelihood
- their 2025a population-optimum theorem is the endpoint statement of the loss-level case;
  the responsibility-gradient identity is its per-step counterpart

This is the central distinction: **where the LSE sits determines whether EM is variational
(loss) or structural (interior).** We agree with their caveat where it applies and supply
the probabilistic status where it does not.

---

## Why the Current Work Adds Value

The present work contributes:

1. **Objective-level grounding**
   - EM dynamics are induced by log-sum-exp objectives

2. **Architectural generality**
   - applies beyond attention to any distance-based model

3. **Removal of special pleading**
   - no need to treat attention as unique or privileged

4. **Clarification of causality**
   - gradient structure follows from geometry, not from design choices

---

## Complementarity

Agarwal et al. (2025b):
- precisely characterize gradient dynamics
- validate EM-like behavior empirically and analytically
- focus on attention as a case study

The current work:
- explains why those dynamics arise
- generalizes the phenomenon
- reframes EM as implicit and continuous

The two works reinforce each other.

---

## Recommended Positioning Language

A clean way to relate the papers:

> *Agarwal et al. (2025b) analyze the gradient dynamics of attention layers trained with cross-entropy, identifying EM-like specialization behavior. The present work provides an objective-level explanation for these dynamics, showing that responsibilities emerge directly as gradients of distance-based log-sum-exp objectives.*

This makes the relationship explicit and non-competitive.

---

## Summary

- Agarwal et al. (2025b): **exact gradient mechanics of attention under CE** (derived, not
  merely observed), with a scoped caveat that the EM reading is structural for attention
- Current work: **the probabilistic status of those gradients** — variational at the loss
  level (Fisher's identity, implicit mixture posteriors), structural in the interior
  (their caveat, given precise form)
- Distinct contribution: mechanics vs semantics, and the delimitation between them

The current work should be read as supplying the **probabilistic semantics and its limits**
for the gradient phenomena Agarwal et al. derive and document, not as a reanalysis of their
results — and never as claiming they "did not attempt the derivation." They did.
