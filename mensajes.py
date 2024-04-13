import pyautogui
import time

def enviar_mensaje(numero, mensaje):
    # Abre el navegador y WhatsApp Web
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)  # Espera un segundo para que se abra una nueva pestaña
    pyautogui.write("https://web.whatsapp.com/")
    pyautogui.press('enter')
    time.sleep(10)  # Espera 10 segundos para que cargue WhatsApp Web

    # Busca el contacto
    pyautogui.click(x=200, y=200)  # Cambia las coordenadas según tu pantalla
    pyautogui.write(numero)
    pyautogui.press('enter')
    time.sleep(2)  # Espera 2 segundos para que cargue el chat

    # Escribe y envía el mensaje
    pyautogui.write(mensaje)
    pyautogui.press('enter')

# Ejemplo de uso
numero = "+524444120234"  # Cambia el número por el que desees enviar el mensaje
mensaje = "Hola, esto es un mensaje automatizado enviado desde Python utilizando pyautogui."
enviar_mensaje(numero, mensaje)
