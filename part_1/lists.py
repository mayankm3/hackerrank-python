# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())

    myList = []

    for _ in range(N):
        command = input().split(" ")
        match command[0]:
            case "insert":
                myList.insert(int(command[1]),int(command[2]))
            case "print":
                print(myList)
            case "remove":
                myList.remove(int(command[1]))
            case "append":
                myList.append(int(command[1]))
            case "sort":
                myList.sort()
            case "pop":
                myList.pop()
            case "reverse":
                myList.sort(reverse=True)
            case _: # Default case in python
                print("Other error")




# Python 3.10 (2021) introduced the match-case statement