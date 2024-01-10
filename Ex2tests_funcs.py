import unittest
from Ex2funcs import FIFO 


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

if __name__ == '__main__':
    unittest.main()

