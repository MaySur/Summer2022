def main():
    height = int(input("Height :"))
    pyrm(height)


def pyrm(x):
    for i in range(x):
        print("*" * (i + 1))


if __name__ == "__main__":
    main()
