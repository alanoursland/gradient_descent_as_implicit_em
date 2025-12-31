# Paper Outline

**Gradient Descent as Implicit EM in Distance-Based Neural Models**

---

## 1. Introduction

### 1.1 Motivation

* EM, mixture models, attention, and Bayesian interpretations repeatedly appear in modern neural networks
* These behaviors are often treated as:

  * architectural coincidences
  * emergent properties
  * or approximations
* Lack of a **single objective-level explanation**

### 1.2 Core Claim

* Show that **standard distance-based objectives** induce **EM-like responsibility-weighted learning dynamics** under gradient descent
* No explicit latent variables, inference steps, or EM algorithms are required

### 1.3 Key Insight (Preview)

* Responsibilities are **not computed** — they are **gradients**
* Inference and learning collapse into the same computation

### 1.4 Scope and Contributions

* Objective-level analysis
* Architecture-agnostic
* Explanatory, not algorithmic
* Summary of contributions (bulleted)

---

## 2. Background and Framing

### 2.1 Distance-Based Interpretation of Neural Outputs (Imported)

* Briefly summarize prior result:

  * standard neural networks compute distances / energies
  * logits and scores are not confidences
* Explicitly defer full derivation to prior work

*(This section is short and citation-heavy, not argumentative.)*

---

### 2.2 EM and Responsibilities (Classical View)

* Brief recap of EM:

  * responsibilities
  * E-step / M-step separation
* Emphasize what EM *requires structurally*, not procedurally

---

### 2.3 Log-Sum-Exp Objectives

* Introduce log-sum-exp as:

  * marginal likelihood
  * normalization over alternatives
* Set up notation used throughout the paper

---

## 3. Main Result: Responsibilities as Gradients

### 3.1 Setup and Assumptions

* Distances / energies ( d_j(x) )
* Unnormalized likelihoods ( \exp(-d_j) )
* Objective:
  [
  L(x) = \log \sum_j \exp(-d_j(x))
  ]

---

### 3.2 Core Derivation

* Compute gradient:
  [
  \frac{\partial L}{\partial d_j} = - \frac{\exp(-d_j)}{\sum_k \exp(-d_k)}
  ]
* Define responsibility ( r_j )
* Highlight the identity:

  > **Responsibilities are gradients**

This is the **formal core** of the paper.

---

### 3.3 Interpretation

* Responsibilities are not auxiliary variables
* No E-step is required
* Assignment is intrinsic to optimization

---

## 4. Implicit EM Dynamics

### 4.1 Gradient Descent as Continuous EM

* Compare:

  * classical alternating EM
  * continuous gradient descent
* Show correspondence:

  * forward pass ↔ responsibility computation
  * backward pass ↔ M-step updates

---

### 4.2 What “Implicit” Means (and Does Not Mean)

* Not an approximation
* Not heuristic
* Not architecture-specific
* EM behavior is **forced by the objective**

---

## 5. Special Cases and Unification

### 5.1 Unsupervised Mixture Learning

* Recover standard GMM intuition
* Responsibilities gate prototype learning

---

### 5.2 Cross-Entropy Classification

* Cross-entropy as constrained log-sum-exp
* Labels clamp assignments
* EM dynamics persist under supervision

---

### 5.3 Attention Mechanisms

* Scores as energies
* Softmax as responsibility normalization
* Value projection matrices as learned prototype structure
* EM dynamics apply **across training**, not within a single forward pass

This section explicitly resolves the “values vs prototypes” issue.

---

### 5.4 Relation to Energy-Based and Metric Learning Models

* Position correntropy, contrastive loss, etc.
* Clarify which objectives induce assignment and which do not

---

## 6. What This Unifies

### 6.1 Optimization and Inference

* Inference is not separate from learning
* Assignment is gradient flow

---

### 6.2 EM, Attention, and Cross-Entropy

* Previously siloed frameworks
* Same objective geometry
* Different constraints

---

### 6.3 Geometry Before Probability

* Distances are primary
* Probabilities are derived
* Bayesian behavior is induced, not assumed

---

## 7. Limits and Failure Modes

### 7.1 When Implicit EM Does Not Arise

* Lack of competition
* No normalization
* Independent outputs

---

### 7.2 Scale, Collapse, and Robustness

* Vanishing gradients
* Metric degeneracy
* Tradeoffs with robust objectives

---

### 7.3 Supervision and Closed-World Effects

* Forced assignment
* OOD limitations

---

## 8. Relation to Prior Work

### 8.1 Relation to Oursland (2024)

* Representation geometry vs learning dynamics
* Distance semantics vs assignment dynamics

---

### 8.2 Relation to Aggarwal et al. (2025a,b)

* Empirical Bayesian geometry vs objective necessity
* Mechanistic observation vs causal derivation

---

## 9. Discussion and Open Questions

* Objective design
* Volume control
* Partial supervision
* Open-set inference
* Diagnostic tools for implicit EM

---

## 10. Conclusion

* Restate core result succinctly
* Emphasize explanatory power
* Reiterate what is *not* claimed
* Close with unification perspective

---

## Optional Appendices

* A. Toy Example
* B. Objective Taxonomy
* C. Detailed Gradient Derivations
* D. Terminology Reference

---

### Final meta-comment

This outline does three important things:

1. **Puts the proof early and central**
2. **Keeps prior work clearly separated**
3. **Avoids architecture-specific rabbit holes**

It reads like a theory paper, not a blog post — which is exactly right for arXiv and beyond.

If you want, next I can:

* tighten this into a *page-budgeted* outline (e.g. 8–10 pages)
* help you decide what goes in appendices
* or draft the Introduction section to set tone and expectations
