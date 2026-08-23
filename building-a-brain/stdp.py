import numpy as np
import matplotlib.pyplot as plt

# Parâmetros biológicos típicos
A_plus = 1.0       # Amplitude máxima de fortalecimento
A_minus = 1.0      # Amplitude máxima de enfraquecimento
tau_plus = 20.0    # Constante de tempo para LTP (ms)
tau_minus = 20.0   # Constante de tempo para LTD (ms)

# Gerar intervalos de tempo de -80ms a +80ms
dt_neg = np.linspace(-80, -0.1, 400)
dt_pos = np.linspace(0.1, 80, 400)

# Aplicação da função por partes
dW_neg = -A_minus * np.exp(dt_neg / tau_minus)
dW_pos = A_plus * np.exp(-dt_pos / tau_plus)

# Plotagem do gráfico
plt.figure(figsize=(10, 6))
plt.plot(dt_pos, dW_pos, 'b-', label='Potenciação (LTP): Pré antes do Pós', linewidth=2.5)
plt.plot(dt_neg, dW_neg, 'r-', label='Depressão (LTD): Pós antes do Pré', linewidth=2.5)

# Linhas de referência
plt.axhline(0, color='black', linestyle='--', alpha=0.5)
plt.axvline(0, color='black', linestyle='--', alpha=0.5)

# Customização técnica do gráfico
plt.title('Regra de Hebb Temporal: Janela de Aprendizado STDP', fontsize=14, fontweight='bold')
plt.xlabel('$\Delta t = t_{pós} - t_{pré}$ (milissegundos)', fontsize=12)
plt.ylabel('Alteração do Peso Sináptico ($\Delta W$)', fontsize=12)
plt.grid(True, which='both', linestyle=':', alpha=0.6)
plt.legend(fontsize=11)

# Destacar a assimetria e causalidade
plt.text(30, 0.5, 'Causalidade\n(Fortalece)', color='blue', fontsize=10, weight='bold', ha='center')
plt.text(-30, -0.5, 'Anti-causalidade\n(Enfraquece)', color='red', fontsize=10, weight='bold', ha='center')

plt.show()