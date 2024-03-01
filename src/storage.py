from main_game import * 
from gen import * 

class node(object):
    def __init__(self,data,parent):
        self.data = data
        self.children = []
        self.parent = parent
    def add_child(self,child):
        self.children.append(child)

intial_state = generate
moves = generate_moves(intial_state)

head = node(intial_state,intial_state); 
for m in moves:
    head.add_child(m)