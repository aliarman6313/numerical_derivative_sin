# Numerical Derivatives of sin(x)

This Python project computes the numerical derivative of the sine function \( \sin(x) \) over the interval \([0, 2\pi]\) using three finite difference methods:

- Forward difference  
- Central difference  
- Backward difference  

It then compares the numerical results with the analytical derivative \( \cos(x) \), and visualizes the differences using matplotlib.

## 📁 Files

- numerical_derivative_sin.py: The main Python script performing the computations and plotting.
- requirements.txt: Python packages needed to run the script.
- README.md: This file.

## 📊 Methods

Let \( f(x) = \sin(x) \), and step size \( \Delta x = 0.01 \):

- Forward difference:
  \[
  f'(x) \approx \frac{f(x + \Delta x) - f(x)}{\Delta x}
  \]

- Backward difference:
  \[
  f'(x) \approx \frac{f(x) - f(x - \Delta x)}{\Delta x}
  \]

- Central difference:
  \[
  f'(x) \approx \frac{f(x + \Delta x) - f(x - \Delta x)}{2\Delta x}
  \]

The output compares these three numerical approximations with the exact derivative \( \cos(x) \).

## ▶️ How to Run

1. Clone the repo:
   `bash
   git clone https://github.com/YOUR_USERNAME/numerical-derivatives.git
   cd numerical-derivatives
