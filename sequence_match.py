def match_sequence(target_string,universal_string):
    for i in range(len(universal_string) - len(target_string)):
        j = 0
        while j < len(target_string) and universal_string[j+i] == target_string[j]:
            j += 1
        if j == len(target_string):
            return i
    return -1