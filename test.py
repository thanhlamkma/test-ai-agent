input_test = input()

arr_test = input_test.split(";")
arr_real = []

for i in arr_test:
  arr_real.append(int(i))
  
for i, value in enumerate(arr_test):
  print(i, value)

print(arr_real)

def max_sum_non_adjacent(arr):
  if not arr:
    return 0
  if len(arr) == 1:
    return arr[0]
  
  # Init
  incl = arr[0]
  excl = 0
  
  # Loop through from second element
  for i in range(1, len(arr)):
    #Save previous incl before updating
    prev_incl = incl
    
    # If choose current element, plus previous excl
    incl = excl + arr[i]
    
    # If not choose current element, find max between incl and previous excl
    excl = max(prev_incl, excl)
    
  return max(incl, excl)

# Test
arr1 = [5, 3, 2, 10, 7]
arr2 = [7, 7, 19, 11, 19, 7, 7]
print(max_sum_non_adjacent(arr1))  # Kết quả: 13
print(max_sum_non_adjacent(arr2))  # Kết quả: 10