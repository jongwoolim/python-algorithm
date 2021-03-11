

def solution(words):
    answer = []
    round_words = []
    round = 0
    for i in range(len(words)):
        round_words.append(words[i])
        
        for j in range(len(round_words)):
            if round_words[j] == words[i]:
                round = j + 1
                break
        answer.append(round)
                
    return answer