# write a recursive function to calculate the sum of n natural numbers

def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(4)
print(sum)


####### write a recursive function print all elements in list.(USE list & index as parameter)

def print_list(list, idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx+1)             # recursive

fruits = ["mango", "litchi", "banana", "apple"]
print_list(fruits)