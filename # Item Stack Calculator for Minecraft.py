# Item Stack Calculator for Minecraft
items = int(input("Enter the amount of items you will need: "))

# Enter the stack size, which is usually 64 for most items, but can be 16 for items like Ender Pearls or Snowballs.
stack_size = int(input("Enter the total stack of an item (usually 64 or 16): "))

#Stack and remainder calculations
stacks = items // stack_size

remainder = items % stack_size

#Item name input
item_name = str(input("Enter the name of the item: "))

#Output the results
print(f"\nYou need: {stacks} stacks and {remainder} leftover {item_name}(s).")