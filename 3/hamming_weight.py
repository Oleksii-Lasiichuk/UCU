number = int(input())
real_number = 5**number
number_output = real_number
number_bit_len = real_number.bit_length()
weight = 0

for _ in range(number_bit_len):
    last_bit = real_number & 1
    weight += last_bit
    real_number = real_number >> 1

if weight%2 == 1:
    print(f"Number {number_output} is an odious number. Its hamming weight is {weight}.")
else:
    print(f"Number {number_output} is an evil number. Its hamming weight is {weight}.")

