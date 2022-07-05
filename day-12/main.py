############ Scope ###############

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# Local Scope - it exists within functions

# def drink_potion():
#     # the variable potion_strength is only accessible in this function
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)


# Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         # the variable player_health is accessible for all because it is a global scope
#         potion_strength = 2
#         print(player_health)
#     # putting the function call outside of the game function doesn't allow it to be called because it doesn't have access to the game function
#     drink_potion()

# Python doesn't have a block scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy) #the new enemy variable is accessible outside of the if block since it is not embeded in a function


###### Modifying Global Scope #####
# enemies = 1 #        <------------------------------------------------
# #                                                                     |
# def increase_enemies():#                                              |
#     global enemies #This line give you to access to the global scope---
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# better way of modifying global scopes
# enemies = 1
# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1
# print(increase_enemies())
# print(f"enemies outside function: {enemies}")

# Global Constants - stay the same it is best to keep it capitalized
