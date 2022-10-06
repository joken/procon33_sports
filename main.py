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
parser.add_argument('-j', '--jamp', default=0, help='プロセス開始位置')


# rootdir = __file__
rootdir = os.path.dirname(os.path.abspath(__file__))
args = parser.parse_args()


match = args.match
stage = args.stage
start = args.jamp

answer_number = 0


def main():
    toiPathes = backup.toiPathesLoad(match, stage)
    analyzed_data = backup.analyzedLoad(match, stage)
    similarity_data = backup.simirarityLoad(match, stage)
    answer_cards = backup.answerLoad(match, stage)

    if start <= 0:
        # request
        # req.ClearChunkPathList()
        toiPathes = req.AutomaticRequestChunksPath(3)

    if start <= 1:
        # analyze
        num = 0
        for toi in toiPathes:
            analyzed_data["seg"+str(num)] = analyze.analyze(match, stage, num, toi)
            num += 1

    if start <= 2:
        # comparison
        for key in analyzed_data.keys():
            similarity_data = comparison.comparison(match, stage, analyzed_data[key]) # ?add similarity_data
    
    if start <= 3:
        # chooser
        answer_cards = chooser.chooser(match, stage, similarity_data, answer_number)
    
    if start <= 4:
        # send
        print("Hello")

if __name__ == '__main__':
    main()