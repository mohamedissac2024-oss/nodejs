def up_to_n(n):
    # add all the values up to n
    sum = 0
    for i in range(1, n + 1):
        print("I is ", i, "Sum is ", sum)
        sum = sum + i

    print("Sum is ", sum)
    return sum

# Make sure this line is at the bottom!
up_to_n(5)