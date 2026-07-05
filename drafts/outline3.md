# Gradient Descent as Implicit EM in Distance-Based Neural Models

## Merged Outline

Target: 8-10 pages + appendices

---

### Abstract (0.25 pages)

- Observation: Neural networks exhibit Bayesian, mixture-model, EM-like behavior
- Problem: Current explanations are analogies, not derivations
- Contribution: For distance-based LSE objectives, ∂L/∂d_j = -r_j (identity, not approximation)
- Consequence: Gradient descent *is* implicit EM—no auxiliary variables required
- Unification: GMMs, attention, cross-entropy are three regimes of one mechanism

---

### 1. Introduction (1.25 pages)

#### 1.1 The Puzzle
- Neural networks repeatedly exhibit: soft clustering, prototype specialization, Bayesian uncertainty tracking
- These appear across architectures—attention, classification heads, energy-based models
- Standard explanations: emergent properties, architectural coincidences, loose analogies

#### 1.2 Recent Evidence
- Agarwal et al. (2025a,b): transformers implement exact Bayesian inference in controlled settings
- Gradient dynamics show EM-like two-timescale structure
- But: characterized as "structural analogy," not derived from objectives

#### 1.3 This Paper
- We close the gap: derive EM dynamics as necessary consequence of objective geometry
- Core result: **Responsibilities are gradients**
- Inference is not added to optimization—it *is* optimization

#### 1.4 Contributions
- One theorem: ∂L/∂d_j = -r_j
- One interpretation: gradient descent performs implicit EM
- One unification: three regimes (unsupervised, conditional, constrained) of the same mechanism

---

### 2. The Geometric Substrate (1 page)

#### 2.1 Distance-Based Representations
- Import from Oursland (2024): standard networks compute distances/energies
- Outputs as deviations from learned prototypes, not confidences
- This is structural to ReLU networks, not a modeling choice

#### 2.2 The Log-Sum-Exp Objective
- General form: $L = \log \sum_j \exp(-d_j)$
- Notation and setup for derivation
- Brief: cross-entropy and attention softmax as instances

#### 2.3 Classical EM (Reference Point)
- E-step: compute responsibilities
- M-step: update parameters weighted by responsibilities
- Discrete and alternating—what we will show collapses into gradient descent

---

### 3. Main Result: Responsibilities Are Gradients (1.5 pages)

#### 3.1 Derivation
- Setup: distances $d_j(x)$, unnormalized likelihoods $\exp(-d_j)$
- Objective: $L = \log \sum_j \exp(-d_j)$
- Compute gradient (full steps shown):

$$\frac{\partial L}{\partial d_j} = -\frac{\exp(-d_j)}{\sum_k \exp(-d_k)} = -r_j$$

- **Theorem:** The gradient with respect to distance is the negative responsibility

#### 3.2 What This Means
- Responsibilities are not auxiliary variables—they are gradients
- No E-step is required; forward pass computes responsibilities implicitly
- Parameter updates are automatically responsibility-weighted (M-step)
- EM is not approximated—it is *performed* by gradient descent

#### 3.3 Conditions
- Requires exponentiation (converts distance to likelihood)
- Requires normalization (induces competition)
- Requires gradient-based optimization
- When these hold, implicit EM is unavoidable

---

### 4. Three Regimes of Implicit Inference (2.5 pages)

The same mechanism manifests differently under different constraints:

#### 4.1 Unsupervised Regime: Mixture Learning
- Pure log-sum-exp objective
- Full competition between prototypes
- Responsibilities are entirely latent
- Dynamics: spontaneous clustering and specialization
- Connection to classical GMM/EM

#### 4.2 Conditional Regime: Attention Mechanisms
- Scores as negative distances
- Softmax as responsibility normalization
- Attention weights *are* responsibilities

**Key clarification:** Prototypes are not value vectors
- $v_j = W_V x_j$ is input-derived (transient)
- $W_V$ is the learned prototype structure (persistent)
- Responsibility-weighted gradients flow to $W_V$ via chain rule
- EM dynamics apply across training, not within a forward pass

Attention as conditional mixture inference:
- Query defines context
- Keys define candidate components
- Values index into learned prototype family
- Per-query mixture, shared parameters

#### 4.3 Constrained Regime: Cross-Entropy Classification
- Objective: $L = d_y + \log \sum_k \exp(-d_k)$
- Gradient structure:

$$\frac{\partial L}{\partial d_j} = r_j - \mathbb{1}[j = y]$$

- Label clamps correct-class responsibility to 1
- Competition persists among incorrect classes
- EM dynamics are *directed*, not eliminated
- Explains why cross-entropy "just works"

