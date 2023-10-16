'''
Задание 1

Напишите функцию, которая будет принимать список nums, содержащий числа в диапазоне от 1 до 100, и возвращать отсортированный 
список чисел, которые в списке nums встречались дважды.
'''


def duplicate_nums(nums: list):

    nums_conversion = [nums[i] for i in range(len(nums)) if nums[i] in nums[i+1:]]

    if len(nums_conversion) > 0:

        sort_nums = sorted(nums_conversion)

    else:
        sort_nums = None

    return sort_nums


nums = [1, 2, 3, 1, 4, 5, 6, 7, 7, 3]

print(duplicate_nums(nums))