# Prior Work: Oursland (2024) — Mahalanobis Distance Interpretation

## Purpose of This Document

This note clarifies how the current work (*implicit EM via gradients*) relates to the 2024 paper:

> **Interpreting Neural Networks through Mahalanobis Distance** (Oursland, 2024)

The goal is to:

* establish continuity of ideas
* distinguish scope and contribution
* avoid overlap or redundancy
* make clear what is *new* in the current work

The two papers are complementary, not competing.

---

## Summary of the 2024 Paper

The 2024 paper establishes a **representational interpretation** of neural network layers.

Core claims:

* Linear layers with Abs (or shifted ReLU) activations approximate **Mahalanobis distance computations** along principal component directions.
* A neural layer effectively models a subset of principal components from a Gaussian Mixture Model (GMM).
* Neural networks operate on a **"distance metric model"** (smaller activation = closer to prototype) rather than an "intensity metric model" (larger activation = stronger feature presence).

Key contributions:

* Mathematical equivalence between linear nodes and 1D Gaussians.
* Demonstration that Abs and ReLU activations are functionally comparable in capturing deviation from a mean.
* Proposal of distance-based initialization and componentization strategies.

The paper is primarily concerned with **representation semantics** and the **statistical interpretation of single layers**.

---

## What the 2024 Paper Does *Not* Address

The 2024 paper deliberately does *not* address:

* how these distances are converted into probabilistic responsibilities via loss functions
* how learning dynamics arise from minimizing these distances
* why EM-like behavior appears during training (beyond the static GMM analogy)
* how optimization relates to inference mechanisms like the M-step

In other words, it explains **what is represented** (Mahalanobis distances), but not **how the objective function utilizes this geometry for inference**.

---

## Scope of the Current Work

The current paper addresses the **dynamics and objectives** layer.

Core focus:

* distance-based objectives with exponentiation and normalization
* log-sum-exp structure
* gradient flow
* emergence of responsibilities
* equivalence between gradient descent and EM dynamics

Key question answered:

> *Given a distance-based representation (as established in 2024), what learning dynamics necessarily follow from standard objectives?*

---

## Relationship Between the Two Works

The relationship can be summarized as:

| Aspect | Oursland (2024) | Current Work |
| --- | --- | --- |
| Primary question | What do neural representations mean? | What learning dynamics do objectives induce? |
| Focus | Geometry of representations | Geometry of optimization |
| Key object | Mahalanobis Distance / Gaussian PCs | Responsibilities / Assignments |
| Level | Representation semantics | Objective-level dynamics |
| Concern | Interpretation of Units | Mechanism of Learning |

The 2024 paper provides the **geometric substrate** (Linear Layer  Mahalanobis Distance).
The current work explains the **inference dynamics that arise on that substrate** (Gradient Descent  Implicit EM).

---

## Conceptual Continuity

The current work assumes (but does not re-derive) the following from the 2024 paper:

* **Outputs are Distances:** Neural outputs should be interpreted as distances/energies relative to a prototype mean, not as arbitrary confidence scores.
* **Geometry Precedes Probability:** The "distance metric model" is the primary physical state of the network; probabilities are derived quantities.
* **Gaussian Connection:** The link between linear layers and Gaussian components provides the justification for treating prototypes as "mixture components."

These assumptions are foundational but not restated.

---

## What Is New in the Current Work

The novel contributions relative to the 2024 paper are:

1. **Responsibilities-as-Gradients**
* We show that if the representation is distance-based (2024), then the gradient of a log-sum-exp objective is the *posterior responsibility*.
* No auxiliary variables or E-step required.


2. **Implicit EM**
* Gradient descent implements EM-like learning dynamics automatically.
* The "GMM" interpretation from 2024 is shown to be an *active dynamic* of training, not just a static property of the weights.


3. **Objective-Level Explanation**
* Applies the distance interpretation to Attention and Cross-Entropy, unifiying them.



These results depend on the Mahalanobis distance representations established in 2024 but go beyond static interpretation to explain learning.

---

## Why This Is Not Redundant

The two papers answer **orthogonal questions**:

* The 2024 paper establishes *that* networks compute distances.
* The current paper establishes *why* optimizing those distances leads to Bayesian/EM behavior.

Neither subsumes the other.

Together, they form a coherent two-stage theory:

1. **Static:** Neural networks learn Mahalanobis-based geometry (Oursland, 2024).
2. **Dynamic:** Distance-based objectives turn that geometry into inference via gradients (Current Work).

---

## Recommended Positioning Language

If referencing the relationship explicitly:

> *Our prior work (Oursland, 2024) establishes that neural linear layers can be interpreted as computing Mahalanobis distances to latent means. The present work builds on this foundation by analyzing the learning dynamics induced by such distance-based representations, showing that EM-style responsibilities arise directly as gradients.*

This framing:

* acknowledges dependency
* avoids repetition
* clearly separates contributions

---

## Summary

* Oursland (2024): representation-level geometry (Mahalanobis/Gaussian)
* Current work: objective-level dynamics (Implicit EM)
* Shared foundation: Distance Metric Model
* Distinct contributions: meaning vs mechanism

The current paper should be read as a **direct continuation**, not a revision, of the 2024 work.