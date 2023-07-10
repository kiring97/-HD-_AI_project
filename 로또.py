# 1) 로또 번호 생성 함수
import random

def getLotto():
    numbers = []
    while len(numbers) < 6:
        n = random.randint(1, 45)
        if n not in numbers:
            numbers.append(n)
    return numbers
    
print('로또번호:', getLotto())

# 2) random 모듈 활용
import random

# 1 ~ 45 숫자 저장
candidate_nubers = [x+1 for x in range(45)] 
# random.shuffle(candidate_nubers)

print(random.sample(candidate_nubers, k=6))