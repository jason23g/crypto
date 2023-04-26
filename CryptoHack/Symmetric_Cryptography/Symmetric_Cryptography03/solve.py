state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    plaintext = []
    for row in matrix:
        plaintext.append(row[0])
        plaintext.append(row[1])
        plaintext.append(row[2])
        plaintext.append(row[3])


    return plaintext


def add_round_key(s, k):

    res = [[0 for i in range(4)] for i in range(4)]

    for i in range(0,4):
        res[i][0] = s[i][0]^k[i][0]
        res[i][1] = s[i][1]^k[i][1]
        res[i][2] = s[i][2]^k[i][2]
        res[i][3] = s[i][3]^k[i][3]

    return "".join([chr(x) for x in matrix2bytes(res)])


print(add_round_key(state, round_key))


