shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# solution 1
# def is_available_to_order(menus, orders):
#     available_order = []
#     # 이 부분을 채워보세요!
#     for order in orders:
#         for menu in menus:
#             if order == menu:
#                 print("{}는 주문이 가능합니다!".format(menu))
#                 available_order.append(menu)
#     return available_order

# solution 2 : 이분 탐색
def is_available_to_order(menus, orders):
    menus.sort()  # menus 정렬 / O(N*logN)
    for order in orders: # O(M*logN)
        if not is_existing_target_number_binary(order, menus): # O(logN)
            return False
    return True


def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False

# solution 3 : 집합 사용
# def is_available_to_order(menus, orders):
#     menus_set = set(menus)
#     for order in orders:
#         if order not in menus_set:
#             return False
#     return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)