import requests
import schedule
import time


"""Función que notifica la temperatura"""
def notificar_temperatura():
    api_key = "abe222cb533216edb9ab63854d97af9f"
    url = f"https://api.openweathermap.org/data/2.5/weather?q=CiudadAutonomaDeBuenosAires&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        
        if temp <= 20:
            mensaje = f"La temperatura actual es de {temp} grados Celsius. Es fresco, ¡no te olvides el abrigo!"
        else:
            mensaje = f"La temperatura actual es de {temp} grados Celsius. Es caluroso, ¡no necesitas abrigo!"
            
        enviar_mensaje(mensaje)
    else:
        print("No se pudo obtener la temperatura")



"""Función que envía un mensaje de texto"""
from twilio.rest import Client

account_sid = "SKd6f8293a1a6501d9e52d15fdfaefe27c"
auth_token = "dpNtbZKKtqm1CifxBd2hML7X0KmUkd85"
twilio_number = "3571638693"
tu_numero = "3571638693"

def enviar_mensaje(texto):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=texto,
        from_=twilio_number,
        to=tu_numero
    )
    print(f"Mensaje enviado a {message.to}: {message.body}")




"""Recibir notificaciones periódicas"""
schedule.every(30).minutes.do(notificar_temperatura)

while True:
    schedule.run_pending()
    time.sleep(1)

