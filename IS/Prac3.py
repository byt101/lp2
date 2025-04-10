def hex2bin(s):
    return bin(int(s, 16))[2:].zfill(len(s) * 4)

def bin2hex(s):
    return hex(int(s, 2))[2:].upper().zfill(len(s) // 4)

def permute(k, arr):
    return "".join(k[i - 1] for i in arr)

def xor(a, b):
    return "".join("0" if a[i] == b[i] else "1" for i in range(len(a)))

def shift_left(k, shifts):
    return k[shifts:] + k[:shifts]

initial_perm = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
final_perm = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
expansion_table = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
pc1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def generate_keys(key):
    key = hex2bin(key)
    key = permute(key, pc1)
    left, right = key[:28], key[28:]
    rkb = []
    for shift in shift_table:
        left, right = shift_left(left, shift), shift_left(right, shift)
        rkb.append(permute(left + right, pc2))
    return rkb

def feistel_function(right, key):
    right_expanded = permute(right, expansion_table)
    xor_x = xor(right_expanded, key)
    return xor_x

def encrypt(pt, rkb, verbose=True):
    pt = hex2bin(pt)
    pt = permute(pt, initial_perm)
    left, right = pt[:32], pt[32:]
    if verbose:
        print("Encryption\nAfter initial permutation", bin2hex(left + right))
    for i, key in enumerate(rkb):
        new_right = xor(left, feistel_function(right, key))
        left, right = right, new_right
        if verbose:
            print(f"Round {i+1}", bin2hex(left), bin2hex(right))
    cipher_text = permute(left + right, final_perm)
    return bin2hex(cipher_text)

def decrypt(ct, rkb, verbose=True):
    rkb.reverse()
    return encrypt(ct, rkb, verbose)

key = "AABB09182736CCDD"
pt = "123456ABCD132536"

rkb = generate_keys(key)
cipher_text = encrypt(pt, rkb)
print("Cipher Text:", cipher_text)

decrypted_text = decrypt(cipher_text, rkb)
print("Plain Text:", decrypted_text)