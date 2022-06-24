# print("")
# use three qoutes at the end and start of the print instead of 1
print("""
                        ..    ............                                                          
                        ..             ..                                                           
,..                     ,.             ..          .                                                
..,,,..                 ,.                        ,: ..                                             
 .  ......              ,.                       .,...,,,.                                          
.,.     ......          ,.                       ,....,;,,.                                         
,,....  .........       .                :;;,   ......:i;;.                                         
::::,,..,,,,......  .   .                fGGi     ....:f11i.                                        
:::::::::,,,,,,... ..  ..                L80;    . ...,tLfi                                         
::::::::::,,,,,,......  .               .fGC:   .. .....:;.                                     ....
;;:::::::::,....,. ......               ,i;1;.   .....,....  ....                        .      ....
iiiiiiii;;;::::,,,,........... .      . ::,:::. .,..,,:;::;:::,:,..,;::,.........,:,,,.... ..  .....
:;;;;iiiiiiiiiii;i;;;;: :iiiiiiiiiiiiiii;....,..,,,,::::iii;;;:,:,..,;;:.:;:::::::;;,,..,..,,,,,,..,
........,,,,,,:::;::::, ,;;;;;;;;;;;;;;;. ..,,,,,,,,:;;:ii;;:,,,......;:.,,,......,:,,. ............
................,: .... ...............  .........,,,i;::ii;:,.,. .,,.,,........   ,,,.  ..         
................::..... ................ .... ....,,:;,,,,,,,...  ..,,,..........  ,,,.  ..         
................:, ...  .....................   .  ............    .,...,,,.....   ,,,,   .         
...............,:,...........................      ..,,..,,,,,.     ::. ,,,:,...   ,,,.   .        .
....,,,,,::::;;;;;;;;;;;;iiiiiiiiiiii;......     ........,,,,,.      :;,..,,,,.:::::::::::,,,,,,,,,.
:;;;;;;;;;iiiiiiiiiiiiiiiiiiiiiiii;;;. .....     ..........,,,..:     :i:...,,,,:;:::,,,,,,,,,,,,,..
;;;;;;;;;;;:::::,,,,,,,..,.,,,,,,,,,    .....,,,...............,i,     :;,...,,..,,,,,..............
,,,,,,.....,,,,,,,,:::::::::::::::::,..     ..,:::,......,...:;;:,      ,:,......,,,,,,,,,,,,,..,..,
...,,,,,::::::::::::::::::::::::::,::::.       ..,......,.,,.,;:.       .::,.....,,,,,,,,,,.........
,,,,,,,,,,,,,,,:::::::::::::::::,,,,,,,                ...,,..,..        .:,,.....,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,:::::::::::::::::,,,,,,:,                   ...,,,..        ,:,.....,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,::::::::::::::::,,,,,,,:.                    ........        ::,......,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,::::::::,,,,,,,,,,,,,,.                     ..,,...        .::,,,,,,::,,,,,,,,,,,,,,
""")

print("Welcome to Survivor. \nYour mission is to survive.")

direction = input(
    "Your are at a party\nDo you want to go left or right?\ntype 'left' for left or 'right' for right: \n").lower()


if direction == "right":
    print("""
    You went right and you fell into the pool. You become the talk of the town.
    """)
    print("Game Over")
else:
    print("You went left.")
    walk_wait = input(
        "You get to the gate. Do you go walk home or do you wait\nType 'walk' to walk and 'wait' to wait:\n").lower()
    if walk_wait == "walk":
        print("You walk home, while walking you get hit by a car, and you die\nGame Over!")
    else:
        print("You decided to wait. Now three taxi drivers offer to take you home")
        Car_Color = input(
            "Which do you enter, red, blue or green: \n")
        if Car_Color == "red":
            print("You entered the red taxi. As the car moves one of the tires, explode.\nWhich causes an accident that lands you in the hospital\nGame Over.")
        elif Car_Color == "blue":
            print(
                "you enter the blue taxi\nCongratulations you just won $100,000 and a free ride home\nYou win!")
        elif Car_Color == "green":
            print("You entered the green taxi.\nOn your way home the driver says he ran out or fuel and parks the car.\nHe tells you not to leave that he will be back\n2 hours later you are arrested for theft\nGame Over")
        else:
            print("The door you chose doesn't exist. Game Over")
