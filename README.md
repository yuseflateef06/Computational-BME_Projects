# Biomedical Engineering & Quantitative Modeling Portfolio

This repository aggregates projects at the intersection of medical image processing, computational epidemiology, and quantitative biological modeling. Each project is maintained in its dedicated branch with full source code, scripts, and reproducible workflows.

---

## Branch Overview

| Branch Name | Project Title | Stack / Tools | Core Mathematical Concepts |
| :--- | :--- | :--- | :--- |
| **`Convex-Optimization-&-Image-Denoising`** | Image Denoising via ADMM | MATLAB | Convex Optimization, Total Variation Regularization, Dual Ascent[cite: 7, 8, 10] |
| **`Physics-Informed-Neural-Network-(PINN)-SIRHD-Model`** | Physics-Informed Neural Networks (PINNs) | Python, PyTorch, SciPy | Scientific Machine Learning, Inverse Problems, Automatic Differentiation |
| **`Hopfield-Network-Neural-Memory-Model`** | Classical ODE Integration & Validation | Python, NumPy, SciPy | 4th-Order Runge-Kutta (RK4), Adaptive RK45 Integration[cite: 14] |

---

## Project Summaries

### 1. Total Variation Image Denoising via ADMM (`admm-denoising` branch)

This project implements total variation (TV) image denoising using the **Alternating Direction Method of Multipliers (ADMM)** in MATLAB[cite: 7, 8]. The solver removes high-frequency noise from corrupt grayscale images by balancing target fidelity against neighbor-pixel smoothness[cite: 8, 9, 11].

* **Key Mechanics**:
  * Decouples the convex optimization problem into primal ($y$-update), dual ($d$-update), and multiplier ($\lambda$-update) steps[cite: 7, 9, 10, 11].
  * Evaluates parameter sweeps across regularization parameters $t \in [5, 40]$[cite: 8].
  * Applies proximal operators (`Prox_Absolute_Value`) for L1-norm total variation minimization[cite: 9].
* **Primary Code Files**: `ADMM.m`, `Update_D.m`, `Update_Y.m`, `Update_Lambda.m`[cite: 7, 9, 10, 11].

---

### 2. Physics-Informed Neural Networks for SIRHD Modeling (`pinn-epidemic-model` branch)

This project constructs a **Physics-Informed Neural Network (PINN)** in PyTorch to solve inverse problems for complex compartmental systems ($S, I, R, H, D$)[cite: 14]. Given only sparse, noisy measurements of infected ($I$), hospitalized ($H$), and deceased ($D$) populations, the PINN reconstructs hidden state dynamics ($S, R$) while simultaneously identifying six unknown system parameters ($\beta, \gamma, \rho, \mu, \alpha, \nu$)[cite: 14].

* **Key Mechanics**:
  * Hard-constrained **softmax** activation layer enforces physical total population bounds ($s + i + r + h + d = 1$) by construction[cite: 14].
  * Trainable parameter tensors mapped via sigmoids prevent unphysical parameter ranges[cite: 14].
  * Latin Hypercube Sampling (LHS) generates collocation points to compute ODE residual loss terms via automatic differentiation (`torch.autograd`)[cite: 14].
* **Primary Code Files**: `Final_Project.ipynb`[cite: 14].

---

### 3. Numerical ODE Integration & System Validation (`numerical-ode-solvers` branch)

This project focuses on forward simulation and validation of multi-compartment non-linear differential equation systems using classical numerical initial value problem (IVP) methods[cite: 14].

* **Key Mechanics**:
  * Classical 4th-Order Runge-Kutta (RK4) multi-step integrator implementation[cite: 14].
  * Benchmark comparison against SciPy adaptive-step numerical integrators (`solve_ivp` RK45)[cite: 14].
  * Numerical verification comparing parameter estimates derived from physics-informed deep learning against classical RK4 trajectories[cite: 14].
* **Primary Code Files**: `Final_Project.ipynb` / numerical solvers module[cite: 14].

---

## Accessing Project Branches

To inspect or run code from a specific project, switch to its corresponding branch:

```bash
# Clone the repository
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

# Checkout a specific project branch
git checkout admm-denoising
# or
git checkout pinn-epidemic-model
# or
git checkout numerical-ode-solvers
