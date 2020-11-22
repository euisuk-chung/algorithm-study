'''
Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
'''


input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for num_chk in range(1, number+1):
        #print(num_chk)
        # for each num_chk
        cnt = 0  # cnt 초기화
        for num_div in range(1, num_chk + 1):
            # 나머지가 0이면 cnt +1
            if num_chk % num_div == 0:
                #print(num_div)
                cnt += 1
        if cnt == 2:
            prime_list.append(num_chk)
        #print("end of loop")
    return prime_list


result = find_prime_list_under_number(input)
print(result)

'''
# solution 1
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list


# solution 2
def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list
'''