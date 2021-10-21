# Advent of Code - 2019 - Day 2

example_input = '1,9,10,3,2,3,11,0,99,30,40,50'
input_part_one = open('d2_p1input.txt')

# Parameters
example_data = False
debug = False

if example_data:
    input_str = example_input.split(',')
else:
    input_file = open('d2_p1input.txt')
    input_row = input_file.read()
    input_str = input_row.split(',')

# parse input into an array of integers
op_codes = []
for c in input_str:
    op_codes.append(int(c))

if debug:
    print('Start values: ' + str(op_codes))

# fix code
# before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
op_codes[1] = 12
op_codes[2] = 2

if debug:
    print('Values after fix: ' + str(op_codes))


for i in range(0, len(op_codes), 4):
    if op_codes[i+1] > len(op_codes) or op_codes[i+2] > len(op_codes) or op_codes[i+3] > len(op_codes):
        break

    first = op_codes[i+1]
    second = op_codes[i+2]
    third = op_codes[i+3]

    if op_codes[i] == 1:
        # ADD - three next positions - add the first two values and store the output in the third value position
        if debug:
            print(' ---- begin add ---- ')
            print('Before: ' + str(op_codes))
        op_codes[third] = op_codes[first] + op_codes[second]
        if debug:
            print('After:  ' + str(op_codes))
            print(' ---- end of add ---- ')

    elif op_codes[i] == 2:
        # MULTIPLY - three next positions - multiply the first two and store the output in the third value position
        if debug:
            print(' ---- begin multiply ---- ')
            print('Before: ' + str(op_codes))
        op_codes[third] = op_codes[first] * op_codes[second]
        if debug:
            print('After:  ' + str(op_codes))
            print(' ---- end of multiply ---- ')

    elif op_codes[i] == 99:
        if debug:
            print(' ---- found exit code 99 on position: ' + str(i) + ' ---- ')
        break


if debug:
    print('After:  ' + str(op_codes))


# What value is left at position 0 after the program halts?
print(' - Part one -   The value at position 0 is: ' + str(op_codes[0]))

