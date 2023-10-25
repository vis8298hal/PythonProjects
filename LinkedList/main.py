from node import Node


node_d = Node("d",None)
node_c = Node("c",node_d)
node_b = Node("b",node_c)
node_a = Node("a",node_b)

print(node_a)
