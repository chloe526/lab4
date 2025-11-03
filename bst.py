import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

BinTree : TypeAlias = Union['BTNode', None]
@dataclass(frozen=True)
class BTNode():
    value: Any
    left: BinTree
    right: BinTree

class BST:
    comes_before : Callable[[Any,Any],bool]
    tree : BinTree

# returns true if 'tree' is empty, false otherwise
def is_empty(tree : BST) -> bool:
    if tree is None:
        return True
    return False 

# returns BST with 'val' added to 'tree' 
def helper_insert(tree : BinTree, new_val: Any, comes_before : Callable[[Any,Any],bool]) -> BST:
    match tree:
        case None:
            return BTNode(new_val, None, None)
        case BTNode(v, l, r):
            if comes_before(new_val, v): #new-val comes before 
                return BTNode(v, helper_insert(l, new_val, comes_before), r)
            else: #new-val comes after
                return BTNode(v, l, helper_insert(r, new_val, comes_before))

def insert(tree_input : BST, val: Any) -> BST:
    return helper_insert(tree_input.tree, val, tree_input.comes_before) 
        
def helper_lookup(tree: BinTree, new_val: Any, comes_before : Callable[[Any, Any], bool]):
    match tree:
        case None:
            return False
        case BTNode(v, l, r):
            if comes_before(new_val, v): #new_val comes before v
                return helper_lookup(l, new_val, comes_before)
            if comes_before(v, new_val):
                return helper_lookup(r, new_val, comes_before)
            else:
                return True

# returns True if 'val' already in 'BST', False if not
def lookup(tree_input : BST, val: Any) -> bool:
    helper_lookup(tree_input.tree, val, tree_input.comes_before)

def highest_value( bst : BST ) -> int:
    match bst:
        case None:
            raise ValueError( "Called on empty bst." )
        case BTNode( v, l, r ):
            if r is None:
                return v
            else:
                return highest_value( r )

# Delete the highest value from non-empty 'bst'.
def delete_highest_value( bst : BST ) -> BST:
    match bst:
        case None:
            raise ValueError( "Called on empty bst." )
        case BTNode( v, l, r ):
            if r is None:
                return l
            else:
                return BTNode( v, l, delete_highest_value( r ) )

def delete_root( bst : BST ) -> BST:
    match bst:
        case None:
            return None
        case BTNode( v, l, r ):
            if l is None:
                return r
            else:
                left_max : int = highest_value( l )
                new_left_subtree : BST = delete_highest_value( l )
                return BTNode( left_max, new_left_subtree, r )  

def helper_delete(tree: BinTree, new_val: Any, comes_before : Callable[[Any, Any], bool]) -> BST:
    match tree:
        case None:
            return tree
        case BTNode(v, l, r):
            if v == new_val:
                return delete_root(tree)
            if comes_before(new_val, v): #new_val comes before v
                return BTNode(v, helper_delete(l, new_val, comes_before), r)
            if comes_before(v, new_val):
                return BTNode(v, l, helper_lookup(r, new_val, comes_before))

# removes 'val' from 'BST
def delete(tree_input: BST, val: Any) -> BST:
    if lookup(tree_input, val):
        return helper_delete(tree_input.tree, val, tree_input.comes_before)
    else:
        return tree_input 
