from turtle import pos
from typing import Hashable
import unittest
from BPlusTreeV2 import BPlusTree
from main import SLinkedList, Node
from MaxHeap import MaxHeap




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

        
        
    # def test_agregar(self):
    #     agregar1 = SLinkedList(save = False)
    #     agregar1.agregar("TestString")
    #     self.assertEqual(agregar1.headval.dataval, "TestString" )

    #     agregar2 = SLinkedList(save = False)
    #     agregar2.agregar("Probando")
    #     self.assertEqual(agregar2.headval.dataval, "Probando" )

    #     agregar3 = SLinkedList(save = False)
    #     agregar3.agregar("Tomates")
    #     self.assertEqual(agregar3.headval.dataval, "Tomates" )
        

    
    # def test_borrar(self):
    #     borrar1 = SLinkedList(save = False)
    #     borrar1.agregar("TestString")
    #     borrar1.borrar(0)
    #     self.assertEqual(borrar1.headval, None)

    #     borrar2 = SLinkedList(save = False)
    #     borrar2.agregar("Hola")
    #     borrar2.borrar(0)
    #     self.assertEqual(borrar2.headval, None)
    
    # def test_rows(self):
    #     row1 = SLinkedList(save = False)
    #     row1.agregar("Hola")
    #     row1.agregar("Como")
    #     row1.agregar("Estas")
    #     row1.agregar("Hoy")
    #     self.assertEqual(len(row1.headval.dataval),4)

    #     row2 = SLinkedList(save = False)
    #     row2.agregar("Soy")
    #     row2.agregar("Estudiante")

    #     self.assertEqual(len(row2.headval.dataval),3)

    # def test_listfind(self):
    #     find1= SLinkedList(save = False)
    #     find1.agregar("Tomate")
    #     find1.listfind("Tomate")
    #     self.assertEqual(find1.headval.dataval, "Tomate" )

    #     find2= SLinkedList(save = False)
    #     find2.agregar("Pan")
    #     find2.listfind("Pan")
    #     self.assertEqual(find2.headval.dataval, "Pan" )

    # #  getNode() es un print
    # #  listprint()es un print

    # def test_listmodify(self):
    #     mod1 =SLinkedList(save = False)
    #     mod1.headval = Node(['Producto', 'Precio','Inventario'])
    #     mod1.headval.nextval = Node(['CAFE', 15,200])
    #     mod1.listmodify('CAFE',250,"Inventario")
    #     self.assertEqual(mod1.headval.nextval.dataval,['CAFE', 15,250])
    #     mod1.listmodify('CAFE',13,"Precio")
    #     self.assertEqual(mod1.headval.nextval.dataval,['CAFE', 13,250])
    #     mod1.listmodify('CAFE','COFFEE',"Producto")
    #     self.assertEqual(mod1.headval.nextval.dataval,['COFFEE', 13,250])

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

