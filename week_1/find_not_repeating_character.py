input = "abacabade"


def find_not_repeating_character(string):
    # 0으로 가득 찬 Array 채우기
    alphabet_occurrence_array = [0] * 26

    # input으로 받은 char 수를 채워넣기
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
    print(alphabet_occurrence_array)

    # 한번만  노출된 알파펫 출력
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            print(chr(index + ord('a')))

    return "_"



result = find_not_repeating_character(input)
print(result)