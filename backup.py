import os
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

def testInit():
    question = dict({
        "test1" : {
            "status" : {
                "problems": 1,
                "bonus_factor": [1.0],
                "penalty": 1
            },
            "1" : {
                "info" : {
                    "id": "sample_Q_E01",
                    "chunks": 2,
                    "starts_at": 1655302266,
                    "time_limit": 1000,
                    "data": 3
                },
                "path" : [
                    "./origin_data/sample_Q_202205/sample_Q_E01/problem1.wav",
                    "./origin_data/sample_Q_202205/sample_Q_E01/problem2.wav"
                ]
            }
        }
    })
    with open(backupStatus, "w+") as file:
        json.dump(question, file, indent=4)


# Status
def statusWrite(match, status):
    d_update = dict()
    with open(backupStatus, "rt") as file:
        d_update = json.load(file)
    d_update.setdefault(match, {})
    # d_update.update({match: {}})
    # print(d_update)

    d_update[match]["status"] = status
    with open(backupStatus, "w+") as file:
        json.dump(d_update, file, indent=4)

def statusLoad(match):
    d_update = dict()
    with open(backupStatus, "rt") as file:
        d_update = json.load(file)
    return d_update[match]["status"]

# probrem info
def infoWrite(match, stage, probrem_info):
    d_update = dict()
    with open(backupStatus, "rt") as file:
        d_update = json.load(file)
    d_update.setdefault(match, {})
    d_update[match].setdefault(stage, {})
    # d_update.update({match: {stage: {}}})
    # print(d_update)

    d_update[match][stage]["info"]= probrem_info
    with open(backupStatus, "w+") as file:
        json.dump(d_update, file, indent=4)

def infoLoad(match, stage):
    d_update = dict()
    with open(backupStatus, "rt") as file:
        d_update = json.load(file)
    return d_update[match][stage]["info"]

# toiPahtes
def toiPathesWrite(match, stage, toiPathes):
    d_update = dict()
    with open(backupStatus, "rt") as file:
        d_update = json.load(file)
    d_update.setdefault(match, {})
    d_update[match].setdefault(stage, {})
    # d_update.update({match: {stage: {}}})
    # print(d_update)

    d_update[match][stage]["path"]= toiPathes
    with open(backupStatus, "w+") as file:
        json.dump(d_update, file, indent=4)

def toiPathesLoad(match, stage):
    d_update = dict()
    with open(backupStatus, "rt") as file:
        d_update = json.load(file)
    return d_update[match][stage]["path"]

# analyzed data
def analyzedWrite(match, stage, analyzed_data):
    d_update = dict()
    with open(backupAnalyzed, "rt") as file:
        d_update = json.load(file)
    d_update.setdefault(match, {})
    d_update[match].setdefault(stage, {})
    # d_update.update({match: {stage: {}}})
    # print(d_update)

    d_update[match][stage] = analyzed_data
    with open(backupAnalyzed, "w+") as file:
        json.dump(d_update, file, indent=4)

def analyzedLoad(match, stage):
    d_update = dict()
    with open(backupAnalyzed, "rt") as file:
        d_update = json.load(file)
    return d_update[match][stage]

# similarity data
def similarityWrite(match, stage, similarity_data):
    d_update = dict()
    with open(backupSimilarity, "rt") as file:
        d_update = json.load(file)
    d_update.setdefault(match, {})
    d_update[match].setdefault(stage, {})
    d_update[match][stage].setdefault("dict", {})
    d_update[match][stage].setdefault("soted", {})
    # d_update.update({match: {stage: {}}})
    # print(d_update)

    similarity_data_alt = sorted(similarity_data.items(), key=lambda x : x[1])

    d_update[match][stage]["dict"] = similarity_data
    d_update[match][stage]["soted"] = similarity_data_alt
    with open(backupSimilarity, "w+") as file:
        json.dump(d_update, file, indent=4)

def similarityLoad(match, stage):
    d_update = dict()
    with open(backupSimilarity, "rt") as file:
        d_update = json.load(file)
    return d_update[match][stage]["dict"]

# answer cards
def answerWrite(match, stage, answer_cards):
    d_update = dict()
    with open(backupAnswer, "rt") as file:
        d_update = json.load(file)
    d_update.setdefault(match, {})
    d_update[match].setdefault(stage, {})
    # d_update.update({match: {stage: {}}})
    # print(d_update)

    d_update[match][stage] = answer_cards
    with open(backupAnswer, "w+") as file:
        json.dump(d_update, file, indent=4)

def answerLoad(match, stage):
    d_update = dict()
    with open(backupAnswer, "rt") as file:
        d_update = json.load(file)
    return d_update[match][stage]

if __name__ == '__main__':
    os.makedirs("./backup", exist_ok=True)
    cleanUP()
    testInit()