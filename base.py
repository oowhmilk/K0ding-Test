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



## 코딩 테스트 입출력 형태 맞추기
# n = int(input())
# arr = list(map(int, input().split()))

# print(n)
# print(arr)



import sys
input  = sys.stdin.readline

data = input().rstrip()
print(data)