"""
Write a function that checks whether two given strings contain the same number of digits. Generalize the function's
behavior to check whether the two strings contain the same number of characters that meet a certain dynamically passed condition.
"""

from typing import Callable

# def compare_matching_chars(c1: str, c2: str, cond: Callable[[str], int]) -> bool:
#     return cond(c1) == cond(c2)
#
# def count_digits(c1: str) -> int:
#     return sum([1 for char in c1 if char in '0123456789'])
#
# def main() -> None:
#     print(compare_matching_chars('halo11henlo', '5436vfj2', count_digits))
#     print(compare_matching_chars('halo11henlo', '5vfj2', count_digits))
#
# if __name__ == '__main__':
#     main()


def create_staircase(nums):

    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
          subsets.append(nums[0:step])
          nums = nums[step:]
          step += 1
          return subsets
        else:
          return False







print(create_staircase([1, 2, 3, 4, 5, 6]))


def create_staircase_2(nums):


    while len(nums) != 0:
        step = 1
        subsets = []
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False

    return subsets


print(create_staircase_2([1, 2, 3, 4, 5, 6]))