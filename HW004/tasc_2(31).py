# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7


from_user = int(input("Введите число: "))
temp = from_user
i = 2
prime_numbers = []
while i <= temp:
    if temp % i == 0:
        prime_numbers.append(i)
        temp //= i
    else:
        i += 1
print(from_user, '=>', prime_numbers)