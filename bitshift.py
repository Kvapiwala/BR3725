
num = int(input("enter a number: "))
num_bin = bin(num)[2:]
print(num_bin)
bits = int(input("enter a single digit number to shift by: "))
shift = num * (2** bits)
shift = bin(shift)[2:]
new_num = int(shift, 2)

print(shift)
print(new_num)