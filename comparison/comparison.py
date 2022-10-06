import json

# def buckup(match, stage, analyzed_data, similarity_data):
#     print()

def comparison(match, stage, analyzed_data):
    yomi_data = dict()
    with open("yomi.json", "r") as f:
        yomi_data = json.load(f)

    yomi_names = yomi_data.keys()

    similarity_data = dict()
    for name in yomi_names:
        yomi_value = yomi_data[name]["data"]
        similarity = 1.0
        for i in range(yomi_data[name]["size"]):
            similarity *= analyzed_data[i]/yomi_value[i]

        similarity_data[name] = similarity
    
    # buckup(match, stage, analyzed_data, similarity_data)
    return similarity_data


if __name__ == '__main__':
    comparison()