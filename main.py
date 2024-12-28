class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

class InventoryItem:
    def __init__(self, item_id, name, cost_price, quantity):
        self.item_id = item_id
        self.name = name
        self.cost_price = cost_price
        self.quantity = quantity

class Sale:
    def __init__(self, sale_id, item_id, sale_price, quantity):
        self.sale_id = sale_id
        self.item_id = item_id
        self.sale_price = sale_price
        self.quantity = quantity

class CompanyManagement:
    def __init__(self):
        self.employees = []
        self.inventory = []
        self.sales = []

    # Employee Management
    def add_employee(self, emp_id, name, position, salary):
        employee = Employee(emp_id, name, position, salary)
        self.employees.append(employee)

    def remove_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    def list_employees(self):
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Position: {emp.position}, Salary: {emp.salary}")

    # Inventory Management
    def add_inventory_item(self, item_id, name, cost_price, quantity):
        item = InventoryItem(item_id, name, cost_price, quantity)
        self.inventory.append(item)

    def remove_inventory_item(self, item_id):
        self.inventory = [item for item in self.inventory if item.item_id != item_id]

    def list_inventory(self):
        for item in self.inventory:
            print(f"ID: {item.item_id}, Name: {item.name}, Cost Price: {item.cost_price}, Quantity: {item.quantity}")

    # Sales Management
    def add_sale(self, sale_id, item_id, sale_price, quantity):
        sale = Sale(sale_id, item_id, sale_price, quantity)
        self.sales.append(sale)

    def list_sales(self):
        for sale in self.sales:
            print(f"Sale ID: {sale.sale_id}, Item ID: {sale.item_id}, Sale Price: {sale.sale_price}, Quantity: {sale.quantity}")

    # Calculate Profit
    def calculate_profit(self):
        total_cost = sum(item.cost_price * item.quantity for item in self.inventory)
        total_revenue = sum(sale.sale_price * sale.quantity for sale in self.sales)
        total_salary = sum(emp.salary for emp in self.employees)
        profit = total_revenue - total_cost - total_salary
        return profit

# Example usage
if __name__ == "__main__":
    company = CompanyManagement()
    company.add_employee(1, "MrQu", "Manager", 5000)
    company.add_employee(2, "Mark", "Planer", 3000)

    company.add_inventory_item(1, "Laptop", 800, 10)
    company.add_inventory_item(2, "Phone", 500, 20)

    company.add_sale(1, 1, 1000, 5)
    company.add_sale(2, 2, 600, 10)

    print("Employees:")
    company.list_employees()

    print("\nInventory:")
    company.list_inventory()

    print("\nSales:")
    company.list_sales()

    print("\nProfit:")
    print(company.calculate_profit())