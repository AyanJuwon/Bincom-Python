#  Function to create the
# random binary string


import random


def rand_bin_to_dec():

    # Variable to store the
    # string
    p = 4
    key1 = ""

    # Loop to find the string
    # of desired length
    for i in range(p):

        # randint function to generate
        # 0, 1 randomly and converting
        # the result into str
        temp = str(random.randint(0, 1))

        # Concatenatin the random 0, 1
        # to the final result
        key1 += temp

    print(key1)
    print(int(key1, 2))
    return key1


#
rand_bin_to_dec()
