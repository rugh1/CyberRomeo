import os
import sys

FILE_NAME = "encrypted_msg.txt"
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W',
           'V', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '.', ';', "'", '?', '!', ':', '']
NUMBERS = [56, 57, 58, 59, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 10, 11, 12,
           13, 14, 15, 16, 17, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
           100, 101, 102, 103, 104, 105, '']


def encrypt(msg):
    if not os.path.exists(FILE_NAME):
        temp_file_handle = open(FILE_NAME, 'a').close()
    file_handle = open(FILE_NAME, 'w')
    file_handle.write(",".join(map(lambda x: str(NUMBERS[LETTERS.index(x)]), msg)))
    file_handle.close()


def read_file(path):
    try:
        file_handle = open(FILE_NAME, 'r')
        message = file_handle.read()
        file_handle.close()
        return message
    except FileNotFoundError:
        print('this file does not exist pls check and re run the program')
        return None


def decrypt(msg):
    return ''.join(map(lambda x: LETTERS[NUMBERS.index(int(x))], msg.split(',')))


def main(mode):
    if mode == 'encrypt':
        message = input("enter msg to encrypt: ")
        encrypt(message)
    elif mode == 'decrypt':
        message = read_file(FILE_NAME)
        if not message == '' and not None:
            print(decrypt(message))


if __name__ == '__main__':
    main(sys.argv[1])
