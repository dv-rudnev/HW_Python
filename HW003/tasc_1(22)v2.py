# создал список значений
users_nums = [
    45,  # 0
    67,  # 1
    43,  # 2
    78,  # 3
    3,  # 4
    5,  # 5
]

# применил встроенную функцию "sum" к срезу списка, начинающегося с первого нечетного индекса и с шагом 2
print(f'Sum => {sum(users_nums[1::2])}')
