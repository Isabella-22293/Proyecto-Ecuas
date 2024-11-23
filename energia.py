import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del circuito RLC
R = 10       # Resistencia (ohmios)
L = 0.1      # Inductancia (henrios)
C = 0.001    # Capacitancia (faradios)
V0 = 5       # Voltaje máximo (voltios)
omega = 100  # Frecuencia angular (rad/s)

# Ecuaciones diferenciales
def rlc_system(t, y):
    q, i = y
    dqdt = i
    didt = (V0 * np.sin(omega * t) - R * i - q / C) / L
    return [dqdt, didt]

# Condiciones iniciales
y0 = [0, 0]  # Carga inicial (q=0) y corriente inicial (i=0)

# Tiempo de simulación
t_span = (0, 0.1)  # Simular de 0 a 0.1 segundos
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # 1000 puntos de evaluación

# Resolver el sistema
sol = solve_ivp(rlc_system, t_span, y0, t_eval=t_eval)

# Extraer resultados
t = sol.t  # Tiempo
q = sol.y[0]  # Carga
i = sol.y[1]  # Corriente

# Cálculo de energías
E_C = 0.5 * (q**2) / C  # Energía en el condensador
E_L = 0.5 * L * (i**2)  # Energía en el inductor
P_R = R * (i**2)        # Pérdida de energía en la resistencia
E_total = E_C + E_L     # Energía total

# Gráfica de energías
plt.figure(figsize=(10, 6))
plt.plot(t, E_C, label="Energía en el condensador $E_C$", color="blue")
plt.plot(t, E_L, label="Energía en el inductor $E_L$", color="green")
plt.plot(t, E_total, label="Energía total $E_{total}$", color="red", linestyle="--")
plt.title("Energía en el circuito RLC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Energía (J)")
plt.grid()
plt.legend()
plt.show()
