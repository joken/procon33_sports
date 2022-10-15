import json
import numpy as np

yomiPath = "/home/gisuperu/Desktop/procon33_sports/yomi.json"
# yomiPath= "./yomi.json"
maskPath = "/home/gisuperu/Desktop/procon33_sports/mask.json"
# maskPath = "./mask.json"

# def buckup(match, stage, analyzed_data, similarity_data):
#     print()

def comparison(analyzed_data):
    yomi_data = dict()
    mask_data = dict()
    with open(yomiPath, "r") as f:
        yomi_data = json.load(f)
    with open(maskPath, "r") as f:
        mask_data = json.load(f)

    yomi_names = yomi_data.keys()

    similarity_data = dict()
    for name in yomi_names:
        yomi_value = yomi_data[name]["data"]
        similarity = 1.0
        for key in analyzed_data.keys():
            for i in range(min(yomi_data[name]["size"], len(analyzed_data[key]))):
                similarity += np.abs(analyzed_data[key][i]-yomi_value[i])
                # similarity += np.min(np.abs(analyzed_data[key][i]-yomi_value[i], np.exp(np.abs(analyzed_data[key][i]-yomi_value[i]))))

        similarity_data[name] = similarity
    
    # buckup(match, stage, analyzed_data, similarity_data)
    return similarity_data


if __name__ == '__main__':
    comparison()