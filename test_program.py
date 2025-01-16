import unittest
from inventory_cost import inventory_cost
from simulate_inventory import simulate_inventory


class TestInventoryManagement(unittest.TestCase):
    def test_inventory_cost(self):
        # Test pentru costul inventarului cu parametri simpli
        demand = [50, 60, 55]
        reorder_point = 40
        order_quantity = 100
        ordering_cost = 100
        holding_cost = 2
        shortage_cost = 5

        cost = inventory_cost(
            (reorder_point, order_quantity),
            demand,
            ordering_cost,
            holding_cost,
            shortage_cost
        )
        # Costul estimat manual
        # Calculul manual al costului estimat (920)
        expected_cost = 100  # Prima comanda
        expected_cost += 280  # Stocare (140 unitați in stoc la inceputul perioadei 1, 140*2 = 280)
        expected_cost += 180  # Stocare (90 unitati in stoc dupa perioada 2, 90*2 = 180)
        expected_cost += 100  # A doua comanda
        expected_cost += 260  # Stocare (130 unitati in stoc dupa perioada 3, 130*2 = 260)

        self.assertAlmostEqual(cost, expected_cost, delta=0.1)

    def test_simulate_inventory(self):
        # Test pentru simularea inventarului
        demand = [50, 60, 55]
        reorder_point = 40
        order_quantity = 100

        inventory_levels = simulate_inventory(demand, reorder_point, order_quantity)
        expected_levels = [140, 90, 130]  # Exemplu calculat manual
        self.assertEqual(inventory_levels, expected_levels)

    def test_edge_cases(self):
        # Test pentru cazuri limită
        demand = [0, 0, 0]
        reorder_point = 10
        order_quantity = 20
        #Desi stocul initial este 10, acesta creste la 30 in prima perioada deoarece
        #se face o comanda de 20 de unitați (pentru ca stocul a ajuns la punctul de reaprovizionare, 10).

        #In urmatoarele perioade, cererea fiind 0, stocul nu se reduce si nu mai sunt necesare comenzi suplimentare, deoarece inventarul ramane constant la 30.

        inventory_levels = simulate_inventory(demand, reorder_point, order_quantity)
        expected_levels = [30, 30, 30]  # Inventarul rămâne constant
        self.assertEqual(inventory_levels, expected_levels)

    def test_no_restock(self):
        # Test pentru scenariul în care nu e nevoie de reaprovizionare
        demand = [10, 20, 30]
        reorder_point = 50
        order_quantity = 0

        inventory_levels = simulate_inventory(demand, reorder_point, order_quantity)

        #Perioada 1: Stocul initial este 50, cererea este 10, deci stocul scade la 40.
        #Perioada 2: Stocul ramane la 40, cererea este 20, deci stocul scade la 20.
        #Perioada 3: Stocul ramane la 20, dar cererea este 30, deci se epuizeaza complet stocul si devine 0.
        expected_levels = [50, 40, 20]
        self.assertEqual(inventory_levels, expected_levels)


if __name__ == "__main__":
    unittest.main()
