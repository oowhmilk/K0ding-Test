# 1초에 5000만개 계산 가능

## 배열 초기화 
# 4 * 5 크기 배열 
arr = [[i] * 5 for i in range(4)]

## Dictionary 자료형 (key, value) 형식 
# 특정한 데이터의 등장 횟수 세기
data = {}
data['apple'] = "사과"
data['banana'] = "바나나"

data = [1,3,3,5,4,3,1,4]
counter = {}

for i in data:
    if i not in counter :
        counter[i] = 1
    else :
        counter[i] += 1

print(counter)

## Dictionary 자료형 반복문 작성 법
for key in counter :
    value = counter[key]

# Dictionary 자료형 value 값으로 정렬하는 법
max(dict.values())

# Dictionary 자료형 key 로 정렬
sorted_dict = sorted(dict.itmes())


# Dictionary 자료형 value 로 정렬
sorted_dict = sorted(dict.itmes(), key = lambda x : x[1])

## Set 자료형 
# 데이터의 중복을 허용하지 않고, 순서 상과 없을때 사용하는 형식
# 특정한 데이터의 등장 여부를 판단하기 

data = [1,3,3,5,4,3,1,4]
visited = set()

for i in data :
    visited.add(i)

print(visited)

## 사용자 입력 형태 
# x = int(input())
# y = int(input())


## enumerate() 함수
# 인덱스와 함께 반복하기 
name_list = ["김", "이", "박"]
for i, element in enumerate(name_list) :
    print(i, element)


## 소수 찾기
for x in range(11) :
    prime = True
    for y in range(2, x) :
        if x % y == 0 :
            prime = False
            break
    
    if prime == True :
        print(x, "소수 O")
    elif prime == False :
        print(x, "소수 X")

## 리스트 내에서 가장 큰 값 찾기
def find_max(arr):
    max_index = 0
    max_value = 0
    for i in range(len(arr)) :
        if max_value < arr[i] :
            max_value = arr[i]
            max_index = i

    print(max_index, max_value)

arr = [7,1,5,9,3,2,4]
find_max(arr)

## 특정한 값을 가지는 원소 찾기
def find_value(arr, value) :
    find_arr = -1
    for i in range(len(arr)) :
        if value == arr[i] :
            find_arr = i
            break
    
    return find_arr

print(find_value(arr, 9))
print(find_value(arr, 8))


## 순열 (1, 2), (1, 3), (2, 1)
from itertools import permutations
arr = ['a', 'b', 'c']
result = list(permutations(arr, 2))
print(result)

## 중복 순열 (1, 1), (1, 2), (1, 3), (2, 1), (2, 2)
from itertools import product
result = list(product(arr, repeat=2))
print(result)

## 조합 (1, 2), (1, 3), (2, 3)
from itertools import combinations
result = list(combinations(arr, 2))
print(result)

## 중복 조합 (1, 1), (1, 2), (1, 3), (2, 2), (2, 3)
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(arr, 2))
print(result)


## 내장 함수
print(max(arr))
print(min(arr))
print(sum(arr))
print(sorted(arr))


## 우선순위 큐(priority queue)의 목적으로 힙(heap)
# 힙에 원소를 넣었다가 빼는 것만으로 오름차순 정렬 가능 O(NlogN)

import heapq

heap =[]
result = []

for i in arr :
    heapq.heappush(heap, i)

for i in range(len(heap)) :
    x = heapq.heappop(heap)
    result.append(x)

print(result)


## 절대값 만들기 함수
abs()


## 코딩 테스트 입출력 형태 맞추기
n = int(input())
arr = list(map(int, input().split()))

print(n)
print(arr)

## 입력 문자열의 다수 라인인 경우 시간 초과를 피하기 위해서 import sys
import sys
input  = sys.stdin.readline

data = input().strip() # 개행 지우기 
data = input().rstrip() 
print(data)


# String -> list 로 한 글자씩 넣는 법
arr = list(str)

#String 띄워쓰기 기준으로 나눠서 list 에 저장
arr = str.split(' ')

# 기본 정렬 라이브러리 사용시 tuple 이용해서 key 값으로 정렬 하는 방법
arr = sorted(arr, key = lambda x: x[0])

# 기본 정렬 라이브러리 사용시 tuple 이용해서 key 값으로 내림차순 정렬 하는 방법 -- key = lambda x : -x[0] 마이너스 붙이기
arr = sorted(arr, key = lambda x : -x[1])

# 여러개 기준으로 정렬해야하는 경우
arr = sorted(arr, key = lambda x : (x[0], x[1], x[2]))

# x, y 에 대해 동시 정렬할때 그냥 sorted 만 사용해도 자동 정렬 가능
arr = sorted(arr) 

# 정렬하는 방법
arr.sort()
sorted(arr)

# 내림차순 정렬 하는 방법
arr = sorted(arr, reverse = True)

# 계수 정렬 알고리즘 ( 수의 범위가 1 ~ 10000 )
# 배열의 인덱스를 특정한 데이터의 값으로 여기는 정렬 방법
# 데이터가 등장한 횟수를 셈

# 정수 -> String
str(integer)

# String 만들때 + 이용해서 만들기
string += str(integers[i]) + operators[i]

# eval()
eval(string.replace(" ", ""))

# 재귀함수 순환 횟수 제한 풀기 
sys.setrecursionlimit(100000)

# 문자를 하나씩 확인하며 숫자일때만 더하기
# isdigit() == '0' <= x and x <= '9'
for x in str :
    if x.isdigit() :
        result += int(x)

# 하나의 문자를 해당 문자에 해당하는 유니코드 정수를 반환하는 함수
ord('a') # => 97

# 하나의 정수를 해당 정수에 해당하는 유니코드 문자를 반화하는 함수
chr(97) # => 'a'

# 원형 큐 => 회전하는 배열을 사용하기 위해서 반드시 "deque" 사용
q = deque()
q.rotate(1) # => 증가하는 방향으로 1만큼 회전
q.rotate(-1) # => 감소하는 방향으로 1 만큼 회전