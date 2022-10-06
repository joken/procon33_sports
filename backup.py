import json
from typing import OrderedDict

# backupPath = "/home/gisuperu/Desktop/procon33_sports/backup"
backupPath = "./backup"
backupStatus = backupPath + "/question.json"
backupAnalyzed = backupPath + "/analyzed.json"
backupSimilarity = backupPath + "/similarity.json"
backupAnswer = backupPath + "/answer.json"

def cleanUP():
    with open(backupStatus, "w") as file:
        json.dump(dict({}), file, indent=4)
    with open(backupAnalyzed, "w") as file:
        json.dump(dict({}), file, indent=4)
    with open(backupSimilarity, "w") as file:
        json.dump(dict({}), file, indent=4)
    with open(backupAnswer, "w") as file:
        json.dump(dict({}), file, indent=4)


# toiPahtes
def toiPathesWrite(match, stage, toiPathes):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match][stage]["toi"] = toiPathes
    with open(backupStatus, "w+") as file:
        json.dump(d_update, file, indent=4)

def toiPathesLoad(match, stage):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)
    return d_update[match][stage]["toi"]

# analyzed data
def analyzedWrite(match, stage, analyzed_data):
    d_update
    with open(backupAnalyzed, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match][stage] = analyzed_data
    with open(backupAnalyzed, "w+") as file:
        json.dump(d_update, file, indent=4)

def analyzedLoad(match, stage):
    d_update
    with open(backupAnalyzed, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)
    return d_update[match][stage]

# similarity data
def simirarityWrite(match, stage, simirarity_data):
    d_update
    with open(backupSimilarity, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match][stage] = simirarity_data
    with open(backupSimilarity, "w+") as file:
        json.dump(d_update, file, indent=4)

def simirarityLoad(match, stage):
    d_update
    with open(backupSimilarity, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)
    return d_update[match][stage]

# answer cards
def answerWrite(match, stage, answer_cards):
    d_update
    with open(backupAnswer, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match][stage] = answer_cards
    with open(backupAnswer, "w+") as file:
        json.dump(d_update, file, indent=4)

def answerLoad(match, stage):
    d_update
    with open(backupAnswer, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)
    return d_update[match][stage]

if __name__ == '__main__':
    cleanUP()