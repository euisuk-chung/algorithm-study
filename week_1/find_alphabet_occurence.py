'''
Tips
# 해당 문자열의 알파벳 확인
print("a".isalpha())    # True
print("1".isalpha())    # False

s = "abcdefg"
print(s[0].isalpha())   # True

# 빈도수 저장 리스트 초기화
alphabet_occurrence_array = [0] * 26

# 내장 함수 ord() 이용해서 ASCII 값 받기
print(ord('a'))               # 97
print(ord('a') - ord('a'))    # 97-97 -> 0
print(ord('b') - ord('a'))    # 98-97 -> 1
'''

# Question
input = "hello my name is chung eui suk"

alphabet_occurrence_array = [0] * 26

print(alphabet_occurrence_array)


def find_max_occurred_alphabet(string):
    for i in string:
        if i.isalpha():
            idx = ord(i) - ord("a")
            alphabet_occurrence_array[idx] += 1
        else:
            continue

    print(alphabet_occurrence_array)

    max_val = max(alphabet_occurrence_array)
    index = int(alphabet_occurrence_array.index(max_val)) + 97
    output = (chr(index), max_val)

    return output


result = find_max_occurred_alphabet(input)
print(result)
