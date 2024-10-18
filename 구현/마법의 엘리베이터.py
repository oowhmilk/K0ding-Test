def solution(storey):
    answer = 0
    
    while True :
        
        if (storey // 10) == 0 and (storey % 10) == 0:
            break
        
        now_check = storey % 10
        
        if now_check < 5 :
            answer += now_check
            
            next = storey // 10
            storey = next
            
        elif now_check == 5 :
            
            answer += (10 - now_check)
            
            next = storey // 10
            next_check = next % 10
            
            if 5 <= next_check : 
                next = next + 1
                storey = next
            else :
                next = storey // 10
                storey = next
                
            
        else : 
            answer += (10 - now_check)
            
            next = storey // 10
            storey = next + 1
        
    return answer