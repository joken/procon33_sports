import soundfile as sf
import numpy as np
from scipy import fftpack
from matplotlib import pyplot as plt

# リニア値をdB変換
def db(x, dBref):
    y = 20 * np.log10(x / dBref)                      # リニア値をdB値に変換
    return y                                          # dB値を返す

# dB値をリニア変換
def lin(x, dBref):
    y = dBref * 10 ** (x / 20)                        # dB値をリニア値に変換
    return y                                          # リニア値を返す

# フーリエ変換の振幅を正規化
def norm(spectrum, dBref):
    spectrum = lin(spectrum, dBref)                   # 計算のために一度リニア値に戻す
    spectrum = np.abs(spectrum / (len(spectrum) / 2)) # 正規化
    spectrum = db(spectrum, dBref)                    # dB値に戻す
    return spectrum


def trans(wavfile, outfile):
    # wavの読み込み
    path = wavfile                                        # ファイルパスを指定
    data, samplerate = sf.read(path)                      # wavファイルを開き、波形とサンプリングレートを取得

    # ケプストラム分析
    spec = fftpack.fft(data)                              # 時間波形をフーリエ変換してスペクトルにする
    spec_db = db(spec, 2e-5)                              # スペクトルを対数(dB)にする(0dB=20[μPa])
    ceps_db = np.real(fftpack.ifft(spec_db))              # 対数スペクトルを逆フーリエ変換してケプストラム波形を作る
    index = 50                                            # ローパスリフターのカットオフ指標
    ceps_db[index:len(ceps_db) - index] = 0               # ケプストラム波形の高次を0にする（ローパスリフター）
    ceps_db_low = fftpack.fft(ceps_db)                    # ケプストラム波形を再度フーリエ変換してスペクトル包絡を得る

    # グラフ用の軸を作成
    frequency = np.linspace(0, samplerate, len(data))     # frequency軸を作成
    quefrency = np.arange(0, len(data)) / samplerate      # quefrency軸を作成

    # グラフ用に振幅を正規化
    spec_db_amp = norm(spec_db, 2e-5)                     # 音声スペクトルの振幅成分を計算
    ceps_db_low_amp = norm(ceps_db_low, 2e-5)             # ローパスリフター後のスペクトル包絡の振幅成分を計算

    # ここからグラフ描画
    # フォントの種類とサイズを設定する。
    plt.rcParams['font.size'] = 14
    # plt.rcParams['font.family'] = 'Times New Roman'

    # 目盛を内側にする。
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # グラフの上下左右に目盛線を付ける。
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')

    # 軸のラベルを設定する。
    ax1.set_xlabel('Frequency [Hz]')
    ax1.set_ylabel('SPL [dB]')

    # データプロット。
    ax1.plot(frequency, spec_db_amp)
    ax1.plot(frequency, ceps_db_low_amp, lw='4')

    # スケールの設定をする。
    ax1.set_xticks(np.arange(0, 20000, 1000))
    ax1.set_xlim(0, 5000)
    ax1.set_yticks(np.arange(-200, 200, 20))
    ax1.set_ylim(-20, 80)

    # レイアウト設定
    fig.tight_layout()

    # グラフを表示する。
    plt.savefig(outfile)
    plt.close()

    return len(data)