while True:
    value = input("반지름 (종료하려면 'q' 입력): ")
    if value == 'q':
        print("프로그램을 종료합니다.")
        break
    else:
        radius = float(value)
        area = 3.14 * radius ** 2
        circumference = 2 * 3.146 * radius
        print("원의 넓이:", area)
        print("원의 둘레:", circumference)