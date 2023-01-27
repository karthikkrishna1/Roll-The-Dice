import tkinter

import pyglet

import random









from tkinter import *
def main():
    global root_main
    root_main=Tk()
    root_main.title("Main Menu")
    canvas1 = Canvas(root_main, width=900, height=500)
    canvas1.pack()
    img1 = PhotoImage(file="dicehome.png")
    canvas1.create_image(20, 20, anchor=NW, image=img1, )
    mybutton1=Button(root_main,text="Play Dice",padx=10,pady=5,command=die,bg="black",fg="white")
    mybutton2 = Button(root_main, text="Quit", padx=10, pady=5, command=root_main.destroy, bg="black", fg="white")
    mybutton1.pack()
    mybutton2.pack()
    root_main.mainloop()

def gif():
    root1.destroy()
    animation=pyglet.image.load_animation("tenor3.gif")
    animSprite=pyglet.sprite.Sprite(animation)

    w=800
    h=600
    window=pyglet.window.Window(width=w,height=h)
    r, g, b, alpha=0.5,0.5,0.8,0.5
    pyglet.gl.glClearColor(r,g,b,alpha)

    @window.event
    def on_draw():
        window.clear()
        animSprite.draw()
    @window.event
    def on_key_press(symbol,modifier):
        if symbol == pyglet.window.key.SPACE:
            global num_disp
            num_disp=1
            window.close()



    pyglet.app.run()



def reload():
    root2.destroy()
    main()
def die():
    root_main.destroy()
    global root1
    root1 = tkinter.Tk()
    root1.title("Roll dice")
    canvas1 = Canvas(root1, width =450, height = 300)
    canvas1.pack()
    img1 = PhotoImage(file="dice.png")
    canvas1.create_image(20,20, anchor=NW, image=img1,)
    mybutton = Button(root1, text="Start Roll",padx= 10,pady=5, command=gif, bg="black", fg="white")
    mybutton.pack()
    root1.mainloop()





    if num_disp==1:
        num_die=random.randint(1,6)
        global root2


        root2 = tkinter.Tk()
        root2.title("Result")
        canvas = Canvas(root2, width=300, height=300)
        canvas.pack()
        if num_die == 1:
            img = PhotoImage(file="dice1.png")
            canvas.create_image(30, 20, anchor=NW, image=img)
            Mylabel1 = Label(root2, text="Its a one!", bg="black", fg="white")
            Mylabel1.pack()
            mybutton = Button(root2, text="Back to Home Screen.", padx=10, pady=5, command=reload, bg="black", fg="white", )
            mybutton.pack()



        if num_die==2:
            img = PhotoImage(file="dice2.png")
            canvas.create_image(30, 20, anchor=NW, image=img)
            Mylabel2 = Label(root2, text="Its a Two!", bg="black", fg="white")
            Mylabel2.pack()
            mybutton = Button(root2, text="Back to Home Screen.", padx=10, pady=5, command=reload, bg="black", fg="white", )
            mybutton.pack()

        if num_die == 3:
            img = PhotoImage(file="dice3.png")
            canvas.create_image(30, 20, anchor=NW, image=img)
            Mylabel = Label(root2, text="Its a three!", bg="black", fg="white")
            Mylabel.pack()
            mybutton = Button(root2, text="Back to Home Screen.", padx=10, pady=5, command=reload, bg="black", fg="white", )
            mybutton.pack()


        if num_die == 4:
            img = PhotoImage(file="dice4.png")
            canvas.create_image(30, 20, anchor=NW, image=img)
            Mylabel = Label(root2, text="Its a four!", bg="black", fg="white")
            Mylabel.pack()
            mybutton = Button(root2, text="Back to Home Screen.", padx=10, pady=5, command=reload, bg="black", fg="white", )
            mybutton.pack()


        if num_die == 5:
            img = PhotoImage(file="dice5.png")
            canvas.create_image(30, 20, anchor=NW, image=img)
            Mylabel = Label(root2, text="Its a five!", bg="black", fg="white")
            Mylabel.pack()
            mybutton = Button(root2, text="Back to Home Screen.", padx=10, pady=5, command=reload, bg="black", fg="white", )
            mybutton.pack()

        if num_die == 6:


            img = PhotoImage(file="dice6.png")
            canvas.create_image(30, 20, anchor=NW, image=img)
            Mylabel = Label(root2, text="Its a six!", bg="black", fg="white")
            Mylabel.pack()
            mybutton = Button(root2, text="Back to Home Screen.", padx=10, pady=5, command=reload, bg="black", fg="white", )
            mybutton.pack()

            root_cong = Toplevel()
            root_cong.title("Congratulations!!")
            img1 = PhotoImage(file="download.png ")
            canvas1 = Canvas(root_cong, width=300, height=300)
            canvas1.pack()
            canvas1.create_image(30, 20, anchor=NW, image=img1)







    root2.mainloop()

main()

"""def guess():
    rand_num =random.randint(1,1000)

    def check():


            if int(guess) == rand_num:
                mylabel.destroy()
                num.destroy()
                mylabel2 = Label(root, text="Congrats!! You guessed it.", padx=20, pady=5)
                mylabel2.pack()
                root2 = Toplevel()
                img1 = PhotoImage(file="download.png ")
                canvas1 = Canvas(root2, width=300, height=300)
                canvas1.pack()
                canvas1.create_image(30, 20, anchor=NW, image=img1)
                root2.mainloop()

            else:
                if int(guess) > rand_num:
                    mylabel2 = Label(root, text="Go lower.", padx=20, pady=5)
                    mylabel2.pack()
                if int(guess) < rand_num:
                    mylabel2 = Label(root, text="Go Higher.", padx=20, pady=5)
                    mylabel2.pack()

    while True:
        flag=1
        root = Tk()
        mylabel = Label(root, text="Enter your guess in the box below")
        mylabel.pack()
        num = Entry(root, borderwidth=10)
        num.pack()
        button=Button(root,text="Go back to home screen",command=check)
        button.pack()
        guess=num.get()

        root.mainloop()
"""







