import numpy as np
import time
import matplotlib.pyplot as plt
from math import pi

# Fungsi untuk integrasi Simpson 1/3
def simpsons_rule_revised(f, a, b, N):
    if N % 2 == 1:  # N harus genap untuk Simpson's 1/3 Rule
        raise ValueError("N harus genap untuk Simpson's 1/3 Rule.")
    
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = f(x)
    
    S = y[0] + y[-1]
    for i in range(1, N, 2):
        S += 4 * y[i]
    for i in range(2, N, 2):
        S += 2 * y[i]
    
    integral = (h / 3) * S
    return integral

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Fungsi untuk menghitung galat RMS
def calculate_rms_error(approx_pi, true_pi=pi):
    return np.sqrt(np.mean((approx_pi - true_pi) ** 2))

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Referensi nilai pi
true_pi = 3.14159265358979323846

# Penyimpanan hasil
results = []

# Testing untuk berbagai nilai N
for N in N_values:
    start_time = time.time()
    approx_pi = simpsons_rule_revised(f, 0, 1, N)
    end_time = time.time()
    rms_error = calculate_rms_error(approx_pi, true_pi)
    execution_time = end_time - start_time
    
    results.append((N, approx_pi, rms_error, execution_time))
    print(f"N = {N}")
    print(f"Approximate Pi = {approx_pi}")
    print(f"RMS Error = {rms_error}")
    print(f"Execution Time = {execution_time:.6f} seconds\n")

# Plotting hasil
N_values = [result[0] for result in results]
estimated_pis = [result[1] for result in results]
errors = [result[2] for result in results]
exec_times = [result[3] for result in results]

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(N_values, estimated_pis, 'o-', label='Estimated π')
plt.axhline(y=3.14159265358979323846, color='r', linestyle='--', label='Reference π')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Estimated π')
plt.legend()
plt.title('Estimated π vs N')

plt.subplot(1, 3, 2)
plt.plot(N_values, errors, 'o-', label='RMS Error')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('RMS Error')
plt.legend()
plt.title('RMS Error vs N')

plt.subplot(1, 3, 3)
plt.plot(N_values, exec_times, 'o-', label='Execution Time (s)')
plt.xscale('log')
plt.xlabel('N')
plt.ylabel('Execution Time (s)')
plt.legend()
plt.title('Execution Time vs N')

plt.tight_layout()
plt.show()
