#Напишите функцию на языке Python, которая принимает целочисленный список и возвращает новый список 
#(без дубликатов), содержащий только чётные числа из исходного списка, отсортированные по убыванию.

def list_remake(income):
    if isinstance(income, list):
        buf_set = set()
        buf_list = list()
        for ch in income:
            if (isinstance(ch, int) and (ch % 2 == 0)):
                buf_set.add(ch)
        buf_list.extend(buf_set)
        
        n = len(buf_list)
        for i in range(n - 1):
            fl = False
            for j in range(n - 1 - i):
                if buf_list[j] < buf_list[j + 1]:
                    buf_list[j], buf_list[j + 1] = buf_list[j + 1], buf_list[j]
                    fl = True
            if not fl:
                break
        return buf_list
    else:
        print("Поступившие в функцию данне не список")
    return income

lst = [1, 'd', 0, -4, 5.7, 8, 6, 3]
print(list_remake(lst))


