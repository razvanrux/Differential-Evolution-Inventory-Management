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
        if inventory_level <= reorder_point:
            total_cost += ordering_cost
            inventory_level += order_quantity

        total_cost += holding_cost * max(inventory_level, 0)

        if inventory_level < d:
            total_cost += shortage_cost * (d - inventory_level)

        inventory_level -= d

    return total_cost