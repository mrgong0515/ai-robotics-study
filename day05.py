# # open("파일명", "모드")
# # r: 읽기, w : 쓰기, b: 바이너리, a : 덮어쓰기
# file = open("simple.txt", "r", encoding="UTF-8")
# content = file.read()
# print(content)
# file.close() #열었으면 닫자

# file = open("test.txt", "w", encoding="UTF-8")
# file.write("오늘 점심 메뉴는\n")
# file.write("미정")
# file.close()

# 개발자가 close를 잊어버렸을 때 문제 발생!!
# 실수를 미연에 방지하기 위해
# with ~ open
# as (alias) 별칭
# with open("test.txt", "r", encoding="UTF-8") as file:
#     content = file.read()
#     print(content)

# 1) number.txt 파일을 만들고
# 1 ~ 100 까지 한 줄에 하나씩 저장
with open("number.txt", "w") as file:
    for i in range(1, 101):
        file.write(f"{i}\n")
        
# 2) number.txt를 읽어
# 가로로 1 ~ 100 까지 출력

with open("number.txt", "r") as file:
    content = file.read()
    nums = content.split("\n")
    print(nums)
    for num in nums:
        print(num, end=" ")

with open("number.txt", "r") as file:
    for line in file:
        print(line.strip(), end = " ")  # .strip => 공백 제거 

    # c1 = file.readline()
    # print(c1)
    # c2 = file.readline()
    # print(c2)

# split 활용하기
str1 = "사과,바나나,키위"
fruits = str1.split(",") # fruits는 리스트!!
print(fruits)

for fruit in fruits:
    print(f"{fruit}주스")
# 사과주스
# 바나나주스
# 키위주스

# join() 리스트를 문자열로 결합
# "연결자".join()
s1 = "123".join(fruits)
print(s1)
s2 = "주스".join(fruits)
print(s2)
print(s2, end="")
print("주스")
