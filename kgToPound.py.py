while True:
    value = input("kg (종료하려면 'q' 입력): ")
    if value == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        kg = float(value)
        print(kg * 2.20462262, "lbs")