import argparse
import os
import json

from numpy import mat
# from analyze import cepstrum
from analyze import analyze
from comparison import comparison
from chooser import chooser
from http_req import http_req_lib as req
import backup

parser = argparse.ArgumentParser(description='解答用プログラム')
parser.add_argument('match', help='試合番号')
parser.add_argument('stage', help='問題番号')
parser.add_argument('-j', '--jump', default=0, type=int, help='プロセス開始位置')
parser.add_argument('-s', '--start', action='store_true', help='GETで問題情報を取得')


# rootdir = __file__
rootdir = os.path.dirname(os.path.abspath(__file__))
args = parser.parse_args()


match = args.match
stage = args.stage
start = args.jump
isbegin = args.start



def main():
    Status = dict()
    problem_info = dict()
    analyzed_data = dict()
    similarity_data = dict()
    answer_cards = dict()
    answer_number = 0

    print("Try GET/mutch")
    if isbegin:
        Status = req.GETmatch()
        backup.statusWrite(match, Status)
    else:
        Status = backup.statusLoad(match)
    print("GET/mutch finish")

    if int(start) <= 0:
        # request
        print("Try GET/probrem")
        # req.ClearChunkPathList()
        problem_info = req.GETproblem()
        toiPathes = req.AutomaticRequestChunksPath(max(int(problem_info["chunks"]/2, 2)))
        answer_number = int(problem_info["data"])
        backup.infoWrite(match,stage,problem_info)
        backup.toiPathesWrite(match,stage,toiPathes)
        print("GET/probrem finish")
    else:
        problem_info = backup.infoLoad(match, stage)
        toiPathes = backup.toiPathesLoad(match, stage)
        answer_number = int(problem_info["data"])


    if int(start) <= 1:
        # analyze
        print("Try analyzing")
        num = 0
        for toi in toiPathes:
            analyzed_data["seg"+str(num)] = analyze.analyze(toi)
            num += 1
        backup.analyzedWrite(match,stage,analyzed_data)
        print("analyzing finish")
    else:
        analyzed_data = backup.analyzedLoad(match, stage)


    if int(start) <= 2:
        # comparison
        print("Try comparing")
        similarity_data = comparison.comparison(analyzed_data)
        backup.similarityWrite(match,stage,similarity_data)
        print("comparing finish")
    else:
        similarity_data = backup.similarityLoad(match, stage)


    if int(start) <= 3:
        # chooser
        # answer_number = 20 # teststatus
        print("Try card choosing")
        answer_cards = chooser.chooser(similarity_data, answer_number)
        print(answer_cards)
        backup.answerWrite(match,stage,answer_cards)
        print("card choosing finish")
    else:
        answer_cards = backup.answerLoad(match, stage)


    if int(start) <= 4:
        # send
        print("Try POST")
        answer = set([i[1:] for i in answer_cards[:3]])
        post_data = dict()
        with open("./interaction.json", "rt") as file:
            post_data = json.load(file)
        post_data["answer"] = list(answer)
        print(post_data)
        with open("./interaction.json", "w+") as file:
            json.dump(post_data, file, indent=4)
        req.POSTanswer()
        print("POST finish")

if __name__ == '__main__':
    main()