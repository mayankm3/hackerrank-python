# https://www.hackerrank.com/challenges/nested-list?isFullScreen=true

if __name__ == '__main__':
    scores = set()
    myList = []
    listForMultipleNames = []

    for _ in range(int(input())):   # _ is used to signify that even though something is being returned,
                                    # we don't plan to use that variable any where.
        name = input()
        score = float(input())
        myList.append([name, score])
        scores.add(score)

    secondLowest = sorted(scores)[1]

    for name, score in myList:
        if score == secondLowest:
            listForMultipleNames.append(name)

    print(*sorted(listForMultipleNames), sep="\n")
