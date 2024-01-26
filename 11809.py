import math


def main():
    n = input()
    if n == "0e0":
        return
    nf = float(n)
    mantissa, exponent = math.frexp(nf)

    mantissa_binary = format(mantissa, ".15f").split(".")[1]
    print(mantissa_binary)
    mantissa_binary = mantissa_binary[1:].strip("0")
    print(mantissa_binary)
    M = len(mantissa_binary)

    E = exponent.bit_length()
    print(M, E)


while True:
    try:
        main()
    except EOFError:
        break
