class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.head = False

class LinkedList:

    def __init__(self):
        self.node = Node(None)
        self.node.head = False

    def insert(self, data):
        if self.node.head == False and self.node.data == None: # empty
            self.node.data = data
            self.node.head = True
        else:
            new_node = Node(data)

            search_node = self.node
            while search_node.next != None:
                search_node = search_node.next
            search_node.next = new_node

    def delete(self, node_number):
        if self.node.head == False and self.node.data == None:  # empty
            return False
        elif self.node.head == True and node_number == 1:  # if, only one node
            self.node.data == None
            self.node.head == False
        else:
            index = 1
            search_node = self.node
            prev_node = None
            while search_node != None:

                if index == node_number:
                    if search_node.head == True: # if, first node
                        self.node = search_node.next
                        self.node.head = True
                        del search_node
                        break
                    else:  # if, not first node
                        link_node = search_node.next
                        prev_node.next = link_node
                        del search_node
                        break

                prev_node = search_node
                search_node = search_node.next
                index += 1

    def print(self):
        search_node = self.node
        while search_node != None:
            print(f"NODE DATA : [{search_node.data}]")
            search_node = search_node.next


ilist = LinkedList()
ilist.insert("data1")
ilist.insert("data2")
ilist.insert("data3")
ilist.insert("data4")

ilist.print()

print ("----------")

ilist.delete(2)
ilist.delete(3)
ilist.print()

