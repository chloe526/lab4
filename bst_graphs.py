import sys
import unittest
from typing import *
from dataclasses import dataclass
import math 
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)
from bst import *
import time

TREES_PER_RUN : int = 10000

# def example_graph_creation() -> None:
# # Return log-base-2 of 'x' + 5.

#     def f_to_graph( x : float ) -> float:
#         return math.log2( x ) + 5.0
    
#     # here we're using "list comprehensions": more of Python's
#     # syntax sugar.
#     x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
#     y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
    
#     # Could have just used this type from the start, but I want
#     # to emphasize that 'matplotlib' uses 'numpy''s specific array
#     # type, which is different from the built-in Python array
#     # type.
#     x_numpy : np.ndarray = np.array( x_coords )
#     y_numpy : np.ndarray = np.array( y_coords )

#     plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.title("Example Graph")
#     plt.grid(True)
#     plt.legend() # makes the 'label's show up
#     plt.show()

def height_tree(bst : BTNode) -> BTNode:
    if bst is None:
        return 0

    match bst:
        case None:
            return 0
        case BTNode(v, l, r):
            return 1 + max(height_tree(l), height_tree(r))
   
def avg_height(n) -> float:

    if n<=0:
        return 0.0
    tot_height = 0
    
    for _ in range(TREES_PER_RUN):
        rand_tree = random_tree(n)
        tot_height += height_tree(rand_tree.tree)
     
    return tot_height / TREES_PER_RUN


def random_tree(n: int) -> BST:
    def comes_before_float(a: float, b: float): 
        return a < b

    bst = BST(comes_before_float, None)

    for _ in range(n):
        bst = insert(bst, random.random())
        
    return bst

def random_tree_graph() -> None:
# Return log-base-2 of 'x' + 5.
    
    
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[int] = [ int(i) for i in range( 1, 100, 2) ]
    y_coords : List[float] = [ avg_height( x ) for x in x_coords ]
    
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )

    plt.plot( x_numpy, y_numpy, label = 'avg height of 10,000 random trees of size n.' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Average Tree Height")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

def insert_tree(bst: BTNode, val: int) -> BST:
    match bst:
        case None:
            return BTNode(val, None, None)
        case BTNode(v, l, r):
            if int == v:
                return bst
            if int < v:
                return BTNode(v, insert_tree(l, val), r)
            if int > v:
                return BTNode(v, l, insert_tree(r, val))

def time_insert_random_tree(n: int) -> None:
    start = time.time()
    for _ in range(TREES_PER_RUN): #number of trees
        tree = random_tree(n) #size n in each tree
        sorted_tree = insert_tree(tree.tree, random.random)  # or tree.root if your field is different
    end = time.time()
    return end - start


def insert_random_tree_graph() -> None:
# Return log-base-2 of 'x' + 5.
    
    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[int] = [ int(i) for i in range( 1, 50 ) ]
    y_coords : List[float] = [ avg_height( x ) for x in x_coords ]
    
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )

    plt.plot( x_numpy, y_numpy, label = 'time to insert value in random trees' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Insertion Time ")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

if (__name__ == '__main__'):
    # random_tree_graph()
    # start = time.time()
    # avg_height(80)
    # end = time.time()

    # print(end - start)
    insert_random_tree_graph()
