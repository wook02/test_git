while True:
    value = input("inch (종료하려면 'q' 입력): ")
    if value == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        Inch = float(value)
        print(Inch * 2.54, "cm")