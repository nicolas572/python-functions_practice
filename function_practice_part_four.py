def max_num (a,b,c):
    return max([a,b,c])
print(max_num(1,50,100))

def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
my_list = [1, 50, 100]
result = mult_list(my_list)
print('Multiplication result is', result)

def rev_string(my_str):
  return my_str[::-1]

print(rev_string("python"))

def num_within(number, start_range, end_range):
    return start_range <= number <= end_range

print(num_within(1,50,100))

def pascal(n):
    if n <= 0:
        return

    current_row = [1]

    for i in range(n):
        print(" ".join(map(str, current_row)))

        next_row = [1]
        for j in range(1, len(current_row)):
            next_row.append(current_row[j - 1] + current_row[j])
        next_row.append(1)

        current_row = next_row

n = 1 
pascal(n)
