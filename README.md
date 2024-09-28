[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vK6WBQ1t)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15560930)

# Creacion de test y reportes usando Selenium Gird

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
### Instalar allure-pytest
```python
pip install allure-pytest
```
### Codigo para correr las pruebas para cada navegador:
```python
pytest --browser=chrome --alluredir=./allure-results
pytest --browser=edge --alluredir=./allure-results
pytest --browser=firefox --alluredir=./allure-results
```
### Codigo para correr las pruebas en paralelo:
```python
pytest -n 3 --alluredir=./allure-results
```

### Código para visualizar los reportes en allure:
```powershell
allure serve ./allure-results
```

