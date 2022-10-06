import argparse
import os

from numpy import mat
# from analyze import cepstrum
from analyze import analyze
from comparison import comparison
from chooser import chooser
from http_req import http_req_lib as req

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


def main():
    toiPathes = []
    analyzed_data = dict()
    similarity_data = dict()
    answer_cards = list()

    # print(req.ClearChunkPathList()) OK
    print(req.AutomaticRequestChunksPath(3))

if __name__ == '__main__':
    main()