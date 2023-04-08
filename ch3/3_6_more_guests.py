glist = ["malcolm x", "huey .p newton", "martin luther king"]

print(f"Hello {glist[2].title()}, you are invited to dinner for tomorrow night.")
print(f"Good evening {glist[0].title()}, you are invited for dinner!")
print(f"{glist[1].title()} how is it going, you up for dinner tomorrow?")

print(f"{glist[1].title()} could't make it.")

#del value [1](huey) and then insert new value in right position into list(1)
del glist[1]
glist.insert(1, "FraNZ KAFka")

# glist = ["malcolm x", "FraNZ KAFka", "martin luther king"]

print(f"{glist[1].title()} how is it going, you up for dinner tomorrow?")
print(f"Hello {glist[2].title()}, you are invited to dinner for tomorrow night.")
print(f"Good evening {glist[0].title()}, you are invited for dinner!")

print("We found a bigger dinner table, so we will invite more guests to the dinner!")

glist.insert(0, "ThoMAS SaNKArA")
# glist = ["ThoMAS SaNKArA", "malcolm x", "FraNZ KAFka", "martin luther king"]
glist.insert(2, "jIMI HEnDriX")
# glist = ["ThoMAS SaNKArA", "malcolm x", "jIMI HEnDriX", "FraNZ KAFka", "martin luther king"]
glist.append("KarL MArX")
# glist = ["ThoMAS SaNKArA", "malcolm x", "jIMI HEnDriX", "FraNZ KAFka", "martin luther king", "KarL MArX"]

print(f"Good evening {glist[0].title()}, you are invited for dinner!")

print(f"Good evening {glist[1].title()}, you are invited for dinner!")

print(f"Good evening {glist[2].title()}, you are invited for dinner!")

print(f"Good evening {glist[3].title()}, you are invited for dinner!")

print(f"Good evening {glist[4].title()}, you are invited for dinner!")

print(f"Good evening {glist[5].title()}, you are invited for dinner!")
