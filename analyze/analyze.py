import soundfile as sf
import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

# def buckup(match, stage, number, analyzed_data):
#     print()


# cepstrum
def db(x, dBref):
    y = 20 * np.log10(x / dBref)
    return y
def lin(x, dBref):
    y = dBref * 10 ** (x / 20)
    return y
def norm(spectrum, dBref):
    spectrum = lin(spectrum, dBref)
    spectrum = np.abs(spectrum / (len(spectrum) / 2))
    spectrum = db(spectrum, dBref)
    return spectrum

def cepstrum(data, samplerate):
    # ケプストラム分析
    spec = fftpack.fft(data)                              # 時間波形をフーリエ変換してスペクトルにする
    spec_db = db(spec, 2e-5)                              # スペクトルを対数(dB)にする(0dB=20[μPa])
    
    ceps_db = np.real(fftpack.ifft(spec_db))              # 対数スペクトルを逆フーリエ変換してケプストラム波形を作る
    index = 50                                            # ローパスリフターのカットオフ指標
    ceps_db[index:len(ceps_db) - index] = 0               # ケプストラム波形の高次を0にする（ローパスリフター）
    ceps_db_low = fftpack.fft(ceps_db)
    # グラフ用に振幅を正規化
    spec_db_amp = norm(spec_db, 2e-5)                     # 音声スペクトルの振幅成分を計算
    ceps_db_low_amp = norm(ceps_db_low, 2e-5)             # ローパスリフター後のスペクトル包絡の振幅成分を計算

    out = tuple(ceps_db_low_amp)
    # print(type(ceps_db_low))
    return out

def cepstrum_alt(data, samplerate):
    spectrum_amp_log = np.log(np.abs(np.fft.fft(data, len(data))))
    cep = np.fft.fft(spectrum_amp_log)
    dims = 100
    cep[dims:cep.shape[0]-dims]  =0
    plt.plot(cep)
    plt.savefig("./out.png")
    plt.close()

def cepstrum_alt2(data, samplerate):
    n = len(data)
    fscale = np.linspace(0, samplerate, n)
    dft = np.fft.fft(data,n)

    dft_abs = np.abs(dft)
    logampDFT = 10*np.log10(dft_abs**2)

    cps = np.real(np.fft.ifft(logampDFT))

    cpsCoef = 100
    cps[cpsCoef:len(cps) - cpsCoef] = 0
    
    dft_cps_low = np.real(np.fft.fft(cps, n))

    return list(dft_cps_low)


# main process
def analyze(wavfile):
    data, samplerate = sf.read(wavfile)

    analyzed_data = cepstrum(data, samplerate)
    
    # buckup(match, stage, analyzed_data)
    return analyzed_data


# debug
if __name__ == '__main__':
    path = "./J01.wav"
    ana = analyze(path)
    print(ana)
    print(type(ana))
    print(len(ana))