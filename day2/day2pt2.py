aim = 0
horiz_pos = 0  # Horizontal position
depth = 0

file = open("in.txt", "r")

for line in file:
    # Parse line
    direction, amount = line.split()
    amount = int(amount)  # Convert amount from str -> int

    # Update positioning with new line results

    # Down increases your depth
    if direction == "down":
        aim += amount

    # Up decreases your aim
    if direction == "up":
        aim -= amount

    # Forward increases horiz_pos, increases depth (aim*amount)
    if direction == "forward":
        horiz_pos += amount
        depth += aim * amount


print("You ended up with the following:")
print("Horizontal position:", horiz_pos)
print("Depth:", depth)

print("Those multiplied is", horiz_pos * depth)
