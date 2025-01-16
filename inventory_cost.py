def inventory_cost(params, demand, ordering_cost, holding_cost, shortage_cost):
    """
    Calculate total inventory cost based on reorder point and order quantity.

    Parameters:
    - params: Tuple (reorder_point, order_quantity)
    - demand: List of demand values for each period
    - ordering_cost: Fixed cost per order
    - holding_cost: Cost per unit held in inventory
    - shortage_cost: Cost per unit short of demand

    Returns:
    - Total inventory cost
    """
    reorder_point, order_quantity = params
    total_cost = 0
    inventory_level = reorder_point

    for d in demand:
        # Subtract demand first
        inventory_level -= d

        # Apply shortage cost if inventory is negative
        if inventory_level < 0:
            total_cost += shortage_cost * abs(inventory_level)
            inventory_level = 0  # Reset inventory to 0 after shortage is accounted

        # Restock if inventory is below reorder point
        if inventory_level <= reorder_point and order_quantity > 0:
            total_cost += ordering_cost
            inventory_level += order_quantity

        # Apply holding cost after restocking
        total_cost += holding_cost * inventory_level

    return total_cost
