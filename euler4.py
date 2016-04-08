#https://projecteuler.net/problem=4

def is_palindrome(n: int) -> bool:
    string = str(n)
    length = len(string)
    for i in range(0, int(length / 2)):
        if(string[i] != string[length - i - 1]):
            return False
    return True

def biggest_palindrome_for_2_numbers(number_digits_for_each: int) -> (int):
    assert number_digits_for_each > 0
    maxnumber = 0
    maxpalindrome = 0;
    for i in range(0, number_digits_for_each):
        maxnumber += (10 ** i) * 9
    number1 = maxnumber
    while(len(str(number1)) == number_digits_for_each):
        number2 = maxnumber
        while(len(str(number2)) == number_digits_for_each):
            if is_palindrome(number1 * number2) and number1 * number2 > maxpalindrome:
                maxpalindrome = number1 * number2
            number2 -= 1
        number1 -= 1
    return maxpalindrome

