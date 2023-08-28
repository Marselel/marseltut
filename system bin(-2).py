N = int(input("Введите число N: "))  # Запрос ввода числа

result = ""
if N == 0:
    result = "0"
else:
    while N != 0:
        remainder = N % -2
        if remainder == -1:
            result = "1" + result
            N = (N - 1) // -2
        else:
            result = str(remainder) + result
            N = N // -2

print(result)
