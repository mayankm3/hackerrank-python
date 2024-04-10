# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(string):
    vowel = ['A', 'E', 'I', 'O', 'U']
    S = 0
    K = 0

    for i in range(len(string)):
        if string[i] in vowel:
            K += len(string)-i  # Hackerrank witchcraft
        else:
            S += len(string)-i

    if S > K:
        print(f"Stuart {S}")
    elif K > S:
        print(f"Kevin {K}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)




# why len(string)-i equals the number of times a word occurs in string?

# For the word "BANANA", the first vowel 'A' occurs at position 1, len("BANANA") = 6, so there are 6-1 = 5 substrings
# starting with this letter 'A': ['A', 'AN', 'ANA', 'ANAN', 'ANANA'], you add one extra letter to that specific letter 'A'
# until you get to the end of the word.

# and on subsequent iterations, you count the same substrings as additional instances.