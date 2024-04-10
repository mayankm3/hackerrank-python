# https://www.hackerrank.com/challenges/swap-case?isFullScreen=true

def swap_case(s):
    # s.swapcase() or use join function
    swapList = [st.lower() if st.isupper() else st.upper() for st in s]
    var = "".join(swapList)
    return var


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
