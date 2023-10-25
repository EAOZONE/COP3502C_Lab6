def encoder(password):
    encoded_password = ''
    for i in range(len(password)):
        password_integer = int(password[i]) + 3
        encoded_password += str(password_integer)[-1]
    return encoded_password


def decode(password):
    decoded = ''
    for digit in password:
        decoded_digit = (str(int(digit) - 3) % 10)
        decoded += decoded_digit
    return decoded


def main():
    while True:
        print('Menu')
        print('-' * 9)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        choice = int(input('Do you want to encode, decode or quit? '))
        if choice == 1:
            password = input('What is your password? ')
            print(encoder(password))
        elif choice == 2:
            print('This is for the other person ')
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
