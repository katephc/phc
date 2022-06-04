num = int(input())
sum_nums = 0
while num != 0:
    last = num % 10
    sum_nums += last
    num = num // 10
print(sum_nums)
