# N = int(input("Введите количество элементов: "))
# if N <= 0:
#     print("Не соотвестсвует условию")
# else:
#     A = [i for i in range(1, N + 1)]
#     print(*A)
#     X = int(input("Введите число: "))
#     V = 0
#     for i in range(len(A)):
#         if A[i] == X:
#             V += 1
#             print("Встечается", V, "раз")



# N = int(input("Введите воличество элементов: "))
# A = [i for i in range(1, N + 1)]
# print(*A)
# X = int(input("Введите число: "))
# min1 = 0
# min2 = 0
# for i in range(len(A)):
#     if X == A[i] + 1:
#         min1 = X - 1
#         print("Близжайший к числу элемент", "-", min1)
#     elif X > N + 1:
#         min2 = A[-1]
#         print("Близжайший к числу элемент", "-", min2)



# dict1 = {}
# dict1["AEIOULNSTRАВЕИНОРСТ"], dict1["DGДКЛМПУ"], dict1["BCMPБГЁЬЯ"], dict1["FHVWYЙЫ"], dict1["KЖЗХЦЧ"], dict1["jJXШЭЮ"], dict1["QZФЩЪ"] = 1, 2, 3, 4, 5, 8, 10
# word = str(input("Введите слово: ").upper())
# schet = 0
# for i in word:
#     for k, v in dict1.items():
#         if i in k:
#             schet += v
#             print("Ваш выйгрыш - ", schet)



    
    
