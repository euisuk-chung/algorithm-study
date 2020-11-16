input = [3, 5, 6, 1, 2, 4]


def number_existence(number, array):
    for num in array: # array의 길이만큼 아래 연산이 실행된다
        if num != number: # 비교연산 실행
            continue
        else:
            return True

# def number_existence(number, array):
#     for num in array: # array의 길이만큼 아래 연산이 실행된다
#         if num == number: # 비교 연산 실행
#             return True # N * 1 = N 만큼
#     return False


result = number_existence(3, input)
print(result)