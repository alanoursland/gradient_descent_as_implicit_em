### **Gradient Descent as Implicit EM in Distance-Based Neural Models**

---

### **Abstract**

* **The Observation:** Neural networks trained with standard objectives often exhibit "Bayesian-like" behavior, forming clusters and estimating uncertainty.
* **The Problem:** Current explanations rely on loose analogies to mixture models or post-hoc architectural justifications.
* **The Contribution:** We derive a rigorous mechanism: for any distance-based log-sum-exp objective, the gradient with respect to distance **is** the posterior responsibility.
* **The Consequence:** Gradient descent inherently performs "Implicit EM"—continuous, responsibility-weighted inference—without auxiliary variables or explicit probabilistic layers.
* **The Unification:** We show this single mechanism unifies Gaussian Mixture Models, Transformer Attention, and Cross-Entropy classification.

---

### **1. Introduction**

* **1.1 The Theoretical Gap:** We have "geometry" (representations) and "optimization" (gradient descent), but we treat "inference" (EM, Bayesian updates) as a separate algorithmic class.
* **1.2 The Core Thesis:** Inference is not an algorithm we add; it is a thermodynamic property of the objective function.
* **1.3 Key Claim:** **Responsibilities are Gradients.** When we optimize geometry with LSE losses, we are performing inference.
* **1.4 Roadmap:**
* Establish the geometric substrate (outputs = distances).
* Derive the gradient-responsibility identity.
* Demonstrate unification of Attention and Classification.



### **2. Preliminaries: The Geometric Substrate**

* *Source Material: `distance_from_prototype.md`, `prior_work_oursland_2024.md*`
* **2.1 From Confidences to Energies:** Standard interpretation vs. the "Distance Interpretation."
* Neural outputs  are negative energies or distances .
* Probabilities are derived quantities, not primitives.


* **2.2 Prototypes, Not Templates:** A "prototype" is a region in the latent metric space, not a specific point.
* **2.3 The Canonical Objective:** Define the standard Log-Sum-Exp (LSE) form: .

### **3. The Mechanism: Implicit EM via Gradients**

* *Source Material: `implicit_em_via_gradients.md`, `toy_example.md*`
* **3.1 Derivation of the Gradient Identity:**
* Step-by-step calculus showing .
* Definition of Responsibility .
* **Theorem 1:** .


* **3.2 The Dynamics of Gradient Descent:**
* Forward Pass  Unnormalized Likelihoods.
* Normalization  Implicit E-Step.
* Backward Pass  Responsibility-Weighted M-Step.


* **3.3 No Auxiliary Variables:** Crucial distinction from classical EM. The architecture *is* the inference engine; there are no separate latent variable parameters.

### **4. Unification: Three Regimes of Implicit Inference**

* *Source Material: `unification_impact.md*`
* **4.1 Unsupervised Regime (GMMs & EBMs):**
* Pure competition between prototypes.
* Dynamics: Spontaneous clustering and specialization based on initialization.


* **4.2 Conditional Regime (Attention Mechanisms):**
* *Source: `relation_to_attention.md*`
* Reinterpretation: Queries define context; Keys are component candidates; Values are prototypes.
* Attention weights are strictly equivalent to responsibilities.
* Gradient flow updates Value vectors based on "assignment."


* **4.3 Constrained Regime (Cross-Entropy Classification):**
* *Source: `relation_to_cross_entropy.md*`
* The "Constrained EM" view: Labels clamp one responsibility to .
* Analysis of the gradient .
* Argument: CE does not break the mechanism; it directs it. Competition still exists among the incorrect classes.



### **5. Limits and Boundary Conditions**

* *Source Material: `limits_and_failure_modes.md`, `open_questions.md*`
* **5.1 The Necessity of Normalization:** Without "competition" (normalization across alternatives), responsibilities do not emerge. Independent sigmoids fail this test.
* **5.2 Volume and Collapse:** Classical EM includes covariance terms () to prevent collapse. Neural networks often lack this, leading to "metric collapse" unless regularized or normalized (BatchNorm/LayerNorm).
* **5.3 Scale Sensitivity:** Distance-based objectives can suffer from vanishing gradients if initialization is poor (the "outlier" problem).

### **6. Discussion: Implications for Deep Learning**

* **6.1 Interpretability:** We don't need probes to find "concepts." The gradients *are* the concept assignments.
* **6.2 Architecture Design:** Suggests that "Log-Sum-Exp" is not just a math trick for stability, but a structural requirement for inference.
* **6.3 The "Physics" of Learning:** Moving from heuristic architectural design to objective-driven geometric design.

### **7. Conclusion**

* **Summary:** We replaced the analogy "NNs are like mixture models" with the identity "Gradients are Responsibilities."
* **Final Thought:** Optimization and Inference are the same process viewed at different scales.

---

### **8. References**

* *(Populated from the `prior_art.md` list, including Oursland 2024, Aggarwal 2025a/b, etc.)*