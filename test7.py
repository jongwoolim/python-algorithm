def solution(s):
    answer = ""
    count = [0] * 123
    max_count = 0
    #스트링의 대소문자를 고려하지 않는다
    
    #가장 많은 알파벳이 하나일 때 소문자로 반환
    ignore_string = s.lower()

    for i in range(len(s)):
        count[ord(ignore_string[i])] += 1

    #최댓값 갯수
    for i in range(len(count)):
        if max(count) == count[i]:
            max_count += 1
            
    if max_count == 1:
        answer = chr(count.index(max(count))) 
    else:
        #print(count)
        #print(max(count))
        for k in range(len(count)):
            if count[k] == max(count):
                #print(count.index(count[k]))
                answer += chr(k)
                
            
    
    #가장 많은 알파벳이 2개 이상이면 알파벳 순서대로 반환
    
    return answer


print(solution("BAC"))
