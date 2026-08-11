# Image Denoising via ADMM (Convex Optimization)

This repository implements total variation image denoising using the **Alternating Direction Method of Multipliers (ADMM)** in MATLAB[cite: 7, 8]. The algorithm minimizes image noise by balancing fidelity to the noisy target image against spatial smoothness across neighbor pixel differences[cite: 8, 9, 11].

## Repository Structure

* `ADMM.m` — Main ADMM solver that coordinates iterative primal and dual variable updates until convergence (` Frobenius norm <= 1e-2 `)[cite: 7].
* `Update_D.m` — Updates spatial gradient dual variables $d_{\text{down}}$ and $d_{\text{right}}$ using proximal operators (`Prox_Absolute_Value`)[cite: 9].
* `Update_Y.m` — Updates the primal variable $y$ (denoised image) through local 4-neighbor spatial relaxation iterations[cite: 11].
* `Update_Lambda.m` — Updates the Lagrange multipliers $\lambda_{\text{down}}$ and $\lambda_{\text{right}}$[cite: 10].
* `ima-noisy.pgm` — Source noisy image file.

## Mathematical Overview

The ADMM solver splits the convex image denoising problem into tractable sub-problems[cite: 7, 9, 11]:

1. **$d$-Update**: Evaluates proximal updates on horizontal and vertical intensity differences[cite: 9].
2. **$y$-Update**: Solves for image intensities by combining neighbor values, multipliers, and the noisy input $x$ scaled by hyperparameter $t$[cite: 11]:
   $$\text{tmp} = \frac{t \cdot x_{i,j} + \sum y_{\text{neighbors}} + \Delta \lambda + \Delta d}{t + N_{\text{neighbors}}}$$
3. **$\lambda$-Update**: Dual ascent step accumulating difference residuals[cite: 10].

## Requirements

* MATLAB R2018b or later (requires standard Image Processing Toolbox for `.pgm` reading/writing).

## Usage

1. Place `ima-noisy.pgm` in the working folder.
2. Run the driver script to sweep regularization values $t \in [5, 40]$ in step sizes of 5:

```matlab
% Run optimization across t parameters
main
