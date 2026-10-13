#Напишите функцию, которая принимает на вход два вектора (2 списка) и рассчитывает косинусное расстояние 
#полученных векторов и выводит результат вычисления в консоль. Реализуйте проверку для валидности расчета 
#косинусного расстояния между 2-мя векторами, в случае если проверка не прошла, вывести в консоль причину 
#почему рассчитать расстояние между 2-мя векторами невозможно.

def cos_dist(vec1, vec2):
    if isinstance(vec1, list) and isinstance(vec2, list):
        ln1 = len(vec1)
        ln2 = len(vec2)
          
        ln = min(ln1, ln2)
        
        sc_ml = 0
        for i in range(0, ln-1):
            sc_ml += vec1[i] * vec2[i]

        norm1 = 0
        for j in range(0, ln1- 1):
            norm1 += vec1[j] ** 2
        norm1 = norm1 ** 0.5

        norm2 = 0
        for k in range(0, ln2 - 1):
            norm2 += vec2[k] ** 2
        norm2 = norm2 ** 0.5
        
        if norm1 == 0:
            print("Длинна первого вектора нулевая")
            return -1.0

        if norm2 == 0:
            print("Длинна второго вектора нулевая")
            return -1.0

        c_s = sc_ml / (norm1 * norm2)

        c_sub = 1.0 - c_s
        return c_sub

    print("Данные, поданные на вход, не вектор")
    return -1.0

s1 = [1, 2, 3, 4, 5, 6]
s2 = [7, 8, 9, 10]

print(f"{cos_dist(s1, s2)}")