# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string, sub_string):
    my_count,  my_list = 0, []
    sub_string_length = len(sub_string)

    for _ in range(len(string)):
        slice_of_string = string[my_count: my_count + sub_string_length]
        my_list.append(slice_of_string)
        my_count += 1

    my_count = 0

    for _ in my_list:
        if sub_string == _:
            my_count += 1

    return my_count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# hackerrank-python solutions

# def count_substring(string, sub_string):
#     count = 0
#     for i in range(len(string)):
#         if string[i:].startswith(sub_string):
#             count += 1
#     return count

# def count_substring(s, sub):
#     return [s[i:i+len(sub)] for i in range(len(s))].count(sub)


# My solution a month later
# def count_substring(string, sub_string):
#     low = 0
#     count = 0
#     high = len(sub_string)
#
#     for i in range(len(string)):
#         if sub_string == string[low+i:high + i]:
#             count += 1
#
#     return count
