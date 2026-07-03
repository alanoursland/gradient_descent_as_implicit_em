# Toy Example: Implicit EM in the Smallest Possible Setting

## Purpose of This Document

This note provides a **minimal worked example** demonstrating how implicit EM dynamics arise from a distance-based log-sum-exp objective.

The goal is not realism or performance, but clarity:
- no architecture details
- no datasets
- no asymptotics
- just distances, exponentiation, normalization, and gradients

This example can be kept internal or lightly adapted for exposition later.

---

## Setup

Consider a single data point \( x \) and **two prototypes**, indexed by \( j \in \{1,2\} \).

Assume distances:
\[
d_1(x), \quad d_2(x)
\]

These distances may be produced by a standard neural network, but their origin is irrelevant.

Define unnormalized likelihoods:
\[
P_1 = \exp(-d_1), \quad P_2 = \exp(-d_2)
\]

---

## Objective

We use the unsupervised log-sum-exp objective:
\[
L(x) = \log \left( \exp(-d_1) + \exp(-d_2) \right)
\]

This corresponds to the marginal likelihood that the data point came from *either* prototype.

---

## Responsibilities

Define responsibilities:
\[
r_1 = \frac{\exp(-d_1)}{\exp(-d_1) + \exp(-d_2)}, \quad
r_2 = \frac{\exp(-d_2)}{\exp(-d_1) + \exp(-d_2)}
\]

These satisfy:
\[
r_1 + r_2 = 1
\]

---

## Gradient Computation

Compute gradients of the loss with respect to distances:

\[
\frac{\partial L}{\partial d_1} = -r_1, \quad
\frac{\partial L}{\partial d_2} = -r_2
\]

This is the central result:
> **Responsibilities are gradients.**

---

## Interpretation of Gradient Descent

Assume distances depend on prototype parameters \( \theta_1, \theta_2 \).

Under gradient descent:
- prototype 1 is updated proportionally to \( r_1 \)
- prototype 2 is updated proportionally to \( r_2 \)

Consequences:
- if \( d_1 \ll d_2 \), then \( r_1 \approx 1 \): prototype 1 learns strongly
- if \( d_1 \gg d_2 \), then \( r_1 \approx 0 \): prototype 1 ignores the sample

Assignment and learning are inseparable.

---

## Numerical Example

Let:
\[
d_1 = 0.5, \quad d_2 = 2.0
\]

Then:
\[
P_1 \approx 0.61, \quad P_2 \approx 0.14
\]

Responsibilities:
\[
r_1 \approx 0.81, \quad r_2 \approx 0.19
\]

Thus:
- prototype 1 receives ~81% of the gradient signal
- prototype 2 receives ~19%

No explicit clustering decision was made.

---

## Comparison to Explicit EM

In classical EM:
- E-step computes \( r_1, r_2 \)
- M-step updates prototypes weighted by responsibilities

Here:
- forward pass computes \( P_1, P_2 \)
- normalization yields \( r_1, r_2 \)
- backpropagation applies responsibility-weighted updates

EM emerges without being implemented.

---

## Extension to More Prototypes

For \( K > 2 \) prototypes:
\[
L(x) = \log \sum_{j=1}^K \exp(-d_j)
\]

All results generalize directly:
- responsibilities normalize across \( K \)
- gradients distribute learning signal
- specialization scales naturally

No additional structure is required.

---

## Relation to Cross-Entropy

If a label forces prototype 1 to be correct:
\[
L = d_1 + \log(\exp(-d_1) + \exp(-d_2))
\]

Then:
\[
\frac{\partial L}{\partial d_1} = 1 - r_1, \quad
\frac{\partial L}{\partial d_2} = -r_2
\]

(Note the signs: these are gradients with respect to *distances*, so they are the negatives of the familiar logit-space gradients \( p_j - \mathbb{1}[j=y] \). A descent step pulls the correct prototype closer with strength \( 1 - r_1 \) and pushes the incorrect one away with strength \( r_2 \). Verified numerically in `experiments/verify_identities.py`.)

Responsibilities remain present but are **constrained by supervision**.

---

## What This Example Demonstrates

This toy example shows:

- assignment arises from normalization
- learning is gated by responsibilities
- EM dynamics require no explicit latent variables
- inference and optimization are the same computation

Everything scales from this example.

---

## Summary

In the smallest nontrivial case:
- two prototypes
- one data point
- log-sum-exp objective

EM-like behavior is unavoidable.

This example grounds the abstract claims of the paper in a concrete computation.
