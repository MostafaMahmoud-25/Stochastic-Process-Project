# Stochastic Processes — Course Projects (Fall 2026)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)

**Faculty of Computer and Data Science (FCDS) — Alexandria University**  
Two independent Python implementations exploring **Markov Chains**, **Hidden Markov Models (HMMs)**, and **Baum-Welch Parameter Learning**.

---

## Repository Structure

```text
├── Project_1/                  # HMM Application: Student Academic / Focus State
│   ├── r1_r2_model.py          # Model definition, P matrix verification & diagram
│   ├── state_transition_diagram.png
│   └── ...                     # R3–R8 scripts & final report
│
├── Project_2/                  # Learning HMM Parameters with Baum-Welch
│   └── ...                     # Dataset, Forward-Backward, Baum-Welch & report
│
└── README.md
```

---

## Project 1: Student Academic / Focus State (HMM)
Models a student's unobservable weekly study state (**Focused**, **Distracted**, **Burned Out**) using observable weekly academic outputs (**High Score**, **Average Score**, **Low / Missed**).

* **R1 & R2:** Problem formulation, Markov property justification, transition matrix $P$, and state-transition diagram.
* **R3 & R4:** $n$-step transition behavior ($\pi \cdot P^n$) and steady-state distribution ($\pi = \pi P$).
* **R5:** Absorption analysis (canonical form, fundamental matrix $N$, absorption probabilities $B$, and expected steps to burnout $t$).
* **R6 – R8:** Emission matrix $E$, initial distribution $\pi$, **Forward** evaluation, and **Viterbi** decoding.

---

## Project 2: Learning HMM Parameters (Baum-Welch)
Estimates HMM parameters $(P, E, \pi)$ purely from unlabeled observation sequences using a from-scratch Python implementation of the **Baum-Welch (EM) algorithm**.

* **R1 – R3:** Dataset preprocessing, discretization, model design, and parameter initialization.
* **R4 – R5:** Forward-Backward ($\alpha, \beta$), $\gamma$ and $\xi$ calculations, re-estimation loop, and log-likelihood convergence plots.
* **R6 – R8:** Multi-initialization comparison (local maxima analysis), `hmmlearn` benchmark comparison, and Viterbi decoding.

---

## Quick Start

```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)<your-username>/<repo-name>.git
cd <repo-name>

# Install dependencies
pip install numpy matplotlib
```

---

## Team Roles

### Project 1 (Students 1–5)
| Role | Requirements | Responsibilities |
| :--- | :--- | :--- |
| **Student 1** | R1 + R2 | Problem & model definition, Markov justification, transition matrix $P$, and state-transition diagram |
| **Student 2** | R3 + R4 | $n$-step behavior ($\pi \cdot P^n$) and steady-state distribution ($\pi = \pi P$) |
| **Student 3** | R5 | Absorption analysis (canonical form, $N$, $B$, $t$) |
| **Student 4** | R6 + R7 | HMM parameters ($E$, $\pi$) and Forward algorithm |
| **Student 5** | R8 + Integration | Viterbi algorithm, code integration, and final report |

### Project 2 (Students 6–10)
| Role | Requirements | Responsibilities |
| :--- | :--- | :--- |
| **Student 6** | R1 + R2 | Dataset selection, preprocessing/discretization, and model design ($N$) |
| **Student 7** | R3 + R4 (Part 1) | Initialization ($P, E, \pi$) and scaled Forward-Backward ($\alpha, \beta$) |
| **Student 8** | R4 (Part 2) | $\gamma$, $\xi$, re-estimation formulas, and full Baum-Welch loop |
| **Student 9** | R5 + R7 | Convergence plots, multi-initialization comparison, and `hmmlearn` benchmark |
| **Student 10** | R6 + R8 + Integration | Final parameter interpretation, Viterbi/evaluation, code integration, and final report |
