from log import Log
class Node:
    """Container of Data Value and Data Connection
    Attributes:
        * value         ==> Value of element.
        * next_node     ==> Reference to the next node.
        * logfile       ==> Logfile name for the Program.

    Syntax:
        Node(data,next_node) ==> next_node == Node(alpha,beta)
                                by default next_node is None
            data is the value to be stored into node.
    """
    
    def __init__(self,data, next_node=None):
        self._value = data
        self._next_node = next_node
        self.__logfile = "logfile.txt"
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value
    
    @property
    def next_node(self):
        return self._next_node
    
    @next_node.setter
    def next_node(self, new_next_node):
        self._next_node = new_next_node
        log = Log(self.__logfile)

    
        
    