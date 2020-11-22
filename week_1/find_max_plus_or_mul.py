input = [0, 3, 5, 6, 1, 2, 4]

'''
곱셈과 더하기 연산으로 구할 수 있는
최대값을 출력하는 문제
'''


def find_max_plus_or_mul(array):
    multiply_sum = 0
    for number in array: #O(N)
        if number <= 1 or multiply_sum == 0:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_mul(input)
print(result)