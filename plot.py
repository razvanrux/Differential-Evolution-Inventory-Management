import matplotlib.pyplot as plt

def plot_demand_and_reorder_point(demand, reorder_point):
    plt.figure(figsize=(10, 6))
    plt.plot(demand, label="Demand", marker='o')
    plt.axhline(y=reorder_point, color='r', linestyle='--', label="Reorder Point")
    plt.title("Demand vs. Reorder Point")
    plt.xlabel("Time Period")
    plt.ylabel("Units")
    plt.legend()
    plt.grid()
    plt.show()

def plot_inventory_levels(inventory_levels, demand, reorder_point):
    plt.figure(figsize=(10, 6))
    plt.plot(inventory_levels, label="Inventory Level", marker='o', color='g')
    plt.plot(demand, label="Demand", marker='o', color='b')
    plt.axhline(y=reorder_point, color='r', linestyle='--', label="Reorder Point")
    plt.title("Inventory Levels Over Time")
    plt.xlabel("Time Period")
    plt.ylabel("Units")
    plt.legend()
    plt.grid()
    plt.show()
