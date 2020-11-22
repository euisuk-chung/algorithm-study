'''
0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다.
주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.
'''

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    string = list(string)

    # make empty list
    num_list = [0, 0]
    
    # 0이 많은지 1이 많은지 확인
    for num in string:
        if num == "0":
            num_list[0] += 1
        else:
            num_list[1] += 1

    # max_num 지정
    if num_list[0] >= num_list[1]:
        max_num = "0"
    else:
        max_num = "1"
    
    # 0이 많은지 1이 많은지 확인
    for i in range(len(string)):
        if string[i] == max_num:
            continue
        else:
            string[i] = max_num

    finalString = ''.join(string)

    return finalString


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)


'''
# solution
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '0':
                count_to_all_one += 1
            if string[i + 1] == '1':
                count_to_all_zero += 1

    return min(count_to_all_one, count_to_all_zero)
'''