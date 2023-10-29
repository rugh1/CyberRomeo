import sys
import logging

logging.basicConfig(filename='mylog.log', encoding='utf-8', level=logging.DEBUG)

FILE_NAME = "encrypted_msg.txt"

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ',', '.', ';', "'", '?', '!', ':', '']

NUMBERS = [56, 57, 58, 59, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 10, 11, 12,
           13, 14, 15, 16, 17, 18, 19, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
           100, 101, 102, 103, 104, 105, '']

EXM = (('My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I have, '
        'for both are infinite.',
        '48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,90,98,12,90,98,91,19,16,98,90,16,12'
        ',99,98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,91,19,16,98,34,36,39,16,98,44,98,18,30,93,16,98'
        ',91,36,98,91,19,16,16,99,98,65,19,16,98,34,36,39,16,98,44,98,19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,'
        '12,39,16,98,30,35,17,30,35,30,91,16,100'),

       ("Don't waste your love on somebody, who doesn't value it.",
        '59,36,35,102,91,98,94,12,90,91,16,98,96,36,92,39,98,33,36,93,16,98,36,35,98,90,36,34,16,13,36,15,96,99,98,'
        '94,19,36,98,15,36,16,90,35,102,91,98,93,12,33,92,16,98,30,91,100'),

       ("Love is a smoke raised with the fume of sighs; Being purged, a fire sparkling in lovers' eyes; Being vexed"
        " a sea nourish'd with loving tears: What is it else? a madness most discreet, A choking gall, "
        "and a preserving sweet.",
        '47,36,93,16,98,30,90,98,12,98,90,34,36,32,16,98,39,12,30,90,16,15,98,94,30,91,19,98,91,19,16,98,17,92,'
        '34,16,98,36,17,98,90,30,18,19,90,101,98,57,16,30,35,18,98,37,92,39,18,16,15,99,98,12,98,17,30,39,16,98'
        ',90,37,12,39,32,33,30,35,18,98,30,35,98,33,36,93,16,39,90,102,98,16,96,16,90,101,98,57,16,30,35,18,98'
        ',93,16,95,16,15,98,12,98,90,16,12,98,35,36,92,39,30,90,19,102,15,98,94,30,91,19,98,33,36,93,30,35,18,'
        '98,91,16,12,39,90,105,98,68,19,12,91,98,30,90,98,30,91,98,16,33,90,16,103,98,12,98,34,12,15,35,16,90,'
        '90,98,34,36,90,91,98,15,30,90,14,39,16,16,91,99,98,56,98,14,19,36,32,30,35,18,98,18,12,33,33,99,98,12'
        ',35,15,98,12,98,37,39,16,90,16,39,93,30,35,18,98,90,94,16,16,91,100'),
       ('My only love sprung from my only hate! Too early seen unknown, and known too late! Prodigious birth of love '
        'it is to me That I must love a loathed enemy.',
        '48,96,98,36,35,33,96,98,33,36,93,16,98,90,37,39,92,35,18,98,'
        '17,39,36,34,98,34,96,98,36,35,33,96,98,19,12,91,16,104,98,65,36,36,98,16,12,39,33,96,98,90,16,16,35,98,'
        '92,35,32,35,36,94,35,99,98,12,35,15,98,32,35,36,94,35,98,91,36,36,98,33,12,91,16,104,98,61,39,36,15,30,'
        '18,30,36,92,90,98,13,30,39,91,19,98,36,17,98,33,36,93,16,98,30,91,98,30,90,98,91,36,98,34,16,98,65,19,12'
        ',91,98,44,98,34,92,90,91,98,33,36,93,16,98,12,98,33,36,12,91,19,16,15,98,16,35,16,34,96,100'))


def diff(str_to_check, answer):
    diff_in_check = ""
    diff_in_answer = ""
    for i in range(0, len(str_to_check)):
        if str_to_check[i] != answer[i]:
            diff_in_check += str_to_check[i]
            diff_in_answer += answer[i]
    return f"in output: {diff_in_check}, the answer: {diff_in_answer}"


def test_code():
    count = 0
    for example in EXM:
        count += 1
        if (encrypt(example[0]) == example[1]) and (decrypt(example[1]) == example[0]):
            print(f"example number:{count} passed :)")
        else:
            print(f"example number:{count} failed :(")
            print(f"in encryption: {diff(encrypt(example[0]), example[1])}")
            print(f"test decryption: {diff(decrypt(example[1]), example[0])}")


def encrypt(msg):
    return ",".join(map(lambda x: str(NUMBERS[LETTERS.index(x)]), msg))


def write_file(path, msg):
    try:
        file_handle = open(path, 'w')
        file_handle.write(msg)
        file_handle.close()
        return True
    except Exception as err:
        logging.error("error in writing to file" + str(err))
        return False


def read_file(path):
    try:
        file_handle = open(path, 'r')
        message = file_handle.read()
        file_handle.close()
        return message
    except IOError:
        logging.error("error in reading file IOError")
        print("file did not exist")
        return None
    except Exception as err:
        logging.error("error in reading file" + str(err))
        return None


def decrypt(msg):
    return ''.join(map(lambda x: LETTERS[NUMBERS.index(x if x == '' else int(x))], msg.split(',')))


def main(mode):
    if mode == 'encrypt':
        message = input("enter msg to encrypt: ")
        encrypted_message = encrypt(message)
        success = write_file(FILE_NAME, encrypted_message)
        logging.debug(f'message inputted: {message}     message encrypted: {encrypted_message}   successfully written '
                      f'to file: {success} ')
    elif mode == 'decrypt':
        message = read_file(FILE_NAME)
        if message is not None:
            decrypted_message = decrypt(message)
            logging.debug(f'message read: {message}     message decrypted {decrypted_message}')
            print(decrypt(message))


if __name__ == '__main__':
    assert (len(sys.argv) == 2)
    main(sys.argv[1])
