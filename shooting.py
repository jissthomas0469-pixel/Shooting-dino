import pgzrun,random,pyautogui
print(pyautogui.size())
WIDTH,HEIGHT=pyautogui.size()
dino=Actor('velociraptor')
dino.pos=100,100
def draw():
    screen.clear()
    screen.blit('yellowstonenationalpark.png',(-100,-200))
    dino.draw()
def on_mouse_down(pos):
    print(pos)
    if dino.collidepoint(pos):
        dino.x=random.randint(50,WIDTH-50 )
        dino.y=random.randint(50,HEIGHT-50)
pgzrun.go()
