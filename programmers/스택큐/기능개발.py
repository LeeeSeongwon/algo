def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    # progresses 자체를 stack으로 본다.
    sec = 0 
    temp_ans = 0
    while progresses:
        if progresses[-1] + speeds[-1] * sec >= 100:
            progresses.pop()
            speeds.pop()
            temp_ans += 1
        else:
            if temp_ans != 0:
                answer.append(temp_ans)
            temp_ans = 0
            sec += 1
    
    answer.append(temp_ans)
    return answer