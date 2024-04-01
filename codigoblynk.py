import RPi.GPIO as GPIO
import requests
import time

token = "Token a usar"

# Configuración de la comunicación GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

def write(token, pin, value):
    api_url = "https://blynk.cloud/external/api/update?token=" + token + "&" + pin + "={:.2f}".format(value)
    response = requests.get(api_url)
    if "200" in str(response):
        print("Value successfully updated")
    else:
        print("Could not find the device token or wrong pin format")

def read(token, pin):
    api_url = "https://blynk.cloud/external/api/get?token=" + token + "&" + pin
    response = requests.get(api_url)
    return response.content.decode()

def main():
    while True:
        button = int(read(token, "v1"))
        if button == 1:
            GPIO.output(13, GPIO.HIGH)  # Encender el pin GPIO 13 (5 voltios)
            print("GPIO 13 encendido (5V)")
        else:
            GPIO.output(13, GPIO.LOW)   # Apagar el pin GPIO 13
            print("GPIO 13 apagado")
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    finally:
        GPIO.cleanup()  # Limpieza de los pines GPIO al salir del programa
