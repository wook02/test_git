from tkinter import *

fnameList = ['gif1.gif', 'gif2.gif', 'gif3.gif', 'gif4.gif', 'gif5.gif',
             'gif6.gif', 'gif7.gif', 'gif8.gif', 'gif9.gif']

window = Tk()
window.title("사진 앨범")
window.geometry("500x350")

photoList = [PhotoImage(file=fname) for fname in fnameList]

num = 0

pLabel = Label(window, image=photoList[num])
pLabel.place(x=15, y=10)

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    pLabel.configure(image=photoList[num])

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    pLabel.configure(image=photoList[num])

btnPrev = Button(window, text="<이전", command=clickPrev)
btnNext = Button(window, text="다음>", command=clickNext)

btnPrev.place(x=150, y=300)
btnNext.place(x=250, y=300)

window.mainloop()