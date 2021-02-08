import tkinter as tk

pencere = tk.Tk()
pencere.title("Merhaba")
pencere.geometry("300x300+1000+100")
pencere.resizable(width=False, height=True)

metin = tk.Label(text="Merhaba Arkadaşlar")
metin.pack()

pencere.mainloop()