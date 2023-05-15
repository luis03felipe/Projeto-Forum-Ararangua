import tkinter as tk
import cv2
import face_recognition
import tkinter.font as tkFont

def capture_and_identify():
    video_capture = cv2.VideoCapture(0) # Inicializa a câmera
    while True:
        loader, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_locations = face_recognition.face_locations(gray) #detecta faces
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)  # Desenha um retângulo ao redor do rosto detectado
             
        cv2.imshow('Video', frame)# Exibe o quadro de vídeo com os rostos detectados
        
        if cv2.waitKey(1) & 0xFF == ord('q'):# ao apertar Q sai da captura
            break
    video_capture.release()
    cv2.destroyAllWindows()

def start_capture():
    root.withdraw() #Sai da janela principal e troca pela do video
    
    capture_and_identify()
    
    # Mostra a janela principal novamente quando a captura for concluída
    root.deiconify()

# Cria a janela principal
root = tk.Tk()
root.title("2º - Vara Criminal")
root.geometry("500x400")

font = tkFont.Font(size=24)

Label = tk.Label(root, text = "Selecione 'Acesso' para continuar.\n Aperte 'Q' para sair.", font = font)
Label.pack()


#Botão tela principal
button = tk.Button(root, text="Acesso", width=40, height=2, command=start_capture)
button.pack(anchor= tk.CENTER, side=tk.TOP)

root.mainloop()
