# pip install numpy
# pip install opencv-python

import cv2
import numpy as np
import tkinter as tk

contador = 0


def perguntar_saida(contador):
    resposta = False

    janela = tk.Toplevel()
    janela.title("Contagem finalizada")
    janela.geometry("400x300")
    janela.resizable(False, False)

    texto = tk.Label(
        janela,
        text=f"Contagem finalizada!\n\nForam contabilizadas {contador} tiaras.",
        font=("Arial", 16),
        justify="center"
    )
    texto.pack(pady=30)

    def sair():
        nonlocal resposta
        resposta = True
        janela.destroy()

    botao_sair = tk.Button(
        janela,
        text="Sair",
        font=("Arial", 12),
        width=10,
        command=sair
    )
    botao_sair.pack(pady=10)

    janela.wait_window()

    return resposta


root = tk.Tk()
root.withdraw()

camera = cv2.VideoCapture(0)

limite_tiaras = int(input("Digite a quantidade de tiaras a ser contabilizadas: "))

objeto_visivel = False
frames_sem_objeto = 0

while True:

    ret, frame = camera.read()

    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    amarelo_min = np.array([20, 100, 100])
    amarelo_max = np.array([35, 255, 255])

    mascara = cv2.inRange(
        hsv,
        amarelo_min,
        amarelo_max
    )

    kernel = np.ones((5, 5), np.uint8)

    mascara = cv2.erode(
        mascara,
        kernel,
        iterations=1
    )

    mascara = cv2.dilate(
        mascara,
        kernel,
        iterations=2
    )

    contornos, _ = cv2.findContours(
        mascara,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    objeto_detectado = False

    for contorno in contornos:

        if cv2.contourArea(contorno) > 2000:

            objeto_detectado = True

            x, y, w, h = cv2.boundingRect(contorno)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    if objeto_detectado:
        frames_sem_objeto = 0

        if not objeto_visivel:
            contador += 1
            objeto_visivel = True

            cv2.putText(
                frame,
                f"Tiaras contabilizadas: {contador}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 0),
                2
            )

            cv2.imshow("Camera", frame)
            cv2.waitKey(1)

    else:
        frames_sem_objeto += 1

        if frames_sem_objeto >= 15:
            objeto_visivel = False

    if contador >= limite_tiaras:
        sair = perguntar_saida(contador)

        if sair:
            break

        else:
            contador = 0
            objeto_visivel = False
            frames_sem_objeto = 0

    cv2.putText(
        frame,
        f"Tiaras contabilizadas: {contador}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 0),
        2
    )

    cv2.imshow("Camera", frame)

    # cv2.imshow("Mascara", mascara)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()