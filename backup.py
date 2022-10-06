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


# Status
def statusWrite(match, status):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match]["status"] = status
    with open(backupStatus, "w+") as file:
        json.dump(d_update, file, indent=4)

def statusLoad(match):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)
    return d_update[match]["status"]

# probrem info
def infoWrite(match, stage, probrem_info):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match][stage]["info"]= probrem_info
    with open(backupStatus, "w+") as file:
        json.dump(d_update, file, indent=4)

def infoLoad(match, stage):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)
    return d_update[match][stage]["info"]

# toiPahtes
def toiPathesWrite(match, stage, toiPathes):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match][stage]["path"]= toiPathes
    with open(backupStatus, "w+") as file:
        json.dump(d_update, file, indent=4)

def toiPathesLoad(match, stage):
    d_update
    with open(backupStatus, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)
    return d_update[match][stage]["path"]

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
def similarityWrite(match, stage, similarity_data):
    d_update
    with open(backupSimilarity, "rt") as file:
        d_update = json.load(file, object_pairs_hook=OrderedDict)

    d_update[match][stage] = similarity_data
    with open(backupSimilarity, "w+") as file:
        json.dump(d_update, file, indent=4)

def similarityLoad(match, stage):
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