# Assumptions from Prior Work

## Purpose of This Document

This note enumerates the assumptions imported from prior work—specifically:

> **Oursland (2024): Interpreting Neural Networks through Mahalanobis Distance**

These assumptions are treated as **established results**, not hypotheses or modeling choices.
They define the geometric substrate on which the current work analyzes learning dynamics.

The present paper does *not* re-derive these results.

---

## Foundational Assumption: Neural Networks Compute Mahalanobis Distances

We assume the following as established:

* Linear layers with Abs (or shifted ReLU) activations approximate **Mahalanobis distance computations**.
* Individual neurons model **one-dimensional Gaussians along principal component directions**.
* Learned weights define a **basis for whitening** the data, effectively standardizing variance along principal axes.
* Neural layers collectively approximate a **Gaussian Mixture Model (GMM)** subset.

This interpretation relies on the mathematical equivalence between the Mahalanobis distance equation and the operation of a linear layer, rather than on geometric analogies to polytopes.

---

## Logits Are Distances (The "Distance Metric Model")

From the prior work, we adopt the distinction between "Intensity Metrics" and "Distance Metrics":

* **Standard View:** Activation intensity = Confidence (Intensity Metric Model).
* **Our Assumption:** Activation magnitude = **Distance from a prototype mean** (Distance Metric Model).
* **Logits:** Treated as negative distances or energies.
* **Reference State:** Zero activation corresponds to the cluster center (perfect match), not absence of signal.

Thus, the current work analyzes optimization on a substrate where **minimizing output magnitude minimizes distance to a mean**.

---

## Normalization and Whitening

Normalization mechanisms (e.g., BatchNorm) are interpreted geometrically:

* They approximate the **whitening transformation** required for Mahalanobis distance.
* They utilize the variance eigenvalues () to scale the principal component basis.
* They do not alter the fundamental interpretation of the layer as a distance estimator.

---

## Distance-Based Geometry Is Structural

The distance-based interpretation is not an optional modeling choice; it is a structural property of:

* Standard linear layers (via the Abs/ReLU equivalence).
* Standard activation functions (which capture deviation from the mean).

Therefore, the current work does not assume a special architecture. It analyzes the **learning dynamics of standard models** which are *already* computing Mahalanobis distances.

---

## What Is *Not* Assumed

While we assume the *representation* approximates Gaussian components, we explicitly do **not** assume:

* **Explicit Mixture Models:** That the model contains explicit latent variable nodes (we show these arise implicitly).
* **Explicit EM Algorithm:** That the training loop contains an E-step (we show this arises from backprop).
* **Polyhedral/Tropical Geometry:** That boundaries are formed by intersection of half-spaces (we rely on the smooth Gaussian/Mahalanobis view).

---

## Role of These Assumptions in the Current Work

These assumptions allow the current work to:

* Take "outputs = distances" as a given starting point.
* Focus exclusively on how **log-sum-exp objectives** manipulate these distances.
* Derive that optimizing these distances via gradient descent leads to **implicit inference**.

The current work begins **after** the geometric representation (Mahalanobis distance) has been established.

---

## Boundary of Responsibility

Any claims about:

* Why linear layers equate to Mahalanobis distance
* How ReLU approximates Abs
* How weights relate to principal components

belong to prior work and are cited.

The present work is responsible only for:

* Analyzing the **gradient dynamics** of objectives defined over these distances.
* Deriving the **responsibility-weighted update rule**.

---

## Summary

The current paper assumes, based on prior work, that:

* **Neural layers compute Mahalanobis distances.**
* **Outputs are deviations from prototype means.**
* **Geometry is Gaussian-based.**

These are treated as **facts**.

The contribution of the current work is to show how **objectives turn this specific geometry into implicit EM inference**.