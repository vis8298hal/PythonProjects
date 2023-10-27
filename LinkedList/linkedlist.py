import time
from node import Node
class LinkedList:
    """To Create a LinkedList from Values provided

    Attributes:
        head        -->    The First Value of Linked List (Smallest Value)
        node_cnt    -->    The total node count in the Linked List
    
    Methods:
        insert      -->    The Method to insert value to Linked List.
        find_node   -->    The Method to find a node in the Linked List.
        delete_node -->    The Method to delete a node from the Linked List. 

    """
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, value):
        """Method to Insert Values to Linked List one value at a time
        Syntax:
            insert(value)  ==> Where Value refers to the value of node 
                            value = Node.value
            ==> Values should be of the same datatype when Inserting.
            ==> Inserting values in ascending order to the linked list.
            ==> If head value is greater than parameter value then shift the head value rightward and insert parameter value as head value and head.next = new element in linked list.

        """
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
        elif self.head.value >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            prev_node = self.head
            runner_node = self.head.next_node
            
            while (runner_node is not None) and (value > runner_node.value):
                prev_node = runner_node
                runner_node = runner_node.next_node
            self.tail = runner_node
            new_node.next_node = runner_node
            prev_node.next_node = new_node

    def find_node(self, target):
        """To find a node in the linked List
        Syntax:
            find_node(target)  ==> target is the value of node you want to find out.

        ==> Returns False if Linked List is not having the given parameter value as a node value.
        ==> Returns True if Linked List contains given target value.
        """
        runner = self.head
        while runner is not None:
            if runner.value == target:
                return True
            else:
                runner = runner.next_node
        return False
    
    def delete_node(self, target):
        """To Delete the fetched node in the Linked List
        Syntax:
            delete_node(target)  ==> target is the value of node you want to delete.

        ==> Returns True if Node is Removed and synced.
        ==> Returns False if Linked List is empty.
        """
        if self.head is None:
            return False
        elif self.head.value == target:
            self.head = self.head.next_node
            return True
        else:
            prev = self.head
            runner = self.head.next_node
            while (runner is not None) and (target > runner.value):
                previous = runner
                runner = runner.next_node
            if (runner is not None) and (runner.value == target):
                previous.next_node = runner.next_node
                return True
            else:
                return False
          
    def __str__(self):
        str1 = ""
        if self.head is None:
            str1 = "List is Empty"
        else:
            runner = self.head
            while runner is not None:
                str1 += f"{runner.value}  "
                runner = runner.next_node
            str1 += "\n"
        return str1
    
    def __len__(self):
        self.node_cnt =  self.__count_nodes(self.head)
        return self.node_cnt
        
    def __count_nodes(self, node):
        """To Count nodes from the Current Node
        Syntax:
            __count_nodes(node)  ==> returns the count of nodes from the current node
        
        ==> Returns 0 If Linked List is empty.
        ==> Returns count of nodes from the node in parameter.
        ==> For Complete Linked list node is head of the linked list.
        """
        if node is None:
            return 0
        else:
            time.sleep(0.01)
             
            return 1 + self.__count_nodes(node.next_node)
        
            