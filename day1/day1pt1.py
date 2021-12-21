num_increases = 0

file = open("in.txt", "r")
last_num = int(file.readline().rstrip())

for line in file:
    cur_num = int(line)
    if cur_num > last_num:
        num_increases += 1
    # Update vars for next iteration
    last_num = cur_num

print("Increased", num_increases, "times")

# Cleanup

file.close()
