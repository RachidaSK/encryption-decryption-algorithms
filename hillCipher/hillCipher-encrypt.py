import numpy as np


def encrypt(msg):
    # Replace spaces with nothing
    msg = msg.replace(" ", "")
    # Ask for keyword and get encryption matrix
    C = make_key()
    # Append zero if the messsage isn't divisble by 2
    len_check = len(msg) % 2 == 0
    if not len_check:
        msg += "0"
    # Populate message matrix
    P = create_matrix_of_integers_from_string(msg)
    # Calculate length of the message
    msg_len = int(len(msg) / 2)
    # Calculate P * C
    encrypted_msg = ""
    for i in range(msg_len):
        # Dot product
        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
        # Modulate and add 65 to get back to the A-Z range in ascii
        integer = int(row_0 % 26 + 65)
        # Change back to chr type and add to text
        encrypted_msg += chr(integer)
        # Repeat for the second column
        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg


def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse


def make_key():
    # Make sure cipher determinant is relatively prime to 26 and only a/A - z/Z are given
    determinant = 0
    C = None
    while True:
        cipher = input("Input 4 letter cipher: ")
        C = create_matrix_of_integers_from_string(cipher)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(C) > 26 and np.amin(C) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C


def create_matrix_of_integers_from_string(string):
    # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M


def chr_to_int(char):
    # Uppercase the char to get into range 65-90 in ascii table
    char = char.upper()
    # Cast chr to int and subtract 65 to get 0-25
    integer = ord(char) - 65
    return integer


if __name__ == "__main__":
    msg = input("Message: ")
    encrypted_msg = encrypt(msg)
    print(encrypted_msg)
