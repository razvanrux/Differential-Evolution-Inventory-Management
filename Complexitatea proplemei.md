# Function Analysis

## Function `inventory_cost`

1. **Best Case:**
   - Complexity is determined by iterating through the `demand` list: **O(n)**, where `n` is the number of elements in `demand`.

2. **Worst Case:**
   - Demand always exceeds `inventory_level`. However, the complexity remains linear because only one iteration through the `demand` list is performed, so the complexity is **O(n)**.

3. **Average Case:**
   - Costs are calculated for each element, and the `if` conditions are evaluated in constant time. The complexity remains **O(n)**.

## Function `simulate_inventory`

1. **Best Case:**
   - If the inventory is always sufficient, only the `inventory_levels` list is updated. The complexity is **O(n)**.

2. **Worst Case:**
   - If the inventory falls below the reorder point for every request, an additional order is placed at each step. Nevertheless, operations are performed in a single iteration, so the complexity remains **O(n)**.

3. **Average Case:**
   - With random demand and variable inventory behavior, the complexity remains linear **O(n)**.

## Function `differential_evolution`

1. **Best Case:**
   - If optimization converges quickly, the number of iterations is minimal. The complexity depends on the population size (`P`) and the number of parameters (`D`): **O(P \* D \* K\_min)**, where `K\_min` is the minimum number of iterations.

2. **Worst Case:**
   - The algorithm requires all possible maximum iterations (`K\_max`) and evaluates all combinations. The complexity is **O(P \* D \* K\_max)**.

3. **Average Case:**
   - The number of iterations lies between the minimum and maximum: **O(P \* D \* K\_med)**.

---

# Proof of Correctness for `simulate_inventory`

### Preconditions:
- `demand` is a list of requests for each period.
- `reorder_point` is the optimal reorder point.
- `order_quantity` is the optimal reorder quantity.

### Goal:
The function aims to calculate inventory levels for each period.

### Postconditions:
- The resulting `inventory_levels` list correctly reflects the inventory evolution in each period, accounting for demand (`d`) and restocking when inventory falls below or equals `reorder_point`.

### Proof of Correctness:

#### Initialization:
At the beginning of execution:
- `inventory_level` is initialized to the value of `reorder_point`, ensuring the starting point is correct based on the provided parameters.

#### Maintaining Invariants:
In each iteration:
- **Condition Check:**
  - If `inventory_level <= reorder_point`, `order_quantity` is added to the inventory.
  - This ensures restocking occurs only when necessary, based on the reorder point.

- **Save Inventory Level:**
  - `inventory_levels.append(inventory_level)`:
    - The current inventory level is saved before subtracting the current demand, reflecting the correct state at the start of the period.

- **Update Inventory:**
  - `inventory_level -= d`:
    - The current demand is subtracted from the inventory, updating the inventory level for the next period.

#### Invariants:
- Inventory is updated correctly based on demand and restocking conditions.
- Each step adds a single element to `inventory_levels`.

#### Finalization:
At the end of the loop:
- The `inventory_levels` list contains the inventory levels for all demand periods.
- The function returns the complete list.
