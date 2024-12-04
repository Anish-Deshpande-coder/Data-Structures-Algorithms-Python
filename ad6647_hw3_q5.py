from collections import deque
def permutations(lst):
    result = []
    queue = deque([[]])
    stack = lst
    while queue:
        current = queue.popleft()
        if len(current) == len(lst):
            result.append(current)
        else:
            for i in range(len(stack)):
                if stack[i] not in current:
                    new = current + [stack[i]]
                    queue.append(new)
    return result



