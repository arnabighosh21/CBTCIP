import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo,showwarning
from  tkinter.filedialog import askdirectory

def file_path():
    global add
    add = askdirectory()
def save_file():

  global add
  try:
      time = int(sec.get())
      addr = add + "/"+" demo.wav"
      showinfo(title="Start", message="Rec Start")
      rece= sounddevice.rec((time*44100), samplerate=44100, channels=2)
      sounddevice.wait()
      write("demo.wav", 44100, rece)
      showinfo(title="End", message="Rec Stop")

  except:
      showwarning (title="Time", message="Wrong Format Time")


def main_window():
    global sec
    win=Tk()
    win.geometry("500x600")
    win.resizable(False,False)
    win.title("Voice recorder")
    win.config(bg="green")

    img1 = PhotoImage(file="pic7.png")
    l1  = Label(win,image=img1)
    l1.place(x=90,y=50,height=150,width=300)


    sec=Entry(win, font=(20))

    sec.place(x=150, y=230, height=50, width=200)


    l2 = Label(win, text="Time in Sec.", font=("Time New Roman", 20), bg="yellow")

    l2.place(x=100, y=290, height=50, width=300)

    b = Button(win, text="Path", font=("Time New Roman", 20),command= file_path)
    b.place(x=150, y=350, height=50, width=200)

    img2 = PhotoImage(file="pic8.png")
    start = Button(win,image=img2,command=save_file)
    start . place (x=200, y=410, height = 100 , width = 100)




    win.mainloop()

main_window()
