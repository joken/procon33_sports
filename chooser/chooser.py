import json

# def buckup(match, stage, similarity_dict, ans_cards):
#     select_buckup = "{}/buckup/{}".format(main.rootdir, "{}{}.json".format(match, stage))
    
#     # with open(select_buckup, "w+", encoding="utf-8") as f:


answerBackupPath = "/home/gisuperu/Desktop/procon33_sports/backup/" + "answer.json"

def chooser(similarity_data, ans_numbers, match, stage):
    similarity_dict = dict()
    similarity_dict = similarity_data

    similarity_list = sorted(similarity_dict.items(), key = lambda s: s[1])

    # ans_cards = [sim[0] for sim in similarity_list][:ans_numbers] # もともとの最善取得
    
    # buckup(match, stage, similarity_dict, ans_cards)
    # return ans_cards

    # 札の取り直しなし----
    out = []
    past = set()
    ans_cards = [sim[0] for sim in similarity_list]
    if(stage == "1" or stage == "01"):
        ans_cards = ans_cards[:int(ans_numbers)]
    else:
        AnsTrace = dict()
        with open(answerBackupPath, "r") as f:
            AnsTrace = json.load(f)
        AnsTrace = AnsTrace[match]
        for key in AnsTrace.keys():
            if int(key) < int(stage):
                # past.union(AnsTrace[key])
                for a in AnsTrace[key]:
                    past.add(a)
            else:
                continue

    for card in [sim[0] for sim in similarity_list]:
        if card in list(past):
            continue
        out.append(card)
    return out[:ans_numbers]
    # 札の取り直しなしEOF-------



# -----
if __name__ == '__main__':
    similarity_data = dict()
    chooser("sample", 0, similarity_data, 20)