# 2021-12-09

# def solution(participant, completion):
#     record = dict()
#     for p in participant:
#         if record.get(p) == None:
#             record[p] = 1
#         else:
#             record[p] += 1

#     for c in completion:
#         record[c] -= 1

#     candidate = [k for k, v in record.items() if v == 1]
#     return candidate[0]


import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
