def generate_prefix(target_string: str) -> list:
    length = len(target_string)
    pi_list = [0] * length
    i = 0
    j = 1
    while j < length:
        if target_string[i] == target_string[j]:
            pi_list[j] = i + 1
            i += 1
            j += 1
        elif i > 0:  # case target_string[i] != target_string[j]
            i = pi_list[i - 1]
        else:  # case i == 0
            pi_list[j] = 0
            j += 1
    return pi_list


def kmp(full_string: str, substring: str) -> list:
    substring_length = len(substring)
    main_string_length = len(full_string)
    if main_string_length == 0 or substring_length > main_string_length:
        return []
    pi_list = generate_prefix(substring)
    print("Pi list: ", pi_list)
    substring_entry_indexes = []
    i = 0
    j = 0
    while i < main_string_length and j < substring_length:
        if full_string[i] == substring[j]:
            if j == substring_length - 1:
                substring_entry_indexes.append(i - substring_length + 1)
                j = 0
            else:
                j += 1
            i += 1
        elif j > 0:  # case full_string[i] != substring[j]
            j = pi_list[j - 1]
        else:  # case j == 0
            i += 1
    return substring_entry_indexes
