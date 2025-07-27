import numpy as np
import matplotlib.pyplot as plt

# تنظیمات اولیه
dx = 0.01
x = np.arange(0, 2*np.pi, dx)
y = np.sin(x)

# مشتق‌گیری عددی
forward = (np.roll(y, -1) - y) / dx
central = (np.roll(y, -1) - np.roll(y, 1)) / (2*dx)
backward = (y - np.roll(y, 1)) / dx
analytical = np.cos(x)

# اصلاح ایندکس آخر در forward (زیرا wrap-around داریم)
forward[-1] = np.nan
central[0], central[-1] = np.nan, np.nan
backward[0] = np.nan

# رسم نمودارها
plt.figure(figsize=(10,6))
plt.plot(x, analytical, 'k-', label='Analytical d/dx(sin(x)) = cos(x)')
plt.plot(x, forward, 'r--', label='Forward difference')
plt.plot(x, central, 'g-.', label='Central difference')
plt.plot(x, backward, 'b:', label='Backward difference')
plt.xlabel('x')
plt.ylabel('Derivative')
plt.title('Numerical vs Analytical Derivative of sin(x)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()