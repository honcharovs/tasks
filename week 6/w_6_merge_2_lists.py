def merge(left_list, right_list):
    sorted_list = []  # объединенный отсортированный список
    left_l_index = 0
    right_l_index = 0
    left_l_length = len(left_list)  # длина левого списка
    right_l_length = len(right_list)  # длина правого списка
    for i in range(left_l_length + right_l_length):
        if left_l_index < left_l_length and right_l_index < right_l_length:
            if left_list[left_l_index] <= right_list[right_l_index]:
                sorted_list.append(left_list[left_l_index])
                left_l_index += 1
            else:
                sorted_list.append(right_list[right_l_index])
                right_l_index += 1
        elif left_l_index == left_l_length:
            sorted_list.append(right_list[right_l_index])
            right_l_index += 1
        elif right_l_index == right_l_length:
            sorted_list.append(left_list[left_l_index])
            left_l_index += 1
    return sorted_list
left_list = list(map(int, input().split()))
right_list = list(map(int, input().split()))
sorted_list = merge(left_list, right_list)
print(*sorted_list)
