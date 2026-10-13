'''
Реализуйте стек (LIFO — Last In, First Out), используя синтаксис языка Python и односвязный список. 
Вам необходимо создать классы Node и Stack, которые будут представлять эту структуру данных.
Стек должен хранить элементы в порядке их добавления, но извлекать их в обратном порядке: 
последний добавленный элемент извлекается первым.

Требования к реализации:
Создайте класс Node, который будет хранить:
значение (value);
ссылку на следующий узел (next).

Создайте класс Stack, который будет управлять стеком и содержать:
ссылку на верхний элемент стека (top);
количество элементов (опционально, но желательно).
Реализуйте следующие методы в классе Stack:
push(value) — добавляет элемент на вершину стека.
pop() — удаляет и возвращает элемент с вершины стека. Если стек пуст, выбрасывает исключение IndexError.
peek() — возвращает значение верхнего элемента без его удаления. Если стек пуст, выбрасывает исключение IndexError.
is_empty() — возвращает True, если стек пуст, иначе False.
Важно: нельзя использовать встроенные списки Python (list) или другие контейнеры (collections.deque и т.п.) 
для хранения данных внутри стека. Вся логика должна быть реализована через ваш собственный связный список.
'''

class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
       new_node = Node(value)
       new_node.next = self.top
       self.top = new_node
       self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Ошибка при удалении: стек пустой")
        poped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return poped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Ошибка отображения верхнего элемента: стек пустой")
        return self.top.value

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.size

    def __repr__(self):
        current = self.top
        ret_str = ""
        while current:
            ret_str += str(current.value)
            ret_str += " | "
            current = current.next
        return ret_str + " TOP"


obj1 = '1'
obj2 = '2'
obj3 = '3'

stack = Stack()
stack.push(obj1)
stack.push(obj2)
stack.push(obj3)

print(stack)  
print(stack.peek()) 
print(stack.pop())  
print(stack)  
print(len(stack)) 