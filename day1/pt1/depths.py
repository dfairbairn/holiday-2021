# Keep it simple for the first and read from a file with fixed name

# Edit the file name for your input
file_name = "inputs/full_input.txt"

with open(file_name, 'r') as f:
    depths = []
    for line in f.readlines():
        depths.append(int(line[:-1]))

    slopes = []
    for i in range(len(depths)):
        if i == 0:
            continue 
        slopes.append(depths[i] - depths[i-1])

    # How many slopes are positive?
    increases = 0
    for slope in slopes:
        if slope > 0:
            increases += 1

    print(increases)
