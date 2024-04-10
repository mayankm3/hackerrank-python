# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

#The problem asks us to check all characters in the string and print true or false.
# We need to print true if any character in the given string satisfies the condition.
# It doesn't ask us if the whole string is only alphanumeric or only digits.

if __name__ == '__main__':
    s = input()

    print(any(st.isalnum() for st in s))    # e.g., 5 is alphanumeric and 6 is also alphanumeric
    print(any(st.isalpha() for st in s))    #
    print(any(st.isdigit() for st in s))
    print(any(st.islower() for st in s))
    print(any(st.isupper() for st in s))



# Another hackerrank-python solution
# arr = [False]*5
#
# for letter in str:
# 	if letter.isalnum():
# 		arr[0] = True
# 	if letter.isalpha():
# 		arr[1] = True
# 	if letter.isdigit():
# 		arr[2] = True
# 	if letter.islower():
# 		arr[3] = True
# 	if letter.isupper():
# 		arr[4] = True
#
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])
# print(arr[4])
