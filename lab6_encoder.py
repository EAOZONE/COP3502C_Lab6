def encoder(password):
    encoded_password = ''
    for i in range(len(password)):
        password_integer = int(password[i]) + 3
        encoded_password += str(password_integer)[-1]

    return encoded_password


def main():
    while True:
        print("Menu")
        print("-"*7)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        Choice = int(input("do you want to encode, decode or quit?"))
        if Choice == 1:
            password = input('What is your password?')
            print(encoder(password))
        elif Choice == 2:
            print("This is where decode goes")
        elif Choice == 3:
            break


if __name__ == '__main__':
    main()