#### 4.4 The Taxonomy
- Key insight: **normalization is the toggle**
- With normalization → competition → responsibilities → implicit EM
- Without normalization → independence → robustness, no assignment (e.g., correntropy)
- Exponentiation without normalization trades inference for outlier resistance

---

### 5. Relation to Prior Work (1 page)

#### 5.1 Oursland (2024)
- Establishes: representations are distances
- We establish: objectives turn distances into inference
- Relationship: geometric substrate → learning dynamics

#### 5.2 Agarwal et al. (2025a,b)
- They show: transformers implement exact Bayesian inference (empirical)
- They show: gradient dynamics are EM-like (mechanistic)
- They call it: "structural rather than variational"
- We show: it's an algebraic identity under the distance interpretation
- Relationship: observation → explanation

#### 5.3 Other Connections
- LeCun et al. (2006): energy-based learning framework
- Dempster et al. (1977): classical EM
- Vaswani et al. (2017): attention mechanism
- Mixture of Experts: explicit gating vs. implicit responsibilities

---

### 6. Limits and Failure Modes (0.75 pages)

#### 6.1 When Implicit EM Does Not Arise
- No normalization → no competition → no responsibilities
- Independent outputs (e.g., sigmoid per class) lack assignment structure

#### 6.2 Scale and Collapse
- Log-determinant (volume) term absent in most neural objectives
- Can cause metric collapse without regularization/normalization
- Framework explains *why* collapse happens, doesn't prevent it

#### 6.3 Supervision Constraints
- Hard labels override latent assignment
- Closed-world assumption: every input must be assigned
- OOD behavior is objective-limited, not mechanism-limited

#### 6.4 What This Framework Does Not Explain
- Generalization, scaling laws
- Long-horizon reasoning, planning
- Emergent capabilities
- One mechanism, clearly bounded

---

### 7. Discussion (0.5 pages)

#### 7.1 Unification
- GMMs, attention, cross-entropy: same mechanism, different constraints
- Geometry precedes probability
- Loss functions are geometric priors

#### 7.2 Implications
- Interpretability: gradients *are* assignments, no probes needed
- Objective design: LSE is structural requirement for inference, not numerical trick
- Theory: optimization and inference are the same process at different scales

#### 7.3 Open Directions
- Learned volume control
- Partial/noisy supervision
- Open-set inference
- Diagnostic tools for implicit EM in trained models

---

### 8. Conclusion (0.25 pages)

- One result: $\frac{\partial L}{\partial d_j} = -r_j$
- One implication: EM is implicit in gradient descent on LSE objectives
- One unification: unsupervised, conditional, and constrained inference share the same mechanism
- Final line: Optimization and inference are the same process viewed at different scales

---

### References (~0.5 pages)

Core:
- Oursland (2024)
- Agarwal et al. (2025a, 2025b)
- LeCun et al. (2006)
- Dempster et al. (1977)
- Vaswani et al. (2017)

Supporting:
- Zhang et al. (2020) — EM vs GD comparison
- Jacobs et al. (1991) — Mixture of Experts

---

### Appendices

#### A. Toy Example (0.5 pages)
- Two prototypes, one data point
- Full numerical walkthrough
- Shows responsibility-weighted updates explicitly

#### B. Objective Taxonomy Table (0.25 pages)
- Competition / Responsibilities / Robustness / EM-like columns
- LSE, Cross-entropy, Correntropy, Metric learning, MSE rows

#### C. Extended Derivations (if needed)
- Chain rule through attention
- Cross-entropy gradient derivation

---

## Page Budget

| Section | Pages |
|---------|-------|
| Abstract | 0.25 |
| 1. Introduction | 1.25 |
| 2. Geometric Substrate | 1.0 |
| 3. Main Result | 1.5 |
| 4. Three Regimes | 2.5 |
| 5. Prior Work | 1.0 |
| 6. Limits | 0.75 |
| 7. Discussion | 0.5 |
| 8. Conclusion | 0.25 |
| References | 0.5 |
| **Main text total** | **~9.5 pages** |
| Appendices | ~1 page |

---

## Key Decisions in This Outline

1. **"Three Regimes" not "Applications"** — frames unification as taxonomy, not laundry list

2. **Agarwal as puzzle-setter, not competitor** — they provide empirical grounding; we provide theoretical explanation

3. **Values vs prototypes resolved explicitly** — in Section 4.2, prevents reviewer confusion

4. **Toy example in appendix** — keeps main text tight, available for skeptics

5. **Limits honest and bounded** — prevents overclaiming, shows maturity

6. **One theorem, one implication, one unification** — repeating triad gives paper rhetorical structure