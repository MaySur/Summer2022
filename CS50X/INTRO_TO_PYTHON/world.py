def main():
    name = input('WHAT IS UR NAME? ')
    print(hello(name))


def hello(to ='world'):
    return f'hello, {to}'


if __name__ == "__main__":
    main()