from typing import List
from typing import Any

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.tail = new_node
        new_node.next = self.head
        self.head = new_node

    def node(self, at: int) -> Node:
        temp = self.head
        if temp is None:
            return None
        for i in range(at):  # powinno byc raczej at-1, wtedy zwroci wezeł o odpowiednim indeksie
            temp = temp.next
        return temp

    def pop(self) -> Any:
        if self.head == 0:
            return 0
        removed = self.head
        removed.data = self.head.data
        self.head = self.head.next
        return removed.data

    def __str__(self) -> str:
        temp = self.head
        temp_list = ""
        if temp is None:
            print("List is empty")
        while temp is not None:
            if temp.next is not None:
                temp_list = temp_list + str(temp.data) + ' -> '  # do ogona dodaje strzalke
            else:
                temp_list = temp_list + str(temp.data)  # dla ogona nie dodaje strzalki
            temp = temp.next
        return temp_list

    def __len__(self) -> int:
        current = self.head
        sum_len = 0
        if current is None:
            return 0
        while current is not None:
            sum_len = sum_len + 1
            current = current.next
        return sum_len


class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def push(self, data: Any) -> None:
        self._storage.push(data)

    def pop(self):
        return self._storage.pop()  # zwrocenie po prostu funkcji pop

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        temp_stack = ""
        if self._storage is None:
            print("Stack is empty")
        for i in range(len(self._storage)):
            temp_stack = temp_stack + "| " + str(self._storage.node(i).data) + " |\n"
        return temp_stack


# TEST DLA STACK
stack = Stack()
assert len(stack) == 0


# TEST DLA PUSH
stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
print("STACK : ")
print(stack)

# TEST DLA SZCZYTOWEJ WARTOSCI ( TA, KTORA STOI NA GORZE )
top_value = stack.pop()
assert top_value == 1
print("STACK AFTER REMOVING VALUE FROM PEAK: ")
print(stack)

# Dlugosc stosu po zdjęciu szczytowego elementu ma wartość 2
assert len(stack) == 2

