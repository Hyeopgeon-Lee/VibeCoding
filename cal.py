def input_number(message):
    while True:
        value = input(message)

        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            print("숫자만 입력하세요.")


def format_number(number):
    if isinstance(number, float) and number.is_integer():
        return str(int(number))
    return str(number)


def main():
    num1 = input_number("첫 번째 숫자를 입력하세요: ")
    num2 = input_number("두 번째 숫자를 입력하세요: ")

    add_result = num1 + num2
    subtract_result = num1 - num2
    multiply_result = num1 * num2

    print("\n===== 계산 결과 =====")
    print(f"입력한 숫자: {format_number(num1)}, {format_number(num2)}")
    print("--------------------")
    print(
        f"덧셈 결과: {format_number(num1)} + {format_number(num2)} = "
        f"{format_number(add_result)}"
    )
    print(
        f"뺄셈 결과: {format_number(num1)} - {format_number(num2)} = "
        f"{format_number(subtract_result)}"
    )
    print(
        f"곱셈 결과: {format_number(num1)} * {format_number(num2)} = "
        f"{format_number(multiply_result)}"
    )

    if num2 == 0:
        print("나눗셈 결과: 0으로 나눌 수 없습니다.")
    else:
        print(
            f"나눗셈 결과: {format_number(num1)} / {format_number(num2)} = "
            f"{num1 / num2:.2f}"
        )


if __name__ == "__main__":
    main()
