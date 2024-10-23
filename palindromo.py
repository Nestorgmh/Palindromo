def is_palindrome(x):
    original_num = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original_num == reversed_num

x = 121
if is_palindrome(x):
    print("El número es un palíndromo")
else:
    print("El número no es un palíndromo")