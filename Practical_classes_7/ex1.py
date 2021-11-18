def print_till_zero(n):
    print(n)
    if n == 1:
        exit()
    else:
        print_till_zero(n-1)

print_till_zero(5)