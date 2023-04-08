car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#stupid assignment, going to skip

pet = "CaT"
print("\nIs pet == 'cat'? I predict True.")
print(pet.lower() == "cat")

meaningoflife = 42
print("\nIs meaningoflife => 24? I predict True.")
print(meaningoflife >= 24)


weight = 70
lenght = 185
print("\nIs weight and length >= 65? I predict True.")
print(lenght >= 65 and weight >= 65)

print("\nIs weight and length <= 100? I predict False")
print(lenght >= 100 and weight >= 100)

print("\nIs weight or length <= 100? I predict True")
print(lenght >= 100 or weight >= 100)


randomlist = (5, 221, 545, 4, 1, 453)
print("\nIs 7 in randomlist? I predict False")
print(7 in randomlist)

print("\nIs 221 in randomlist? I predict True")
print(221 in randomlist)

print("\nIs 221 not in randomlist? I predict False")
print(221 not in randomlist)

print("\nIs 500 not in randomlist? I predict True")
print(500 not in randomlist)
