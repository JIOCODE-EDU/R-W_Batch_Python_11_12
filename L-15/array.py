# Q.1 Array length calculate without using len() built-in function

size = int(input("Enter array size :"))

arr = []

print("Enter array Element : ")

for i in range(size):
  val = int(input(f"arr[{i}] = "))
  arr.append(val)


# check menually length

length = 0

for _ in arr:
  length += 1

print(length)


# Q.2 Calculate size of array and it's average.

size = int(input("Enter size of array : "))

arr = []

print("Enter array Element : ")

for i in range(size):
  val = int(input(f"arr[{i}] = "))
  arr.append(val)

# calculate array of length and average value.

length = 0
total = 0

for val in arr:
  length += 1
  total += val

average = total / length

print(average)
