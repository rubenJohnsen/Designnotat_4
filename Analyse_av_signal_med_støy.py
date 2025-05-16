import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/mnt/data/Analyse_av_signal_med_støy.csv', comment='#')

tid = 'Time (s)'
ch1 = 'Channel 1 (V)'
ch2 = 'Channel 2 (V)'

c2_rms = 0.60638  # V
c2_freq = 4.5006  # kHz
c1_freq = 2.2501  # kHz

plt.figure(figsize=(10, 6))
plt.plot(df[tid]*1e3, df[ch1], label='Channel 1', color='blue', linewidth=1)
plt.plot(df[tid]*1e3, df[ch2], label='Channel 2', color='orange', linewidth=1)

plt.legend(loc='upper right')

textstr = '\n'.join((
    'Målinger:',
    f'C2 AC RMS: {c2_rms:.5f} V',
    f'C2 Frekvens: {c2_freq:.4f} kHz',
    f'C1 Frekvens: {c1_freq:.4f} kHz',
))
props = dict(boxstyle='round', facecolor='white', alpha=0.8)
plt.text(0.02, 0.95, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=props)

plt.title('Tidsdomenevisning av utgangssignal og støy')
plt.xlabel('Tid (ms)')
plt.ylabel('Spenning (V)')
plt.xlim(df[tid].min()*1e3, df[tid].max()*1e3)
plt.grid(True)

plt.tight_layout()
plt.show()
