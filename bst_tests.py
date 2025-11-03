import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)

from bst import *


class BSTTests(unittest.TestCase):

    @dataclass(frozen=True)
    class Point2:
        x: int
        y: int

    #int
    def comes_before_int(self, a: int, b: int): 
        return a < b
    
    #string
    def comes_before_str(self, a: str, b: str): 
        a = a.lower()
        b = b.lower()
        return a < b
    
    #distance
    def comes_before_distance(self, A: Point2, B: Point2):
        distanceA = ((A.x)**2 + (A.y)**2) ** 0.5
        distanceB = ((B.x)**2 + (B.y)**2) ** 0.5

        return distanceA < distanceB


    def test_is_empty(self):
        test1 = BST(self.comes_before_int, None)
        self.assertEqual(is_empty(test1), True)

        test2 = BST(self.comes_before_int, BTNode(4, BTNode(3, None, None), BTNode(5, None, None)))
        self.assertEqual(is_empty(test2), False)

        test3 = BST(self.comes_before_str, BTNode("hi", None, None))
        self.assertEqual(is_empty(test3), False)

        test4 = BST(self.comes_before_distance, BTNode(self.Point2(3, 4), None, None))
        self.assertEqual(is_empty(test4), False)


    def test_insert(self):
        test1 = BST(self.comes_before_int, BTNode(4, BTNode(3, None, None), BTNode(5, None, None)))
        self.assertEqual(insert(test1, 2), 
                         BST(self.comes_before_int, BTNode(4, BTNode(3, BTNode(2, None, None), None), BTNode(5, None, None))))

        test2 = BST(self.comes_before_str, BTNode("c", BTNode("b", None, None), BTNode("d", None, None)))
        self.assertEqual(insert(test2, "e"), 
                         BST(self.comes_before_str, BTNode("c", BTNode("b", None, None), BTNode("d", None, BTNode("e", None, None)))))

        test3 = BST(self.comes_before_distance, BTNode(self.Point2(3, 4), BTNode(self.Point2(3,1), None, None), BTNode(self.Point2(3, 10), None, None)))
        self.assertEqual(insert(test3, self.Point2(5, 10)), 
                         BST(self.comes_before_distance, BTNode(self.Point2(3, 4), BTNode(self.Point2(3,1), None, None), BTNode(self.Point2(3, 10), None, BTNode(self.Point2(5, 10), None, None)))))

        test4 = BST(self.comes_before_int, None)
        self.assertEqual(insert(test4, 10), 
                         BST(self.comes_before_int, BTNode(10, None, None)))

    def test_lookup(self):
        test1 = BST(self.comes_before_int, BTNode(3, None, None))
        self.assertEqual(lookup(test1, 3), True)
        self.assertEqual(lookup(test1, 0), False)

        test2 = BST(self.comes_before_str, BTNode("c", BTNode("b", None, None), BTNode("d", None, None)))
        self.assertEqual(lookup(test2, "f"), False)
        self.assertEqual(lookup(test2, "b"), True)

        test3 = BST(self.comes_before_distance, BTNode(self.Point2(3, 4), BTNode(self.Point2(3,1), None, None), BTNode(self.Point2(3, 10), None, None)))
        self.assertEqual(lookup(test3, self.Point2(3,4)), True)
        self.assertEqual(lookup(test3, self.Point2(100,100)), False)

        test3 = BST(self.comes_before_distance, None)
        self.assertEqual(lookup(test3, self.Point2(3,4)), False)
        self.assertEqual(lookup(test3, self.Point2(100,100)), False)

    def test_delete(self):
        test1 = BST(self.comes_before_int, BTNode(3, None, None))
        self.assertEqual(delete(test1, 3), BST(self.comes_before_int, None))
        self.assertEqual(delete(test1, 0), BST(self.comes_before_int, BTNode(3, None, None)))

        test1 = BST(self.comes_before_int, BTNode(6, BTNode(4, BTNode(2, None, None), BTNode(5, None, None)), BTNode(7, None, None)))
        self.assertEqual(delete(test1, 4), BST(self.comes_before_int, BTNode(6, BTNode(2, None, BTNode(5, None, None)), BTNode(7, None, None))))
        self.assertEqual(delete(test1, 0), BST(self.comes_before_int, BTNode(6, BTNode(4, BTNode(2, None, None), BTNode(5, None, None)), BTNode(7, None, None))))

        test2 = BST(self.comes_before_str, BTNode("c", BTNode("b", None, None), BTNode("f", BTNode("d", None, None), BTNode("g", None, None))))
        self.assertEqual(delete(test2, "z"), BST(self.comes_before_str, BTNode("c", BTNode("b", None, None), BTNode("f", BTNode("d", None, None), BTNode("g", None, None)))))
        self.assertEqual(delete(test2, "f"), BST(self.comes_before_str, BTNode("c", BTNode("b", None, None), BTNode("d", None, BTNode("g", None, None)))))
    
        test3 = BST(self.comes_before_distance, BTNode(self.Point2(3, 4), 
                                                BTNode(self.Point2(3,1), 
                                                    BTNode(self.Point2(2,1), None, None), None),
                                                BTNode(self.Point2(3, 10), 
                                                    BTNode(self.Point2(3,9), None, None), 
                                                    BTNode(self.Point2(3,15), None, None))))
        self.assertEqual(delete(test3, self.Point2(3,4)), BST(self.comes_before_distance, BTNode(self.Point2(3, 1), 
                                                            BTNode(self.Point2(2,1), None, None),
                                                            BTNode(self.Point2(3, 10), 
                                                                BTNode(self.Point2(3,9), None, None), 
                                                                BTNode(self.Point2(3,15), None, None)))))
        self.assertEqual(delete(test3, self.Point2(100,100)), BST(self.comes_before_distance, BTNode(self.Point2(3, 4), 
                                                                BTNode(self.Point2(3,1), 
                                                                    BTNode(self.Point2(2,1), None, None), None),
                                                                BTNode(self.Point2(3, 10), 
                                                                    BTNode(self.Point2(3,9), None, None), 
                                                                    BTNode(self.Point2(3,15), None, None)))))

        test4 = BST(self.comes_before_distance, BTNode(self.Point2(3, 4), None, None))
        self.assertEqual(delete(test4, self.Point2(3,4)), BST(self.comes_before_distance, None))
        self.assertEqual(delete(test4, self.Point2(0,0)), BST(self.comes_before_distance, BTNode(self.Point2(3, 4), None, None)))

    
    
if (__name__ == '__main__'):
    unittest.main()