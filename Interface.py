import tkinter as tk
import tkinter.font as tkFont


window = tk.Tk()
window.title("2º - Vara Criminal")
window.geometry("500x400")

font = tkFont.Font(size=24) #define o tamanho da fonte

Label = tk.Label(window, text = "Selecione 'Acesso' para continuar.", font = font)
Label.pack()


frame = tk.Frame(window)
frame.pack(expand=True)

access_button = tk.Button(frame, text="Acesso", width=40, height=2)
access_button.pack(anchor= tk.CENTER, side=tk.TOP)

window.mainloop()
