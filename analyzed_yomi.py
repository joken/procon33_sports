import json
from analyze import analyze

def main():
    yomifile = "/home/gisuperu/Desktop/procon33_sports/origin_data/JKspeech/{}.wav"
    outjson = "/home/gisuperu/Desktop/procon33_sports/yomi.json"

    yomi_data = dict({})
    for i in range(1, 45):
        data = analyze.cepstrum(yomifile.format("J"+str(i).zfill(2)))
        yomi_data["J"+str(i).zfill(2)] = {"size": len(data), "data": data}
        
        data = analyze.cepstrum(yomifile.format("E"+str(i).zfill(2)))
        yomi_data["E"+str(i).zfill(2)] = {"size": len(data), "data": data}

    
    with open(outjson, "w+") as file:
        json.dump(yomi_data, file, indent=4)

if __name__ == '__main__':
    main()