#What if a player chooses to change out his inventory?
# What if the player finds a weapon that is better than the one, that was previously equipped?
player_inventory = {"weapon": "fists of gu'den"}
print(f"The player has {player_inventory['weapon'].title()} equipped.")

player_inventory["weapon"] = "göb of the bean"
print(f"The player has {player_inventory['weapon'].title()} equipped.")

#Let's make it more interesting.
# Let's see how a different weapon, with more or less power can affect the player

print("\n")
player_inventory = {"weapon": "stick of truth", "player-power": 9}
print(f"Current player power is : {player_inventory['player-power']}.")

if player_inventory['player-power'] < 10:
    print("This player is too low level!")
    if player_inventory['weapon'].lower() == "stick of truth":
        player_inventory['weapon'] = "sword of git"
        print(f"Player has equipped {player_inventory['weapon'].title()}")
        player_inventory['player-power'] = 30
        print(f"Player-Power has increased to : {player_inventory['player-power']}!")
elif player_inventory['player-power'] < 25:
    print("This player is mediocre")
else:
    print("He is the one.")

#Another example can be moving aliens
alien_0 = {"x-position": 0, "y-position": 25, "speed": "medium"}
print(f"\nOriginal position: {alien_0['x-position']}")

#Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == "slow":
    x_increment = 1
elif alien_0['speed'] == "medium":
    x_increment = 2
else:
    x_increment = 3

#The new position is the old position plus the increment
alien_0['x-position'] = alien_0['x-position'] + x_increment
print(f"New position: {alien_0['x-position']}")