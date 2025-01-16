import unittest
from inventory_cost import inventory_cost
from simulate_inventory import simulate_inventory


class TestInventoryManagement(unittest.TestCase):
    def test_inventory_cost_simple_case(self):
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
        expected_cost = 900  # Corrected expected cost
        self.assertAlmostEqual(cost, expected_cost, delta=0.1)

    def test_simulate_inventory_simple_case(self):
        demand = [50, 60, 55]
        reorder_point = 40
        order_quantity = 100

        inventory_levels = simulate_inventory(demand, reorder_point, order_quantity)
        expected_levels = [100, 140, 85]  # Corrected expected levels
        self.assertEqual(inventory_levels, expected_levels)

    def test_inventory_cost_no_restock(self):
        demand = [10, 20, 30]
        reorder_point = 50
        order_quantity = 0
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
        expected_cost = 170  # Corrected expected cost
        self.assertAlmostEqual(cost, expected_cost, delta=0.1)

    def test_simulate_inventory_no_restock(self):
        demand = [10, 20, 30]
        reorder_point = 50
        order_quantity = 0

        inventory_levels = simulate_inventory(demand, reorder_point, order_quantity)
        expected_levels = [40, 20, 0]
        self.assertEqual(inventory_levels, expected_levels)

    def test_inventory_cost_zero_demand(self):
        demand = [0, 0, 0]
        reorder_point = 10
        order_quantity = 20
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
        expected_cost = 100 + 180
        self.assertAlmostEqual(cost, expected_cost, delta=0.1)

    def test_simulate_inventory_zero_demand(self):
        demand = [0, 0, 0]
        reorder_point = 10
        order_quantity = 20

        inventory_levels = simulate_inventory(demand, reorder_point, order_quantity)
        expected_levels = [30, 30, 30]
        self.assertEqual(inventory_levels, expected_levels)


if __name__ == "__main__":
    unittest.main()
