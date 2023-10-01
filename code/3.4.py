"""
实现一个链表，使其能完成增删改查的工作
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def update(self, old_data, new_data):
        node_to_update = self.find(old_data)
        if node_to_update:
            node_to_update.data = new_data

# 创建一个新的链表
my_linked_list = LinkedList()

# 添加元素到链表
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# 显示链表内容
print("链表内容:")
my_linked_list.display()

# 查找节点
search_data = 2
found_node = my_linked_list.find(search_data)
if found_node:
    print(f"查找到节点 {search_data}")

# 删除节点
delete_data = 2
my_linked_list.delete(delete_data)
print(f"删除节点 {delete_data} 后的链表:")
my_linked_list.display()

# 更新节点
old_data = 1
new_data = 10
my_linked_list.update(old_data, new_data)
print(f"更新节点 {old_data} 为 {new_data} 后的链表:")
my_linked_list.display()
