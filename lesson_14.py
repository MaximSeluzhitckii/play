import tkinter as tk
import random

master = tk.Tk()

step = 64
N_X = 10
N_Y = 10

WIDTH = step * N_X
HEIGHT = step * N_Y
a = False

player_pic = tk.PhotoImage(file=r".\player.png")

canvas = tk.Canvas(master, bg='#FCAB08',
                   width=WIDTH, height=HEIGHT)
player_pos = (random.randint(0, N_X - 1) * step, random.randint(0, N_Y - 1) * step)
print(player_pos)

label = tk.Label(master, text="He попадись!")


def prepare_and_start():

    global player
    global oval_finish
    global enemy
    canvas.delete("all")

    player_pos = (random.randint(1, N_X - 1) * step,
                  random.randint(1, N_Y - 1) * step)
    player = canvas.create_image((player_pos[0], player_pos[1]),
                                 image=player_pic,
                                 anchor='nw')
    oval_finish = canvas.create_oval(250, 250, 350, 350, fill='white')
    enemy = canvas.create_oval(300, 300, 400, 400, fill='red')

    label.config(text="Haйди выход!")
    master.bind("<KeyPress>", key_pressed)

def chek_win():
    xy = canvas.coords(player)
    overlap = canvas.find_overlapping(xy[0], xy[1], xy[0]+100, xy[1]+100)
    if enemy in overlap:
        print('looser')
        label.config(text='You loose!')
    elif oval_finish in overlap:
        print('winner')
        label.config(text='You win!')

def move_enemy():
    canvas.move(enemy, random.randint(-20, 20), random.randint(-20, 20))

def move_wrap(obj, move_x, move_y):
    xy = canvas.coords(obj)
    canvas.move(obj, move_x, move_y)
    print(xy)

    if xy[0] <= 0:
        canvas.move(obj, WIDTH, 0)
    if xy[0] >= WIDTH:
        canvas.move(obj, -WIDTH, 0)
    if xy[1] <= 0:
        canvas.move(obj, 0, HEIGHT)
    if xy[1] >= HEIGHT:
        canvas.move(obj, 0, -HEIGHT)

def key_pressed(event):
    if event.keysym == 'Up':
        move_wrap(player, 0, -step)
    elif event.keysym == 'Down':
        move_wrap(player, 0, step)
    elif event.keysym == 'Right':
        move_wrap(player, step, 0)
    elif event.keysym == 'Left':
        move_wrap(player, -step, 0)
    move_enemy()
    chek_win()


restart = tk.Button(master, text="Haчaть заново", command=prepare_and_start)

restart.pack()
label.pack()
canvas.pack()
prepare_and_start()

master.bind("<KeyPress>", key_pressed)
master.mainloop()
