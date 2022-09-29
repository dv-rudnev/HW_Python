# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x, y, z = int(input("Введите X: ")), int(input("Введите y: ")), int(input("Введите z: "))

print((not (x or y or z)) == (not x and not y and not z))