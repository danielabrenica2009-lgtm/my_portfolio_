class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def get_all(self):
        return self.items


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, value):
        curr = self.head
        if curr and str(curr.data) == str(value):
            self.head = curr.next
            return True
        prev = None
        while curr and str(curr.data) != str(value):
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
            return True
        return False

    def get_all(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

    def clear(self):
        self.head = None

    def insert_at_index(self, index, data):
        if index == 0:
            self.prepend(data)
            return True
        new_node = ListNode(data)
        curr = self.head
        curr_index = 0
        while curr and curr_index < index - 1:
            curr = curr.next
            curr_index += 1
        if curr:
            new_node.next = curr.next
            curr.next = new_node
            return True
        return False

    def search(self, value):
        curr = self.head
        index = 0
        while curr:
            if str(curr.data) == str(value):
                return index
            curr = curr.next
            index += 1
        return -1

    def pop_head(self):
        if not self.head:
            return None
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

    def pop_tail(self):
        if not self.head:
            return None
        if not self.head.next:
            popped_data = self.head.data
            self.head = None
            return popped_data
        curr = self.head
        while curr.next.next:
            curr = curr.next
        popped_data = curr.next.data
        curr.next = None
        return popped_data


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = Stack()
    output = []
    steps = []

    tokens = []
    current_token = ""
    for char in expression:
        if char.isspace():
            continue
        if char in "+-*/^()":
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
            current_token += char
    if current_token:
        tokens.append(current_token)

    for token in tokens:
        if token.isalnum():
            output.append(token)
            steps.append(f"Operand '{token}' added to output.")
        elif token == '(':
            stack.push(token)
            steps.append(f"Push '(' to stack.")
        elif token == ')':
            steps.append("Encountered ')', popping until '(' found.")
            while not stack.is_empty() and stack.peek() != '(':
                popped = stack.pop()
                output.append(popped)
                steps.append(f"Popped '{popped}' to output.")
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()
        else:
            steps.append(f"Processing operator '{token}'.")
            while (not stack.is_empty() and stack.peek() != '(' and
                   precedence.get(token, 0) <= precedence.get(stack.peek(), 0)):
                popped = stack.pop()
                output.append(popped)
                steps.append(f"Popped higher/equal precedence '{popped}' to output.")
            stack.push(token)
            steps.append(f"Pushed '{token}' to stack.")

    while not stack.is_empty():
        popped = stack.pop()
        output.append(popped)
        steps.append(f"Popped remaining '{popped}' from stack to output.")

    return "".join(output), steps


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def get_all(self):
        return self.items


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def get_all(self):
        return self.items