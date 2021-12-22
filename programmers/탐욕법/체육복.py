def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for reserve_person in set_reserve:
        if reserve_person - 1 in set_lost:
            set_lost.remove(reserve_person - 1)
        elif reserve_person + 1 in set_lost:
            set_lost.remove(reserve_person + 1)

    return n - len(set_lost)
