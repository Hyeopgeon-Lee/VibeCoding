
def main():
    print("===== 2단부터 9단까지 구구단 =====")

    for number in range(2, 10):
        print(f"\n----- {number}단 -----")
        for i in range(1, 10):
            print(f"{number} x {i} = {number * i}")


if __name__ == "__main__":
    main()


