import numpy as np
import wave
import matplotlib.pyplot as plt
import cepstrum

# reading file 
# J01 ~ J44
# E01 ~ E44
#
# prroblem sample
# 
# 


# filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/JKspeech/{}.wav".format(select)
# # filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/sample_Q_202205/sample_Q_E01/{}.wav".format(select)
# outname = "/home/gisuperu/Desktop/procon33_sports/developper/analytics/graph{}.png".format(select)

def analyze(serial):
    filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/JKspeech/{}.wav"
    # filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/sample_Q_202205/sample_Q_E01/problem{}.wav"
    outname = "/home/gisuperu/Desktop/procon33_sports/developper/analytics/graph{}.png"
    
    w = wave.open(filename.format(serial), 'rb')
    data = w.readframes(w.getnframes())
    w.close()

    fs = w.getframerate()
    s = (np.frombuffer(data, dtype="int16") / 32767.0)[0:fs]
    F = np.fft.fft(s)
    F_abs = np.abs(F)
    # F_abs = F
    F_a = F_abs / fs * 2
    F_a[0] = F_abs[0] / fs

    print(type(F_a))
    print(len(F_a))

    plt.plot(F_a[:int(fs/2)+1])
    plt.ylim(-0.001, 0.03)
    plt.grid(True)
    plt.savefig(outname.format(serial))
    plt.close()

    return len(F_a)

def analyze_sample(folder, serial):
    # filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/JKspeech/{}.wav"
    filename = "/home/gisuperu/Desktop/procon33_sports/origin_data/sample_Q_202205/sample_Q_{}/problem{}.wav".format(folder, serial)
    outname = "/home/gisuperu/Desktop/procon33_sports/developper/analytics_sample/graph{}.png".format(folder+str(serial))
    
    w = wave.open(filename, 'rb')
    data = w.readframes(w.getnframes())
    w.close()

    fs = w.getframerate()
    s = (np.frombuffer(data, dtype="int16") / 32767.0)[0:fs]
    F = np.fft.fft(s)
    F_abs = np.abs(F)
    # F_abs = F
    F_a = F_abs / fs * 2
    F_a[0] = F_abs[0] / fs

    print(type(F_a))
    print(len(F_a))

    plt.plot(F_a[:int(fs/2)+1])
    plt.ylim(-0.001, 0.03)
    plt.grid(True)
    plt.savefig(outname)
    plt.close()

    return len(F_a)

def main():
    filename1 = "/home/gisuperu/Desktop/procon33_sports/origin_data/JKspeech/{}.wav"
    filename2 = "/home/gisuperu/Desktop/procon33_sports/origin_data/sample_Q_202205/sample_Q_{}/problem{}.wav"
    outname1 = "/home/gisuperu/Desktop/procon33_sports/developper/analytics_2/graph{}.png"
    outname2 = "/home/gisuperu/Desktop/procon33_sports/developper/analytics_sample_2/graph{}.png"
    size_list = dict()

    # for i in range(1, 45):
    #     size_list["J"+str(i).zfill(2)] = cepstrum.trans(filename1.format("J"+str(i).zfill(2)), outname1.format("J"+str(i).zfill(2)))
    #     size_list["E"+str(i).zfill(2)] = cepstrum.trans(filename1.format("E"+str(i).zfill(2)), outname1.format("J"+str(i).zfill(2)))
    #     # analyze("E"+str(i))
    
    # with open("./size_list2.csv", "w+") as o_file:
    #     keys = size_list.keys()
    #     for k in keys:
    #         o_file.write("{0}, {1}\n".format(k, size_list[k]))

    folders = ["E01", "E02", "E03", "E04", "J01", "J02", "J03", "J04", "M01"]
    sizes = [2, 2, 3, 5, 2, 3, 5, 5, 5]

    for k in range(len(folders)):
        size_list = dict()
        
        folder = folders[k]
        size = sizes[k]

        size_list[folder+"0"] = cepstrum.trans(filename2.format(folder, ""), outname2.format(folder))

        for i in range(1, size+1):
            size_list[folder+str(i)] = cepstrum.trans(filename2.format(folder, i), outname2.format(folder+str(i)))

        with open("./size_list_sample2.csv", "a+") as o_file:
            o_file.write("--{}--\n".format(folder))
            keys = size_list.keys()
            for k in keys:
                o_file.write("{0}, {1}\n".format(k, size_list[k]))

if __name__ == '__main__':
    main()