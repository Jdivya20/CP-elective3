"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if current:
            while True:
                current = current.next
            current.next = new_element
        else:
            current = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            deleted_ele = self.head
            self.head=deleted_ele.next
            return deleted_ele
        else:
            return None
    def display(self):
        current=self.head
        while current!=None:
            print(current.value)
            current=current.next

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        return self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
    def display(self):
        return self.ll.display()
s=stack()
e1=Element(1)
e2=Element(2)
e3=Element(3)
e4=Element(4)
e5=Element(5)
s.push(e1)
s.push(e2)
s.push(e3)
s.push(e4)
s.push(e5)
s.display()