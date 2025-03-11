# Spiky Fire Animal ASCII Art
def draw_fire_animal():
    fire_animal = """
                            (     )
                           (       )
                          (         )
                        .-          -.
                       /          \  
                      /            \   
                     |   \    /     |       
                     |    \/       |   ~~~
                      \  (    )    /   ~~~~~~
                       \ |    |   /   ~~~~~~~~~~
                        \|    |/   ~~~~~~~~~~~~
          /\             |    |    ~~~~~~~~~~~
         /  \    ~~~~~~~ |    |   ~~~~~~~~~~~
        /    \   ~~~~~~~|    |   ~~~~~~~~~~~
       /      \  ~~~~~~ |    |   ~~~~~~~~~~~
      /        \ ~~~~~~~|    |   ~~~~~~~~~~~
     /__________\ ~~~~~~|    |   ~~~~~~~~~~~
    /   \    /   \ ~~~~ |    |   ~~~~~~~~~~~
   /     \  /     \ ~~~ |    |   ~~~~~~~~~~~
  /   ___  \/   ___\~~~ |    |   ~~~~~~~~~~~
 /   /   \   \ /   \~~~ |    |   ~~~~~~~~~~~
/___/     \___\_____\~~ |    |   ~~~~~~~~~~~
|    FIRE    |    ANIMAL|    |    ~~~~~~~~~~
|   SPARKY   |__________|    |     ~~~~~~~~
 \_________/    ~~~~~~~~~~  |    ~~~~~~~~~~
                ~~~~~~~~~~  |   ~~~~~~~~~~
                 ~~~~~~~~    ~~~~~~~~~~"""
    print(fire_animal)

# Draw the spiky fire animal
draw_fire_animal()

boss_health = 1000  # boss health
our_health = 200   # our health
leaf_use = 0
overgrow_use = 0
light_metal_use = 0
heavy_metal_use = 0
weakness_policy_use = 0

# choose your animal
choice = int(input("\nYou have encountered a fire type animal.\nPlease choose your animal to fight:\n 1. Grass \n 2. Rock \n 3. Steel\nYour choice: "))

if choice == 1:
    choices = "Grass"
elif choice == 2:
    choices = "Rock"
elif choice == 3:
    choices = "Steel"
    
print(f"You have chosen the {choices} animal")
boss_info = print(f"Boss health is currently : {boss_health}")

# check if player is dead
def check_game_over():
    if our_health <= 0:
        print("Your health reached 0. Game Over!")
        exit()  

# Grass animal
if choices == "Grass":
    wee = 1
    while wee > 0:
        attack = (int(input(f"1. Chlorophyll\n2. Leaf Guard\n3. Overgrow\n Attack (Choose a number): ")))
        wee = 0
        if attack == 1:
            print(f"Your attack wasn't effective\nThe fire animal attacks you\nIt was really effective\nYour health: {our_health - our_health}\nYou have died\n")
            check_game_over()
            break
        elif attack == 2:
            if leaf_use < 3:
                boss_health -= 50
                leaf_use += 1
                print(f"The fire animal attacks you\nYou blocked it\nYour attack wasn't really effective\nBoss health: {boss_health}\nYour health: {our_health}\n ")
                check_game_over()
                wee = 1
            else:
                print(f"You've used Leaf Guard 3 times. The fire animal attacks you and you die.\nBoss health: {boss_health}\nYou're health: {our_health - our_health}\nYou have died\n")
                check_game_over()
                break  
        elif attack == 3:
            if overgrow_use < 3:   # checking if overgrow used less than 3 times
                overgrow_damage = int(our_health * 0.20)  # 20% of player's health as damage
                boss_health -= overgrow_damage  # subtract damage from boss health
                overgrow_use += 1
                print(f"You used Overgrow! You sacrifice part of your health to unleash a powerful attack.\nYou deal {overgrow_damage} damage to the boss!\nBoss health: {boss_health}\nYour health: {our_health}\n")
                check_game_over()
                if boss_health <= 0:
                    print("You have defeated the Fire Animal!")
                    break  # game end
                else:
                    wee = 1  # continue the loop
            else:
                print(f"You've used Overgrow 2 times. The fire animal attacks you and you die.\nBoss health: {boss_health}\nYour health: {our_health - our_health}\nYou have died\n")
                check_game_over()
                break  # game end

