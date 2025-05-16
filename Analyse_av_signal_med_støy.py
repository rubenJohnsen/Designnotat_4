import pandas as pd
import matplotlib.pyplot as plt

# Les den korrekte Spek.csv-filen
df = pd.read_csv('/mnt/data/Spek.csv', comment='#')

# Kolonnenavn
time_col = 'Time (s)'
ch1_col  = 'Channel 1 (V)'
ch2_col  = 'Channel 2 (V)'

# Oppdaterte måleverdier
c1_freq = 2.2500    # kHz
c2_freq = 4.5003    # kHz
c2_rms  = 0.58134   # V

# Plot med byttede farger: C1 i oransje, C2 i blått
plt.figure(figsize=(10,6))
plt.plot(df[time_col]*1e3, df[ch1_col], label='Channel 1', color='orange', linewidth=1)
plt.plot(df[time_col]*1e3, df[ch2_col], label='Channel 2', color='blue', linewidth=1)

# Legend
plt.legend(loc='upper right')

# Tekstboks med målinger
txt = (f"Målinger:\n"
       f"C2 AC RMS: {c2_rms:.5f} V\n"
       f"C2 Frekvens: {c2_freq:.4f} kHz\n"
       f"C1 Frekvens: {c1_freq:.4f} kHz")
props = dict(boxstyle='round', facecolor='white', alpha=0.8)
plt.text(0.02, 0.95, txt, transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', bbox=props)

# Akseoppsett
plt.title('Tidsdomenevisning av utgangssignal og støy')
plt.xlabel('Tid (ms)')
plt.ylabel('Spenning (V)')
plt.grid(True)
plt.tight_layout()
plt.show()
