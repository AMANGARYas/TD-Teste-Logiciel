import unittest
from Ex2funcs import FIFO 
from Ex2funcs import LIFO 


class TestFIFO(unittest.TestCase):

    def test_enqueue_dequeue(self):
        fifo = FIFO()
        self.assertIsNone(fifo.dequeue(), "La file doit être vide au début")

        fifo.enqueue(1)
        fifo.enqueue(2)
        fifo.enqueue(3)

        self.assertEqual(fifo.dequeue(), 1, "Le premier élément ajouté doit être le premier retiré")
        self.assertEqual(fifo.dequeue(), 2, "Le deuxième élément ajouté doit être le deuxième retiré")
        self.assertEqual(fifo.dequeue(), 3, "Le troisième élément ajouté doit être le troisième retiré")
        self.assertIsNone(fifo.dequeue(), "La file doit être vide après tous les défilements")

    def test_is_empty(self):
        fifo = FIFO()
        self.assertTrue(fifo.is_empty(), "La file doit être vide au début")

        fifo.enqueue(1)
        self.assertFalse(fifo.is_empty(), "La file ne doit pas être vide après l'enfilement")

        fifo.dequeue()
        self.assertTrue(fifo.is_empty(), "La file doit être vide après le défilement")



class TestLIFO(unittest.TestCase):

    def test_push_pop(self):
        lifo = LIFO()
        self.assertIsNone(lifo.pop(), "La pile doit être vide au début")

        lifo.push(1)
        lifo.push(2)
        lifo.push(3)

        self.assertEqual(lifo.pop(), 3, "Le dernier élément ajouté doit être le premier retiré")
        self.assertEqual(lifo.pop(), 2, "Le deuxième élément ajouté doit être le deuxième retiré")
        self.assertEqual(lifo.pop(), 1, "Le premier élément ajouté doit être le troisième retiré")
        self.assertIsNone(lifo.pop(), "La pile doit être vide après tous les dépilements")

    def test_is_empty(self):
        lifo = LIFO()
        self.assertTrue(lifo.is_empty(), "La pile doit être vide au début")

        lifo.push(1)
        self.assertFalse(lifo.is_empty(), "La pile ne doit pas être vide après l'empilement")

        lifo.pop()
        self.assertTrue(lifo.is_empty(), "La pile doit être vide après le dépilement")

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()

