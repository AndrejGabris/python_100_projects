# Local Scope


enemies = 1 

def increase_enemies():
    enemies += 1  # error line due to local variable
    print(enemies)

increase_enemies()
print(enemies)



# Modyifying Gloabl Scope

enemies = 1 

def increase_enemies():
    global enemies
    enemies += 1 
    print(enemies)

increase_enemies()
print(enemies)
                     