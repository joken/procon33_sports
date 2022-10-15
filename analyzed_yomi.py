import json
from analyze import analyze

def main():
    # yomifile = "/home/gisuperu/Desktop/procon33_sports/origin_data/JKspeech/{}.wav"
    # outjson = "/home/gisuperu/Desktop/procon33_sports/yomi.json"
    yomifile = "./origin_data/JKspeech/{}.wav"
    outjson = "./yomi.json"
    outjson_msk = "./mask.json"

    yomi_data = dict({})
    for i in range(1, 45):
        data = analyze.analyze(yomifile.format("J"+str(i).zfill(2)))
        yomi_data["J"+str(i).zfill(2)] = {"size": len(data), "data": data}
        
        data = analyze.analyze(yomifile.format("E"+str(i).zfill(2)))
        yomi_data["E"+str(i).zfill(2)] = {"size": len(data), "data": data}
        print(i, end=" ")


    ran = 1000000000
    for key in yomi_data.keys():
        ran = yomi_data[key]["size"] if ran > yomi_data[key]["size"] else ran
    print(ran)

    averageJP = []
    averageEN = []
    average = []
    sd = []
    sdJP = []
    sdEN = []
    for i in range(ran):
        numJP = 0
        numEN = 0
        num = 0

        average.append(0)
        averageJP.append(0)
        averageEN.append(0)
        for data in yomi_data.keys():
            if data[0] == 'E':
                average[i] += yomi_data[data]["data"][i]
                averageEN[i] += yomi_data[data]["data"][i]
                numEN += 1
                num += 1
            elif data[0] == 'J':
                average[i] += yomi_data[data]["data"][i]
                averageJP[i] += yomi_data[data]["data"][i]
                numJP += 1
                num += 1
        print("num: "+str(num))
        print("numJP: "+str(numJP))
        print("numEN: "+str(numEN))
        average[i] /= num
        averageJP[i] /= numJP
        averageEN[i] /= numEN

    # for i in range(yomi_data["J01"]["size"]):
        sd.append(0)
        sdJP.append(0)
        sdEN.append(0)
        for data in yomi_data.keys():
            if data[0] == 'E':
                sd[i] += (yomi_data[data]["data"][i] - average[i])**2
                sdEN[i] += (yomi_data[data]["data"][i] - average[i])**2
            elif data[0] == 'J':
                sd[i] += (yomi_data[data]["data"][i] - average[i])**2
                sdJP[i] += (yomi_data[data]["data"][i] - average[i])**2
        sd[i] /= num
        sdJP[i] /= numJP
        sdEN[i] /= numEN

    
    with open(outjson, "w+") as file:
        json.dump(yomi_data, file, indent=4)

    mask = dict({"ave":average, "aveJP":averageJP, "aveEN":averageEN, "sd":sd, "sdJP":sdJP, "sdEN":sdEN})
    with open(outjson_msk, "w+") as file:
        json.dump(mask, file, indent=4)

if __name__ == '__main__':
    main()