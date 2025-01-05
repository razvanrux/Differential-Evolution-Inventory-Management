from scipy.optimize import differential_evolution
from inventory_cost import inventory_cost
from simulate_inventory import simulate_inventory
from plot import plot_demand_and_reorder_point, plot_inventory_levels

demand = [50, 60, 55, 70, 65, 80, 75]
ordering_cost = 100
holding_cost = 2
shortage_cost = 5

bounds = [
    (10, 100),
    (20, 200)
]

result = differential_evolution(
    inventory_cost,
    bounds,
    args=(demand, ordering_cost, holding_cost, shortage_cost),
    strategy='best1bin',
    maxiter=1000,
    popsize=15,
    tol=0.01,
    mutation=(0.5, 1),
    recombination=0.7
)

optimal_reorder_point, optimal_order_quantity = result.x
print("Optimal Parameters (Reorder Point, Order Quantity):", result.x)
print("Minimum Total Cost:", result.fun)

plot_demand_and_reorder_point(demand, optimal_reorder_point)

inventory_levels = simulate_inventory(demand, optimal_reorder_point, optimal_order_quantity)
plot_inventory_levels(inventory_levels, demand, optimal_reorder_point)
