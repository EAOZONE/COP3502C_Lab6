def encoder(password):
    encoded_password = ''
    for i in range(len(password)):
        password_integer = int(password[i]) + 3
        encoded_password += str(password_integer)[-1]

    return encoded_password


def main():
    password = input()
    print(encoder(password))


if __name__ == '__main__':
    main()