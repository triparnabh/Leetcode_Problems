class Node:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        # 1 & 2: Allocate the Node &
        #     Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node



    def findMiddle(self):

        lst = []
        temp = self.head
        while temp:
            lst.append(temp.data)
            temp = temp.next
        return lst[len(lst)//2]




if __name__=='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)

    result = llist.findMiddle()
    print(result)

