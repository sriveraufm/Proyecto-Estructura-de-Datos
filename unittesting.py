from turtle import pos
from typing import Hashable
import unittest
from BPlusTreeV2 import BPlusTree
from MaxHeap import MaxHeap
from hashtable import HashTable




class TestMain(unittest.TestCase):

    def test_parent(self):
        parent1 = MaxHeap(9)
        parent1.parent(6)
        self.assertEqual(parent1.parent(6), 6//2 )
        parent1.parent(71)
        self.assertEqual(parent1.parent(71), 71//2 )
        parent1.parent(39)
        self.assertEqual(parent1.parent(39), 39//2 )
        parent1.parent(8)
        self.assertEqual(parent1.parent(8), 8//2 )

    def test_leftChild(self):
        parent1 = MaxHeap(9)
        parent1.leftChild(9)
        self.assertEqual(parent1.leftChild(9), 9*2 )
        parent1.leftChild(15)
        self.assertEqual(parent1.leftChild(15), 15*2 )
        parent1.leftChild(2)
        self.assertEqual(parent1.leftChild(2), 2*2 )
        parent1.leftChild(-4)
        self.assertEqual(parent1.leftChild(-4), -4*2 )

    def test_rightChild(self):
        child1 = MaxHeap(9)
        child1.rightChild(4)
        self.assertEqual(child1.rightChild(4), (4*2)+1 )
        child1.rightChild(8)
        self.assertEqual(child1.rightChild(8), (8*2)+1 )
        child1.rightChild(27)
        self.assertEqual(child1.rightChild(27), (27*2)+1 )
        child1.rightChild(-2)
        self.assertEqual(child1.rightChild(-2), (-2*2)+1 )

    def test_insert(self):
        ins1=MaxHeap(9)
        ins1.insert({'ID': 'id3','TOTAL': 10})
        self.assertEqual(ins1.size,1)
        ins1.insert({'ID': 'id8','TOTAL': 80})
        self.assertEqual(ins1.size,2)
        ins1.insert({'ID': 'id90','TOTAL': 32})
        self.assertEqual(ins1.size,3)
    
    def test_delete(self):
        del1 = MaxHeap(9)
        del1.insert({'ID': 'id3','TOTAL': 10})
        del1.delete ('id3')
        self.assertEqual(del1.size,0)

        del1.insert({'ID': 'id5','TOTAL': 4})
        del1.insert({'ID': 'id13','TOTAL': 7})
        del1.insert({'ID': 'id7','TOTAL': 18})
        del1.insert({'ID': 'id6','TOTAL': 25})
        del1.delete ('id5')
        self.assertEqual(del1.size,3)

    def test_setVal(self):
        set1=HashTable(7)
        set1.set_val('ejemplo@example.com', 'some other value')
        self.assertEqual(set1.get_val('ejemplo@example.com'),'some other value')
        set1.set_val('clon@example.com', 'valor')
        self.assertEqual(set1.get_val('clon@example.com'),'valor')
        set1.set_val('perro@gato.com', 'some value')
        self.assertEqual(set1.get_val('perro@gato.com'),'some value')
        set1.set_val('ejemplo@pez.com', 'some other values')
        self.assertEqual(set1.get_val('ejemplo@pez.com'),'some other values')

    def test_delVal(self):
        del1=HashTable(7)
        del1.set_val('ejemplo@example.com', 'some other value')
        del1.set_val('clon@example.com', 'valor')
        del1.set_val('perro@gato.com', 'some value')
        del1.delete_val('ejemplo@example.com')
        self.assertEqual(del1.get_val('ejemplo@example.com'),'No record found')
        self.assertEqual(del1.get_val('clon@example.com'),'valor')
        del1.delete_val('clon@example.com')
        self.assertEqual(del1.get_val('clon@example.com'),'No record found')

    def test_arbol(self):
        arb = BPlusTree()
        arb.insert("P","Prueba")
        self.assertEqual(arb.retrieve('P'), ['Prueba'])
        arb.insert("C","Compu")
        self.assertEqual(arb.retrieve('C'), ['Compu'])
        arb.insert("O","Oso")
        self.assertEqual(arb.retrieve('O'), ['Oso'])
        arb.insert("H","Hola")
        self.assertEqual(arb.retrieve('H'), ['Hola'])

if __name__ == "__main__":
    unittest.main()

