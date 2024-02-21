import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def capture_screenshots_from_domains(domain_file, output_directory):
    # Configuración de Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Para ejecutar Chrome en modo sin cabeza
    driver = webdriver.Chrome(options=chrome_options)
    
    # Establecer un tiempo de espera para la carga de la página
    driver.set_page_load_timeout(30)

    # Crear directorio de salida si no existe
    os.makedirs(output_directory, exist_ok=True)

    # Leer dominios del archivo de texto
    with open(domain_file, 'r') as file:
        domains = [domain.strip() for domain in file.readlines()]

    # Captura de pantalla de cada dominio
    for domain in domains:
        try:
            url = "http://" + domain
            driver.get(url)  # Abre la página web
            time.sleep(2)  # Esperar un poco para asegurar que la página se cargue completamente
            screenshot_path = os.path.join(output_directory, f"{domain}.png")
            driver.save_screenshot(screenshot_path)  # Guarda la captura de pantalla
            print(f"Captura de pantalla de {url} realizada correctamente.")
        except WebDriverException:
            print(f"Error al capturar la pantalla de {url}.")

    # Cerrar el navegador
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <archivo_de_dominios> <directorio_de_salida>")
    else:
        domain_file = sys.argv[1]
        output_directory = sys.argv[2]
        capture_screenshots_from_domains(domain_file, output_directory)
