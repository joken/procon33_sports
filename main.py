import argparse
import os

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
parser.add_argument('-j', '--jump', default=0, help='プロセス開始位置')
parser.add_argument('-s', '--start', action='store_true', help='GETで問題情報を取得')


# rootdir = __file__
rootdir = os.path.dirname(os.path.abspath(__file__))
args = parser.parse_args()


match = args.match
stage = args.stage
start = args.jump
isbegin = args.start

answer_number = 0


def main():
    if isbegin:
        Status = req.AnalyzeSpec() # must make function
        backup.statusWrite(match, Status)
    else:
        Status = backup.statusLoad(match)
    toiPathes = backup.toiPathesLoad(match, stage)
    analyzed_data = backup.analyzedLoad(match, stage)
    similarity_data = backup.similarityLoad(match, stage)
    answer_cards = backup.answerLoad(match, stage)

    if start <= 0:
        # request
        # req.ClearChunkPathList()
        probrem_info = dict()
        toiPathes = req.AutomaticRequestChunksPath(3)
        backup.infoWrite(match,stage,probrem_info)
        backup.toiPathesWrite(match,stage,toiPathes)

    if start <= 1:
        # analyze
        num = 0
        for toi in toiPathes:
            analyzed_data["seg"+str(num)] = analyze.analyze(match, stage, num, toi)
            num += 1
        backup.analyzedWrite(match,stage,analyzed_data)

    if start <= 2:
        # comparison
        for key in analyzed_data.keys():
            similarity_data = comparison.comparison(match, stage, analyzed_data[key]) # ?add similarity_data
        backup.similarityWrite(match,stage,similarity_data)

    if start <= 3:
        # chooser
        answer_cards = chooser.chooser(match, stage, similarity_data, answer_number)
        backup.answerWrite(match,stage,answer_cards)

    if start <= 4:
        # send
        print("Hello")

if __name__ == '__main__':
    main()