# Rock animal
if choices == "Rock":
    wee = 1
    while wee > 0:
        attack = int(input("1. Sand Force\n2. Sturdy\n3. Weak Armor\nAttack (Choose a number): "))
        wee = 0
        if attack == 1:
            # Sand Force: fire animal gets damaged by 300, and the player gets damaged by 30
            boss_health -= 300  # fire animal gets damaged by 300
            our_health -= 30    # player gets damaged by 30
            print(f"Using Sand Force! The fire animal takes 300 damage.\nYou take 30 damage from the fire animal.\nBoss health: {boss_health}\nYour health: {our_health}\n")
            check_game_over()
            if boss_health <= 0:
                print("You have defeated the Fire Animal!")
                break  # end the game 
            else:
                wee = 1  # continue the loop
        elif attack == 2:
            # Sturdy: the player gets damaged by 5% of the boss's health, and the fire animal gets damaged by 200
            damage_taken = int(boss_health * 0.05)  # 5% of boss's health damage to the player
            our_health -= damage_taken
            boss_health -= 200  # fire animal gets damaged by 200
            print(f"Using Sturdy! You take {damage_taken} damage from the fire animal.\nThe fire animal takes 200 damage.\nBoss health: {boss_health}\nYour health: {our_health}\n")
            check_game_over()
            if boss_health <= 0:
                print("You have defeated the Fire Animal!")
                break  # end the game 
            else:
                wee = 1  # continue the loop
        elif attack == 3:
            # weak Armor: the fire animal gets damaged by 250, and the player gets damaged by 10% of the boss's health
            damage_taken = int(boss_health * 0.10)  # 10% of boss's health damage to the player
            our_health -= damage_taken
            boss_health -= 250  # fire animal gets damaged by 250
            print(f"Using Weak Armor! The fire animal takes 250 damage.\nYou take {damage_taken} damage from the fire animal.\nBoss health: {boss_health}\nYour health: {our_health}\n")
            check_game_over()
            if boss_health <= 0:
                print("You have defeated the Fire Animal!")
                break  # end the game if the boss is defeated
            else:
                wee = 1  # continue the loop

# Steel animal
if choices == "Steel":
    wee = 1
    while wee > 0:
        attack = int(input("1. Light Metal\n2. Heavy Metal\n3. Weakness Policy\nAttack (Choose a number): "))
        wee = 0
        if attack == 1:
            if our_health < 200 and light_metal_use == 0:
                heal = int(our_health * 0.10)
                our_health += heal
                print(f"Using Light Metal! You heal {heal} HP.\nYour health: {our_health}\n")
                
                our_health -= 100
                print(f"The fire animal attacks you for 100 damage.\nYour health: {our_health}\n")
                check_game_over()
                light_metal_use += 1
            elif our_health == 200 and light_metal_use == 0:
                fire_attack = int(boss_health * 0.05)
                boss_health -= fire_attack
                print(f"Using Light Metal! You attack the fire animal for {fire_attack} damage, but it's not very effective.\nBoss health: {boss_health}\nYour health: {our_health}\n")
               
                our_health -= 100
                print(f"The fire animal attacks you for 100 damage.\nYour health: {our_health}\n")
                check_game_over()
                light_metal_use += 1
            else:
                print(f"You've already used Light Metal.\nYour health: {our_health}\nBoss health: {boss_health}\n")
                wee = 1
        elif attack == 2:
            if heavy_metal_use < 3:
                damage_taken = int(boss_health * 0.10)  # 10% damage to boss
                our_health -= int(our_health * 0.05)  # 5% damage to self
                boss_health -= damage_taken
                print(f"Using Heavy Metal! You attack the fire animal for {damage_taken} damage.\nYou take {int(our_health * 0.05)} damage.\nBoss health: {boss_health}\nYour health: {our_health}\n")
                check_game_over()
                heavy_metal_use += 1
            else:
                print(f"You've used Heavy Metal more than 3 times. You die.\nYour health: {our_health - our_health}\nBoss health: {boss_health}\nYou have died.\n")
                check_game_over()
                break  # game end
        elif attack == 3:
            if weakness_policy_use < 5:
                damage = int(boss_health * 0.05)  # 5% damage each time
                boss_health -= damage
                weakness_policy_use += 1
                print(f"Using Weakness Policy! You deal {damage} damage to the fire animal.\nBoss health: {boss_health}\nYour health: {our_health}\n")
                check_game_over()
            else:
                print(f"You've used Weakness Policy 5 times. You die.\nYour health: {our_health - our_health}\nBoss health: {boss_health}\nYou have died.\n")
                check_game_over()
                break  # game end
