def solution(progresses, speeds):
    answer = []
    
    finish = 0
    day = 0
    while 1 :
        
        if finish == len(progresses) :
            break
        
        day += 1
        
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
            
        count = 0
        for i in range(finish, len(progresses)) :
            if progresses[i] >= 100 :
                finish += 1
                count += 1
            else :
                break
                
        if count != 0 :
            answer.append(count)
            
    return answer






