from itertools import permutations

def solution(k, dungeons):
    answer = -1
    now = k
    
    arr = [i for i in range(1, len(dungeons) + 1)]
    check = list(permutations(arr, len(arr)))
    
    
    for x in check :
        count = 0
        for j in range(len(x)) :
            need, use = dungeons[x[j] - 1]
            if need <= now :
                now -= use
                count += 1
            else :
                break
                
        answer = max(answer, count)
        now = k
    
    return answer