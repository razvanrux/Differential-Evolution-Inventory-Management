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
        # Subtract demand from inventory first
        inventory_level -= d

        # Ensure inventory does not drop below zero
        inventory_level = max(inventory_level, 0)

        # Restock if inventory is below reorder point and order_quantity > 0
        if inventory_level <= reorder_point and order_quantity > 0:
            inventory_level += order_quantity

        # Record the updated inventory level
        inventory_levels.append(inventory_level)

    return inventory_levels
