# environment.py
import cv2
import numpy as np
import mss
import threading
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ScreenRecorder:
    # Definición de la clase ScreenRecorder (como antes)
    def __init__(self, output_file):
        self.output_file = output_file
        self.frames = []
        self.is_recording = False

    def record(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            while self.is_recording:
                img = np.array(sct.grab(monitor))
                frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                self.frames.append(frame)

    def start(self):
        self.is_recording = True
        self.thread = threading.Thread(target=self.record)
        self.thread.start()

    def stop(self):
        self.is_recording = False
        self.thread.join()
        if self.frames:
            height, width, _ = self.frames[0].shape
            out = cv2.VideoWriter(
                self.output_file, cv2.VideoWriter_fourcc(*'mp4v'), 15, (width, height)
            )
            for frame in self.frames:
                out.write(frame)
            out.release()

def before_scenario(context, scenario):
    # Inicializa el WebDriver
    options = Options()
    # options.add_argument('--headless')  # Descomenta si deseas ejecutar en modo headless
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.maximize_window()

    # Generar un nombre de archivo único para cada escenario
    video_name = scenario.name

    # Si el escenario es un Scenario Outline con ejemplos, incluimos los parámetros en el nombre del video
    if hasattr(context, 'table') and context.table:
        pass  # No hay necesidad de modificar para tablas en Given
    elif hasattr(context, 'active_outline') and context.active_outline:
        # Para versiones más recientes de behave
        example = context.active_outline
        params = '_'.join(f"{k}_{v}" for k, v in example.items())
        video_name = f"{video_name}_{params}"
    elif context._stack and 'example' in context._stack[0]:
        # Para versiones más antiguas de behave
        example = context._stack[0]['example']
        params = '_'.join(f"{k}_{v}" for k, v in example.items())
        video_name = f"{video_name}_{params}"

    # Limpiar el nombre del archivo de video
    video_name = re.sub(r'[<>:"/\\|?*]', '_', video_name)
    video_name = f"{video_name}.mp4".replace(" ", "_")

    context.recorder = ScreenRecorder(video_name)
    context.recorder.start()

def after_scenario(context, scenario):
    # Detiene la grabación de pantalla
    context.recorder.stop()
    # Cierra el WebDriver
    context.driver.quit()
