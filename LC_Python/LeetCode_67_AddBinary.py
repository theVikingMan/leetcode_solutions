def addBinary(a, b):
  x, y = int(a, 2), int(b, 2)
  return bin(x + y)[2:]


def addBinary(a, b):
    x, y = int(a, 2), int(b, 2)
    while y:
        answer = x ^ y
        carry = (x & y) << 1
        x, y = answer, carry
    return bin(x)[2:]

print(addBinary('11', '1'))



'''
def addBinary(a, b):
    def convert_str_a(a):
        a_num, first_a_pos = 0
        for i in range(len(a), 0, -1):
            a_num += (int(a[i-1]))*(2**first_a_pos)
            first_a_pos += 1
    def convert_str_b(b):
        b_num, first_b_pos = 0
        for i in range(len(b), 0, -1):
            b_num += (int(b[i-1]))*(2**first_b_pos)
            first_b_pos += 1
        return b_num
    convert_str_a(a) + convert_str_b(b)

print(addBinary("11", "1"))
'''
