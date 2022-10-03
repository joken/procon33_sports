import numpy as np
import wave
import matplotlib.pyplot as plt

select = "J02"

filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/JKspeech/{}.wav".format(select)
# filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/sample_Q_202205/sample_Q_E01/{}.wav".format(select)
outname = "/home/gisuperu/Desktop/procon33_sports/developper/graph{}.png".format(select)

def analyze():
    w = wave.open(filename, 'rb')
    data = w.readframes(w.getnframes())
    w.close()

    fs = w.getframerate()
    s = (np.frombuffer(data, dtype="int16") / 32767.0)[0:fs]
    F = np.fft.fft(s)
    # F_abs = np.abs(F)
    F_abs = F
    F_a = F_abs / fs * 2
    F_a[0] = F_abs[0] / fs
    plt.plot(F_a[:int(fs/2)+1])
    plt.savefig(outname)

def main():
    analyze()

if __name__ == '__main__':
    main()