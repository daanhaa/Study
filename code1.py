#여러 줄에 걸쳐 입력 받기
name = input("이름: ")
age = int(input("나이: "))
print(name, "님의 나이는", age, "살입니다.")

#공백 포함된 입력 처리
full_name = input("이름과 성: ")
age = int(input("나이: "))

print(full_name, "님의 나이는", age, "살 입니다.")

# 두 줄에 입력받은 정수 더하기
num1 = int(input("첫번째 숫자 입력: "))
num2 = int(input("두번째 숫자 입력: "))
print("두 수의 합은", num1 + num2)

#input().split()을 이용한 입력 처리
data = input("띄어쓰기 구분하여 입력: ").split()
print(data)

#한 줄에 입력 받아 변수에 담기
a, b, c = input("띄어쓰기 구분하여 입력: ").split()
print(a)
print(b)
print(c)

#입력 받은 데이터 형 변환
num1, num2 = map(int, input("더할 숫자: ").split())
print("두 수의 합은: ", num1 + num2)

#test
firstname = input("성: ") 
name = input("이름: ")
age = int(input("나이: "))
print("당신의 이름은: ", firstname+name, "내년 나이는: ",age+1 )

#실수a,b,c 입력 받아 소수셋째자리까지 반올림하여 출력
#split은 문자열에서만 사용가능, map(자료형, 입력.split())
a,b,c = map(float,input("실수 a b c 입력").split())
print(f"{a:.3f}\n{b:.3f}\n{c:.3f}") 

#입출력 연습
# 두 개 수 합과 평균 계산
num1 = 15
num2 = 20

total = num1 + num2
print("sum=", total)

average = total/2
print("평균: ", average)

print(f"합: {num1:.2f}, 평균: {average:.3f}")

#BMI계산
weight = float(input("몸무게"))
height = float(input("키"))

bmi = weight / ((height/100)**2) #m를 cm로 입력
print(f"BMI는 {bmi:.2f}")


x = 5
y = 10
avg = (x + y) // 2 #목 7
x += avg #7+5
print(x) #12

#조건문
a = int(input("입력:"))
if(a%2 ==0):
    print("짝수입니다")

else:
    print("홀수입니다")


#변수를 선언해서 정수 a b를 입력받고, 다음 조건에 따라 만족하면 1을, 
# 만족하지 않는다면 0을 각 줄에 출력합니다.
# 변수 선언, 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

# 출력
print(int(a >= b))
print(int(a > b))
print(int(a <= b))
print(int(a < b))
print(int(a == b))
print(int(a != b))

#Else
weather = "sunny"
if weather =="rain":
    print(f"{weather}이므로 우산챙기기")

else:
    print(f"{weather}이므로 선글라스 챙긴다")


A,B = map(int,input().split())


#입력받아 비교하기
if A<B:
    print("1", end=" ") 
    #end=" "는 줄바꿈 대신 지정한 문자열 출력하는것임

else:
    print("0",end=" ")

if A==B:
    print("1")
else:
    print("0")


weather = "snow"
if weather == "sunny":
    activity = "running"

elif weather == "rain":
    activity = "sleep"

else:
    activity = "None"

print(f"오늘 활동은 {activity}")

#반복문
for i in range(10):
    print("Hello")


#반복문 N번 더하기
a,b = 5,6

for i in range(b):
    a += b
    print(a)