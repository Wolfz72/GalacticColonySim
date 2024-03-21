import numpy as np
from scipy.stats import norm

class Resource:
		def __init__(self, name, initial_quantity, initial_price, volatility):
				self.name = name
				self.quantity = initial_quantity
				self.price = initial_price
				self.volatility = volatility

class SpaceColonySimulator:
		def __init__(self, initial_cash, risk_free_rate, resources):
				self.cash = initial_cash
				self.risk_free_rate = risk_free_rate
				self.resources = resources

		def buy_resource(self, name, quantity):
				resource = next((r for r in self.resources if r.name == name), None)
				if resource:
						total_cost = resource.price * quantity
						if total_cost <= self.cash:
								self.cash -= total_cost
								resource.quantity += quantity
								return True
						else:
								print("Insufficient funds to buy resource.")
				else:
						print(f"Resource with name '{name}' not found.")
				return False

		def sell_resource(self, name, quantity):
				resource = next((r for r in self.resources if r.name == name), None)
				if resource:
						if quantity <= resource.quantity:
								self.cash += resource.price * quantity
								resource.quantity -= quantity
								return True
						else:
								print("Insufficient quantity to sell.")
				else:
						print(f"Resource with name '{name}' not found.")
				return False

		def update_resource_prices(self):
				for resource in self.resources:
						drift = self.risk_free_rate - 0.5 * resource.volatility ** 2
						shock = resource.volatility * np.random.normal()
						resource.price *= np.exp(drift + shock)
						resource.price = round(resource.price, 2)

# Create resources with unique parameters
water = Resource("Water", 30, 5, 0.1)
oxygen = Resource("Oxygen", 50, 8, 0.15)
food = Resource("Food", 10, 12, 0.2)
energy = Resource("Energy", 200, 1, 0.5)
uranium = Resource("Uranium", 5, 100, 0.04)


#stockexample = Resource(name, initial_quantity, initial_price, volatility)


# Simulation parameters
initial_cash = 10000
risk_free_rate = 0.05
simulator = SpaceColonySimulator(initial_cash, risk_free_rate, [water, oxygen, food, energy, uranium])

# Display initial market information
print("Market Information:")
for resource in simulator.resources:
		print('----------')
		print(f"Resource: {resource.name}")
		print(f"Initial Quantity: {resource.quantity}")
		print(f"Initial Price: {resource.price}")
		print(f"Volatility: {resource.volatility}")

print('----------')
print()
# Simulation steps
for _ in range(10):
		simulator.update_resource_prices()
		for resource in simulator.resources:
				print(f"Current Price of {resource.name}: {resource.price}")

		print()
		action = input("What do you want to buy/sell? (Enter 'buy' or 'sell' followed by resource name and quantity, e.g., 'buy Water 5'):\n")
		action_parts = action.split()
		if len(action_parts) >= 3:
				action_type = action_parts[0].lower()
				resource_name = action_parts[1]
				quantity = int(action_parts[2])

				if action_type == 'buy':
						simulator.buy_resource(resource_name, quantity)
				elif action_type == 'sell':
						simulator.sell_resource(resource_name, quantity)
				else:
						print("Invalid action. Please enter 'buy' or 'sell'.")
		print()
		print("Cash Balance:", simulator.cash)
		print()

# Example usage:
# Buy 5 units of Water
# simulator.buy_resource("Water", 5)

# Sell 3 units of Oxygen
# simulator.sell_resource("Oxygen", 3)