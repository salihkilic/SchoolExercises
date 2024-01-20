class Stack:
    def __init__(self):
        self.content = []

    def pop(self):
        item = self.content[-1]
        self.content = self.content[0:-1]
        print(f"Removing item: {item} -- Updated Stack: {self.content}")
        return item

    def push(self, item):
        self.content = self.content + [item]
        print(f"Added: {item} -- Updated Stack: {self.content}")


if __name__ == '__main__':
    stack = Stack()

    print("\nAdding items")
    stack.push("1")
    stack.push("2")
    stack.push("3")

    print("\nRemoving Items")
    item1 = stack.pop()
    item2 = stack.pop()
    item3 = stack.pop()


