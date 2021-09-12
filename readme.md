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


## Aquitectura del directorio.

```py
   __init__.py
   # Archivo destinado a estructurar el directorio src como un paquete.
```

```py
   __main__.py
   # Archivo destinado a la ejecución de todo el sistema.
```

```py
   GUI.py
   # Archivo destinado a la implementación de la interfaz grafica del usuario.
```

```py
   IA.py
   # Archivo destinado al desarrollo de la Inteligencia artificial.
```

```py
   GAME.py
   # Archivo destinado a la jugabilidad del programa.
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
   $py src/
```

---
## Funcionalidad
Apartado con el fin de entregar contexto a las funcionalidades de cada una de las implementaciones dentro del proyecto.

### Objetos
```python
class test():
   """ ... """
```

### Funciones
```python
def test() -> None:
   """ ... """
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
*  Nicolás Cruz, **AKA** @NickCracker
