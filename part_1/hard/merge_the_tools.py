# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(string, k):
    while string:
        s = string[0:k]
        seen = ''
        for c in s:
            if c not in seen:
                seen += c
        print(seen)
        string = string[k:]


if __name__ == '__main__':
    string, k = input(), int(input())   # Type AABCAAADA in console press enter, type 3 and press enter again
    merge_the_tools(string, k)




