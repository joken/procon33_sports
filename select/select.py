
def buckup(match, stage, similarity_dict, ans_cards):
    write


def select(match, stage, similarity_data, ans_numbers):
    similarity_dict = dict()
    similarity_dict = similarity_data

    similarity_list = sorted(similarity_dict.items(), key = lambda s: s[1])

    ans_cards = [sim[0] for sim in similarity_list][:ans_numbers]

    buckup(match, stage, similarity_dict, ans_cards)
    return ans_cards


# -----
if __name__ == '__main__':
    similarity_data = dict
    select("sample", 0, similarity_data, 20)