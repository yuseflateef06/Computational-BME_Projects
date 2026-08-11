# Physics-Informed Neural Networks (PINNs) for SIRHD Epidemic Modeling

This repository implements a **Physics-Informed Neural Network (PINN)** in PyTorch to solve inverse problems in epidemiological modeling. Using sparse, noisy observations of only a subset of population compartments ($I$, $H$, and $D$), the model recovers unobserved compartments ($S$ and $R$) while simultaneously estimating the true underlying kinetic parameters ($\beta, \gamma, \rho, \mu, \alpha, \nu$) governing the system dynamics.

## Mathematical Model

The normalized **SIRHD** compartmental model governs the time-evolution of five population fractions:

* $s$ — Susceptible
* $i$ — Infected
* $r$ — Recovered
* $h$ — Hospitalized
* $d$ — Dead

The dynamics are modeled by the following system of non-linear ODEs:

$$\frac{ds}{dt} = -\beta N s i + \alpha r$$

$$\frac{di}{dt} = \beta N s i - (\gamma + \rho) i$$

$$\frac{dr}{dt} = \gamma i + \nu h - \alpha r$$

$$\frac{dh}{dt} = \rho i - (\nu + \mu) h$$

$$\frac{dd}{dt} = \mu h$$

where $N$ is the total population size ($N = 1000$).

## Key Features

* **Softmax Hard-Constraint Enforcer**: State outputs are passed through a `softmax` activation layer to guarantee non-negativity and strictly enforce $\sum_{k} y_k = 1$ ($s + i + r + h + d = 1$) by construction.
* **Bounded Parameter Learning**: Six raw parameter tensors are mapped via sigmoid functions into known physical bounds (`PARAM_BOUNDS`) to prevent unphysical negative values[cite: 14].
* **Latin Hypercube Sampling (LHS)**: Collocation points for physics loss evaluation are uniformly sampled across time using 1D Latin Hypercube Sampling[cite: 14].
* **Multi-Term Loss Function**: Optimizes data loss (MSE on observed $I, H, D$), physics loss (ODE residuals via PyTorch autograd), initial condition loss, and mass conservation loss[cite: 14].
* **Multi-Method Numerical Validation**: Compares PINN trajectory predictions against both SciPy's adaptive ODE solver (`solve_ivp` RK45) and a custom Runge-Kutta 4th Order (RK4) integrator[cite: 14].

## Requirements

Install the required Python packages before running the notebook[cite: 14]:

```bash
pip install torch numpy scipy matplotlib
