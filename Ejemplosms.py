import requests
from gps import gps, WATCH_ENABLE, WATCH_NEWSTYLE
import time

# Configuración de la URL del servidor
server_url = "https://example.com/api/gps"

# Configuración del GPS
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

def send_location(latitude, longitude):
    payload = {"latitude": latitude, "longitude": longitude}
    try:
        response = requests.post(server_url, json=payload)
        if response.status_code == 200:
            print("Ubicación enviada correctamente")
        else:
            print("Error al enviar la ubicación: {}".format(response.text))
    except Exception as e:
        print("Error al enviar la ubicación:", e)

def main():
    while True:
        report = gpsd.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                latitude = getattr(report, 'lat')
                longitude = getattr(report, 'lon')
                print("Latitude: {}, Longitude: {}".format(latitude, longitude))
                send_location(latitude, longitude)
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")
