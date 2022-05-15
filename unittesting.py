import unittest
from BPlusTreeV2 import BPlusTree
from main import SLinkedList, Node



class TestMain(unittest.TestCase):
    def test_agregar(self):
        agregar1 = SLinkedList(save = False)
        agregar1.agregar("TestString")
        self.assertEqual(agregar1.headval.dataval, "TestString" )

        agregar2 = SLinkedList(save = False)
        agregar2.agregar("Probando")
        self.assertEqual(agregar2.headval.dataval, "Probando" )

        agregar3 = SLinkedList(save = False)
        agregar3.agregar("Tomates")
        self.assertEqual(agregar3.headval.dataval, "Tomates" )
        

    
    def test_borrar(self):
        borrar1 = SLinkedList(save = False)
        borrar1.agregar("TestString")
        borrar1.borrar(0)
        self.assertEqual(borrar1.headval, None)

        borrar2 = SLinkedList(save = False)
        borrar2.agregar("Hola")
        borrar2.borrar(0)
        self.assertEqual(borrar2.headval, None)
    
    def test_rows(self):
        row1 = SLinkedList(save = False)
        row1.agregar("Hola")
        row1.agregar("Como")
        row1.agregar("Estas")
        row1.agregar("Hoy")
        self.assertEqual(len(row1.headval.dataval),4)

        row2 = SLinkedList(save = False)
        row2.agregar("Soy")
        row2.agregar("Estudiante")

        self.assertEqual(len(row2.headval.dataval),3)

    def test_listfind(self):
        find1= SLinkedList(save = False)
        find1.agregar("Tomate")
        find1.listfind("Tomate")
        self.assertEqual(find1.headval.dataval, "Tomate" )

        find2= SLinkedList(save = False)
        find2.agregar("Pan")
        find2.listfind("Pan")
        self.assertEqual(find2.headval.dataval, "Pan" )

    #  getNode() es un print
    #  listprint()es un print

    def test_listmodify(self):
        mod1 =SLinkedList(save = False)
        mod1.headval = Node(['Producto', 'Precio','Inventario'])
        mod1.headval.nextval = Node(['CAFE', 15,200])
        mod1.listmodify('CAFE',250,"Inventario")
        self.assertEqual(mod1.headval.nextval.dataval,['CAFE', 15,250])
        mod1.listmodify('CAFE',13,"Precio")
        self.assertEqual(mod1.headval.nextval.dataval,['CAFE', 13,250])
        mod1.listmodify('CAFE','COFFEE',"Producto")
        self.assertEqual(mod1.headval.nextval.dataval,['COFFEE', 13,250])

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

