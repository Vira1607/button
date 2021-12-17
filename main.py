import tkinter

window=tkinter.Tk()
button=tkinter.Button(window, text="Нажми на кнопку...", width=40)
button.pack(padx=10, pady=10)
clickCount=0

def onClick(event):
    global clickCount
    clickCount=clickCount+1
    if clickCount%6==1:
        button.configure(text="Получишь результат")
    elif clickCount%6==2:
        button.configure(text="И твоя мечта осуществится.")
    elif clickCount%6==4:
        button.configure(text="Ну что же ты не рад?")
    elif clickCount%6==5:
        button.configure(text="Тебе больше не к чему стемиться!")
    else:
        button.configure(text="Нажми на кнопку")
        #button.pack_forget()
        
button.bind("<ButtonRelease-1>", onClick)
window.mainloop()
