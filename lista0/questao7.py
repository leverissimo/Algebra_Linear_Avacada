import numpy as np
import time
import matplotlib.pyplot as plt

n_sizes = [16, 32, 64, 128, 256, 512, 1024, 2048]
times = []

for n in n_sizes:
    times_mean = []
    for k in range(100):
        A = np.random.rand(n,n)
        b = np.random.rand(n)

        start = time.time()
        x = np.linalg.solve(A,b)
        end = time.time()
        times_mean.append(end - start)
    times.append(np.mean(times_mean))

log_n = np.log2(n_sizes)
log_times = np.log2(times)

log_n_assintotico = log_n[3:]
log_times_assintotico = log_times[3:]

coeficientes = []

# Calculamos a inclinação entre cada par de pontos consecutivos
for i in range(1, len(log_n_assintotico)):
    delta_y = log_times_assintotico[i] - log_times_assintotico[i-1]
    delta_x = log_n_assintotico[i] - log_n_assintotico[i-1] # Isso aqui será sempre 1!
    
    k_i = delta_y / delta_x
    coeficientes.append(k_i)

# Tiramos a média aritmética simples
media_k = np.mean(coeficientes)

print(f"Média dos coeficientes: {media_k:.3f}")

print("Approximate slope:", log_times[-1] - log_times[-2])

plt.plot(log_n, log_times, marker='o')
plt.xlabel('Log2 of the number of columns')
plt.ylabel('Log2 of the time spent(seconds)')
plt.title('Log-Log\'s graph: Time vs Size of System')
plt.grid(True)
plt.savefig("log_log.png")