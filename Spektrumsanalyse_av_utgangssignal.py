import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/mnt/data/RMS_spectrumanalyse.csv', comment='#')

frekvens_kol = 'Frequency (Hz)'
rms_kol = 'Trace 2 (V)'

indeks = df[rms_kol].idxmax()
fund_freq = df.loc[indeks, frekvens_kol]
fund_rms = df.loc[indeks, rms_kol]

plt.figure(figsize=(10, 6))
plt.plot(df[frekvens_kol], df[rms_kol], linewidth=1, color='orange')
plt.title('Spektrumanalyse av utgangssignal')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('Størrelse (RMS) [V]')
plt.grid(True)

plt.text(
    fund_freq + 100,
    fund_rms - 0.05,
    f'Fundamental frekvens: {fund_freq:.1f} Hz\nRMS: {fund_rms:.5f} V',
    ha='left',
    va='top',
    color='red',
    backgroundcolor='white'
)

plt.tight_layout()
plt.show()
