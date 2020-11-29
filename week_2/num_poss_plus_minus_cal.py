numbers = [2, 3, 1]
target_number = 0
result = []  # 모든 경우의 수를 담기 위한 배열

# solution 1 :
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(numbers):  # 탈출조건!
        all_ways.append(current_sum)  # 마지막 인덱스에 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + numbers[current_index], all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - numbers[current_index], all_ways)

# solution 2 :
# def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum, all_ways_count):
#     if current_index == len(numbers):  # 탈출조건!
#         if current_sum == target:
#             all_ways_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
#         return
#     get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
#                                                        current_sum + numbers[current_index],
#                                                        all_ways_count)
#     get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
#                                                        current_sum - numbers[current_index],
#                                                        all_ways_count)


get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
print(result)