def is_palindrome(s):
    if len(s) < 1:
        print("Палиндром!")
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            print("Не палиндром!")



