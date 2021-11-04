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

    def append(self, data: Any) -> None:
        new_node = Node(data)
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

    # POP MA USUNAC I ZWROCIC PIERWSZY ELEMENT, NIE TYLKO JEGO WARTOSC, ALE W ASSERCIE JEST VALUE, WIEC 2 GOTOWE FUNKCJE
    # DLA PONIZSZEJ TRZEBA ZMIENIC ASSERT ABY BYŁO ,,   assert first_element == returned_first_element   ''
    # def pop(self) -> Any:
    #     if self.head == 0:
    #         return 0
    #     removed = self.head
    #     self.head = self.head.next
    #     return removed

    def pop(self) -> Any:
        if self.head == 0:
            return 0
        removed = self.head
        removed.data = self.head.data
        self.head = self.head.next
        return removed.data

    # TO SAMO CO WYZEJ, ASSERT TU NALZEY ZMIENIC NA : ,,  assert last_element == returned_last_element   ''
    # def remove_last(self) -> Any:
    # if self.head == 0:
    #     return 0
    #     temp = self.head
    #     while temp.next.next is not None:
    #         temp = temp.next
    #     self.tail = temp
    #     temp.next = None
    #     return temp

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


# TEST DLA LISTY
list1 = LinkedList()
assert list1.head == None


# TEST DLA PUSH
list1.push("1")
list1.push("0")
assert str(list1) == '0 -> 1'


# TEST DLA APPEND
list1.append("9")
list1.append("10")
assert str(list1) == '0 -> 1 -> 9 -> 10'


# TEST DLA INSERT
middle_node = list1.node(at=1)
list1.insert(5, after=middle_node)
assert str(list1) == '0 -> 1 -> 5 -> 9 -> 10'


# TEST DLA POP
first_element = list1.node(at=0)
returned_first_element = list1.pop()
assert first_element.data == returned_first_element  # metoda pop ma zwracac i usuwac pierwszy element z listy, zapasowa
                                                    # funkcja wyzej

# TEST DLA REMOVE_LAST
last_element = list1.node(at=2)
returned_last_element = list1.remove_last()
assert last_element.data == returned_last_element
assert str(list1) == '1 -> 5 -> 9'


# TEST DLA REMOVE
second_node = list1.node(at=1)
list1.remove(second_node)
assert str(list1) == '1 -> 5'


# TEST DLA PRINT
print("\nLIST 1 : ")
print(list1)


# TEST DLA __LEN__
print("\nLENGTH OF LIST 1 : ")
print(len(list1))


# TEST DLA PUSTEJ LISTY
print("\n")
list2 = LinkedList()
print(str(list2))


# PRZYKŁADY DLA PUSH,APPEND,INSERT,POP,REMOVE,REMOVE_LAST
list1.push("PUSH")
print("\nLIST 1 AFTER PUSHING FIRST NODE : ")
print(list1)
list1.append("APPEND")
print("\nLIST 1 AFTER APPEND AT THE END OF THE LIST : ")
print(list1)
list1.insert("INSERT", after=list1.node(at=1))
print("\nLIST 1 AFTER INSERT AFTER NODE WITH INDEX OF 1 : ")
print(list1)
list1.pop()
print("\nLIST 1 AFTER REMOVING FIRST NODE ( POP ) : ")
print(list1)
list1.remove(list1.node(at=2))
print("\nLIST 1 AFTER REMOVING NODE AFTER NODE WITH INDEX OF 2 : ")
print(list1)
list1.remove_last()
print("\nLIST 1 AFTER REMOVING LAST NODE : ")
print(list1)
