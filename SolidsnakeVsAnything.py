solidsnake_health = 100
anythinginuniverse_health = 100
solidsnake_damage = 10
anythinginuniverse_damage = 1
def simulate_combat():
    global solidsnake_health, anythinginuniverse_health
    while solidsnake_health > 0 and anythinginuniverse_health > 0:
        anythinginuniverse_health -= solidsnake_damage 
        print(f"solidsnake attacks anythinginuniverse leaving anythinginuniverse with {anythinginuniverse_health} health,")
        if anythinginuniverse_health <= 0:
            print("anythinginuniverse is defeated. solidsnake win!")
            break
    solidsnake_health -=anythinginuniverse_damage
    print(f"anythinginuniverse attacks solidsnake, leaving solidsnake with {solidsnake_health} health,")
    if solidsnake_health <= 0:  
        print("solidsnake is defeated. anythinginuniverse wins!")
    
print("FirstProject")
simulate_combat ()
