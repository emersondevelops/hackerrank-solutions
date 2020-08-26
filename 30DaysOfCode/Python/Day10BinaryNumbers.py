if __name__ == '__main__':
    n = int(input())

    # my solution starts here:

    binary_num = ''

    # populate a string with the remainder of consecutive divisions
    while n > 0:
        binary_num += str(n % 2)
        n //= 2

    # the generated binary number have to be reversed
    binary_num = binary_num[::-1]

    # my strategy was to break the ones blocks into a list using the zeros as separator
    one_blocks = binary_num.split('0')

    # order the pieces according to their sizes
    one_blocks.sort()

    # print out the length of the largest piece of ones
    print(len(one_blocks[-1]))
