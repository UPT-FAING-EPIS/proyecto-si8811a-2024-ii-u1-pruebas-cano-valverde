
# UNIVERSIDAD PRIVADA DE TACNA
## Facultad de Ingeniería
## Escuela profesional de Ingeniería de Sistemas
![Logo de upt](https://net.upt.edu.pe/tdv/assets/dist/img/logo_upt_2024.png)
### Proyecto: Juegos Florales
### Pruebas de Aceptación/Interfaz

### Integrantes:
| ID  | Nombres           | Apellidos           | Código      |
| --- | ----------------- | ------------------- | ----------- |
| 1   | Jean Pier Elias   | Valverde Zamora     | 2020066920  |
| 2   | Anthony Alexander | Cano Sucso          | 2020067573  |
___
____
En primer lugar, se tiene que descargar la versión mas reciente donde se realiza las pruebas con docker LocalDockerTests.
____
## Creacion de test y reportes usando Selenium Gird
- Primero se crea un entorno virtual en la raíz del proyecto y luego se instala las dependencias necesarias:

```python
myenv\Scripts\activate
```
  
### Instalar pytest :

```python
pip install pytest
```
### Instalar allure-pytest para generar reportes con Allure
```python
pip install allure-pytest
```
### Instalar Selenium WebDriver
```python
pip install selenium
```
### Instalar pytest-selenium
```python
pip install pytest-selenium
```
### Instalar pytest-xdist

```python
pip install pytest-xdist
```
### Codigo para correr las pruebas en paralelo:
```python
pytest -n 3 --alluredir=./allure-results
```

### Código para visualizar los reportes en allure:
```powershell
allure serve ./allure-results
```
### Diagrama de selenium grid con allure
```mermaid
graph TD
    A[VS Code - Ejecución de pruebas] -->|Envía pruebas| B[Selenium Grid]
    B -->|Distribución de pruebas| C[Chrome]
    B -->|Distribución de pruebas| D[Firefox]
    B -->|Distribución de pruebas| E[Edge]
    C -->|Resultados de pruebas| F[Allure Reporter]
    D -->|Resultados de pruebas| F[Allure Reporter]
    E -->|Resultados de pruebas| F[Allure Reporter]
    F -->|Generación de reporte| G[Allure Serve]
    C -->|Grabación de video| H[Chrome Video Recorder]
    D -->|Grabación de video| I[Firefox Video Recorder]
    E -->|Grabación de video| J[Edge Video Recorder]
    H --> K[Video de prueba disponible]
    I --> K[Video de prueba disponible]
    J --> K[Video de prueba disponible]
```
