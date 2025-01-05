def simulate_inventory(demand, reorder_point, order_quantity):
    """
    Simulate inventory levels using the optimal parameters.

    Parameters:
    - demand: List of demand values
    - reorder_point: Optimal reorder point
    - order_quantity: Optimal order quantity

    Returns:
    - List of inventory levels over time
    """
    inventory_level = reorder_point
    inventory_levels = []

    for d in demand:
        if inventory_level <= reorder_point:
            inventory_level += order_quantity
        inventory_levels.append(inventory_level)
        inventory_level -= d

    return inventory_levels
