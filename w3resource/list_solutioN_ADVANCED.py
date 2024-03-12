# 1. Write a Python function to reverse a list at a specific location.
def reverse_list_in_location(lst, start_pos, end_pos):
    if start_pos < 0 or end_pos >= len(lst) or start_pos > end_pos:
        return lst
    return lst[:start_pos] + lst[start_pos:end_pos+1][::-1] + lst[end_pos+1:]


print(reverse_list_in_location([10, 20, 30, 40, 50, 60, 70, 80], 2, 4))
print(reverse_list_in_location([10, 20, 30, 40, 50, 60, 70, 80], 1, 4))
