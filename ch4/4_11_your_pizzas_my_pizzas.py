pizzas = ["hAwAI", "PePPERoni", "VEsuviO"]

for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

print("\nMane i luuuuuuv pizza")
print("pizza really that food")
print("pizza really makes you happy!")

friend_pizzas = pizzas[:]

friend_pizzas.append("MarGherita")

for pizza in pizzas:
    print(f"My favorite pizzas are: {pizza.title()} pizza!")

for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza.title()} pizza!")
