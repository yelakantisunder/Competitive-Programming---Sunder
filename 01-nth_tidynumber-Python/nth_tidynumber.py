# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def is_tidy(n):
    temp = 10
    while n != 0:
        last_digit = n % 10

        if last_digit>temp:
            return False
        temp = last_digit
        n = n //10
    return True

def fun_nth_tidynumber(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if is_tidy(guess):
            found += 1
    return guess