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

    def append(self, element: Any) -> None:
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    def node(self, at: int) -> Node:
        temp = self.head
        if temp is None:
            return None
        for i in range(at):  # powinno byc raczej at-1, wtedy zwroci wezeł o odpowiednim indeksie
            temp = temp.next
        return temp

    def insert(self, data: Any, after: Node) -> None:
        if after is None:
            print("There is no such node in this linkedList")
            return None
        new_node = Node(data)
        if after == self.tail:
            after.next = new_node
            self.tail = new_node
        new_node.next = after.next
        after.next = new_node

    def pop(self) -> Any:
        if self.head == 0:
            return 0
        removed = self.head
        removed.data = self.head.data
        self.head = self.head.next
        return removed.data

    def remove_last(self) -> Any:
        if self.head == 0:
            return 0
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        self.tail = temp
        temp.next = None  # ustawienie nastepnika na 0, koniec listy
        return temp.data

    def remove(self, after: Node) -> None:
        if after is None:
            print("There is no such node in this linkedList")
            return None
        else:
            self.tail = after
            after.next = None

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


class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def peek(self) -> Any:
        if self._storage == 0:
            return 0
        return self._storage.head.data

    def enqueue(self, element: Any) -> None:
        return self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __len__(self) -> int:
        return len(self._storage)

    def __str__(self) -> str:
        temp_queue = ""
        if self._storage is None:
            print("Queue is empty")
        for i in range(len(self._storage)):
            if i == len(self._storage) - 1:
                temp_queue = temp_queue + str(self._storage.node(i).data) # dla ostatniego elementu - brak przecinka
            else:
                temp_queue = temp_queue + str(self._storage.node(i).data) + ", "
        return temp_queue

# UTWORZENIE KOLEJKI FIFO
queue = Queue()

# TEST DLA PUSTEJ KOLEJKI FIFO
assert len(queue) == 0

# TEST DLA ENQUEUE
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

# TEST DLA PRINT
assert str(queue) == 'klient1, klient2, klient3'
print("KOLEJKA FIFO :")
print(queue)

# TEST DLA DEQUEUE
# Jako pierwszy zostanie obsłużony klient 1.Po "obsłużeniu" pierwszej osoby w kolejce zostaną elementy klient2 i klient3
client_first = queue.dequeue()
print("\nKOLEJKA FIFO PO OBSLUZENIU KLIENTA NR.1 :")
print(queue)
assert client_first == 'klient1'

# TEST DLA PRINT NR.2
assert str(queue) == 'klient2, klient3'

# TEST DLA LEN
assert len(queue) == 2

# DODANIE KOLEJNYCH ELEMENTOW
queue.enqueue('klient4')
queue.enqueue('klient5')
queue.enqueue('klient6')
queue.enqueue('klient7')
queue.enqueue('klient8')
queue.enqueue('klient9')
queue.enqueue('klient10')
queue.enqueue('klient11')
queue.enqueue('klient12')

print("\nKOLEJKA FIFO PO DODANIU KOLEJNYCH KLIENTOW :")
print(queue)

print("\nKOLEJKA FIFO PO OBSLUZENIU KLIENTA NR.2, NR.3, NR.4, NR.5 :")
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
print(queue)
