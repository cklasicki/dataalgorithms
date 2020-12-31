def sum_integers(n):
    print('entering with n={}'.format(n))
    if n == 1:
        print('return for n={}, output={}'.format(n, 1))    
        return 1

    output = n + sum_integers(n-1) 
    print('return for n={}, output={}'.format(n, output))    
    return output

print(sum_integers(3))


# 1 + 2 + 3
# 1 + 1 + (n-1) + 

