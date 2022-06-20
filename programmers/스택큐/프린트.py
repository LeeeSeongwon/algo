from collections import deque

def solution(priorities, location):
    answer = []
    stack = deque([i for i in range(0, len(priorities))])
    priorities = deque(priorities)
    
    while priorities:
        flag = 0
        for priority in priorities:
            if priority > priorities[0]:
                flag = 1
                break
        else:
            priorities.popleft()
            answer.append(stack.popleft())

        if flag:
            item = priorities.popleft()
            priorities.append(item)
            item = stack.popleft()
            stack.append(item) 

    print(answer.index(location) + 1)
    return answer.index(location) + 1

if __name__ == "__main__":
    solution([2, 1, 3, 2], 2)