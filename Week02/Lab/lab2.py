import random

Weapons = ["Fist", "Knife", "Club", "Gun", "Bvomb", "Nuclear Bomb"]
WeaponRoll = random.randint(1, 6)
print("Hero's Chosen Weapon: ", Weapons[WeaponRoll-1])
if WeaponRoll==1:
    print("You rolled a weak weapon, friend.")
elif WeaponRoll<=4:
    print("Your weapon is meh.")
else:
    print("Nice weapon, friend.")
if WeaponRoll!=1:
    print("Thank goodness you didn't roll the Fist...")