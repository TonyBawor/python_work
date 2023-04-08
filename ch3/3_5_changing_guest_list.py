glist = ["malcolm x", "huey .p newton", "martin luther king"]

print(f"Hello {glist[2].title()}, you are invited to dinner for tomorrow night.")
print(f"Good evening {glist[0].title()}, you are invited for dinner")
print(f"{glist[1].title()} how is it going, you up for dinner tomorrow?")

print(f"{glist[1].title()} could't make it.")

#del value [1](huey) and then insert new value in right position into list(1)
del glist[1]
glist.insert(1, "FraNZ KAFka")

print(f"{glist[1].title()} how is it going, you up for dinner tomorrow?")

