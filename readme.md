# Reversi IA

---
## Introducción y buenas practicas

---
## Dependencias
Para funcionalidad y control de tipado es necesaria una versión de python 

*  Pyton ^3.6.x


---
## Entorno de desarrollo

Generación de un entorno de desarrollo con python
```bash
   $py -m venv <name>
```

### Verificación de archivos

```bash
   $mypy src/main.py
```


---
## Ejecución y uso

Clonar el repositorio:
```bash
   $git clone https://github.com/JajoScript/IA-Reversi.git
   $git clone git@github.com:JajoScript/IA-Reversi.git
```

Instalar las dependencias (recuerda crear antes un entorno de desarrollo):
```bash
   $py pip install -r requirements.txt
```

Iniciar la ejecución:
```bash
   $py src/main.py
```

---
## Funciones
Apartado con el fin de entregar contexto a las funcionalidades de cada una de las implementaciones dentro del proyecto.


```python
()
```
*  Uso:
*  Parametros:
*  Retorna:

```python
def mostrarVentana() -> None:
   """ ... """
```
*  Uso: Función utilizada para crear/renderizar la ventana del juego.
*  Parametros: Ninguno.
*  Retorna: Nada.

```python
def cargarAssets(nombre_archivo: str, transparencia: bool = False) -> typing.Any:
""" ... """
```
*  Uso: Realiza la carga de una recurso (*jpg, jpeg, png, etc*) para ser utilizada dentro de la ventana del juego.
*  Parametros: Es necesario el nombre del archivo junto con el parametro transparencia, parametro asignado para definir si debe o no ser transparente el fondo de la imagen (casos para recursos **.png**).
*  Retorna: Nada.

---
## Colaboradores
*  Javier Almarza, **AKA** @Jajoscript
*  Vicente Salas, **AKA** @Vychon
*  Gonzalo Cañas, **AKA** @Gonzal0-c
*  Nicolas Cruz, **AKA** @NickCracker
