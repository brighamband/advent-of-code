"""3 Measurement Sliding Window Variation of Day 1"""

SLIDING_WINDOW_SIZE = 3

num_increases = 0

# Grab nums from file
file = open("in.txt", "r")
nums = [int(line) for line in file]
file.close()

for i in range(0, len(nums)):
    last_nums = nums[i : i + SLIDING_WINDOW_SIZE]
    cur_nums = nums[i + 1 : i + 1 + SLIDING_WINDOW_SIZE]

    if sum(cur_nums) > sum(last_nums):
        num_increases += 1

print("Increased", num_increases, "times")
