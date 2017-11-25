from tkinter import *
from tkinter import messagebox
def checked(i) :
      global player
      button = list[i]
      c=0
      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      c=rowchecker(i)
      if c==3:
            result(player)
            return
      c=colchecker(i)
      if c==3:
            result(player)
            return
      c=diagonalchecker(i)
      if c==3:
            result(player)
            return
      c=arcdiagonalchecker(i)
      if c==3:
            result(player)
            return
      
      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"
            
def result(player):
      messagebox.showinfo("result","Player "+player+ " WIN!!!")
      window.destroy()
      return
def rowchecker(i):
      button=list[i]
      c=0
      for j in range(9):
            if(j//3==i//3):
                  if(list[j]["text"]==button["text"]):
                        c+=1
      return c

def colchecker(i):
      button=list[i]
      global player
      c=0
      for j in range(9):
            if(j%3==i%3):
                  if(list[j]["text"]==button["text"]):
                        c+=1
      return c
def diagonalchecker(i):
      button=list[i]
      global player
      c=0
      for j in range(9):
            if(j//3==j%3):
                  if(list[j]["text"]==button["text"]):
                        c+=1
      return c
def arcdiagonalchecker(i):
      button=list[i]
      global player
      c=0
      for j in range(9):
            if((j//3)+(j%3)==2):
                  if(list[j]["text"]==button["text"]):
                        c+=1
      return c

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


