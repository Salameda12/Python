# 1
def linear_search(arr, target):
    for i in range(len(target)):
        if arr == target[i]:
            return i
    return "값이 없음"

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

# 2
def LinearSearch(arr, target):
  i = 0
  while i < len(arr):
    if arr[i] == target:
      return i
    i += 1
  return "값이 없음"

target = int(input("찾을 값 >> "))

arr = [3, 5, 6, 1, 4, 7, 9, 8]
print(LinearSearch(arr, target))

# 3
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

n = int(input("배열의 크기를 입력하세요: "))

arr = []
print("배열의 요소를 입력하세요:")
for _ in range(n):
    element = int(input())
    arr.append(element)

target = int(input("찾을 값을 입력하세요: "))

result = linear_search(arr, target)

if result != -1:
    print(f"값 {target}의 인덱스는 {result}입니다.")
else:
    print("배열에서 찾고자 하는 값이 없습니다.")