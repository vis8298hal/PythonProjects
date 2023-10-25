class Node:
    
    
    def __init__(self,data, next_node=None):
        self._value = data
        self._next_node = next_node
    
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

    def __str__(self):
        return f"{self._value} -->  {self._next_node}"

        
    