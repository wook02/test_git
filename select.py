choice = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if choice == 1:
    cal = input("*** 수식을 입력하세요: ")
    result = eval(cal)
    print(str(cal) + " 결과는 " + str(result) + " 입니다.")

elif choice == 2:
    num1 = int(input("*** 첫 번째 숫자를 입력하세요: "))
    num2 = int(input("*** 두 번째 숫자를 입력하세요: "))
    total = sum(range(num1, num2 + 1))
    print(str(num1) + "+...+" + str(num2) + "는 " + str(total) + "입니다.")

else:
    print("1 또는 2 중에서 선택해주세요.")