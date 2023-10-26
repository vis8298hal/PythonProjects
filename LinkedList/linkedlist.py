import time
from node import Node
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, value):
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
        runner = self.head
        while runner is not None:
            if runner.value == target:
                return True
            else:
                runner = runner.next_node
        return False
    
    def delete_node(self, target):
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
        if node is None:
            return 0
        else:
            time.sleep(0.01)
             
            return 1 + self.__count_nodes(node.next_node)
        
            