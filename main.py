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
    print("Try GET/mutch")
    if isbegin:
        Status = req.GETmatch()
        backup.statusWrite(match, Status)
    else:
        Status = backup.statusLoad(match)
    print("GET/mutch finish")

    if start <= 0:
        # request
        print("Try GET/probrem")
        # req.ClearChunkPathList()
        probrem_info = dict()
        toiPathes = req.AutomaticRequestChunksPath(3)
        backup.infoWrite(match,stage,probrem_info)
        backup.toiPathesWrite(match,stage,toiPathes)
        print("GET/probrem finish")
    else:
        toiPathes = backup.toiPathesLoad(match, stage)

    if start <= 1:
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


    if start <= 2:
        # comparison
        print("Try conparing")
        for key in analyzed_data.keys():
            similarity_data = comparison.comparison(analyzed_data)
        backup.similarityWrite(match,stage,similarity_data)
        print("conparing finish")
    else:
        similarity_data = backup.similarityLoad(match, stage)


    if start <= 3:
        # chooser
        print("Try card choosing")
        answer_cards = chooser.chooser(similarity_data, answer_number)
        backup.answerWrite(match,stage,answer_cards)
        print("card choosing finish")
    else:
        answer_cards = backup.answerLoad(match, stage)


    if start <= 4:
        # send
        print("Try POST")
        print("POST finish")

if __name__ == '__main__':
    main()