# https://www.hackerrank.com/challenges/python-string-split-and-join?isFullScreen=true

def split_and_join(line):
    listOfString = line.split(" ")
    return "-".join(listOfString)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)