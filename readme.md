# Reversi IA

---
## Resumen e inicio del programa.
En esta serie de pasos usted podrá descargar y correr nuestro juego Reversi.

PASO 0: Clonar el repositorio (SSH o HTTPS):
```bash
	$git clone https://github.com/JajoScript/IA-Reversi.git
	$git clone git@github.com:JajoScript/IA-Reversi.git
```

PASO 1: Entrar al repositorio clonado.
```bash
	$cd IA-Reversi\
```

PASO 2: Crear un entorno de desarrollo.
```bash
	$py -m venv env
```

PASO 3: Activar el entorno de desarrollo.
```bash
	$env\Scripts\activate.bat
```

PASO 4: Instalar las dependencias necesarias para correr el programa.
```bash
	$pip install -r requirements.txt
```

PASO 5: Ejecutar el paquete **src**.
```bash
	$py src\
```

---
## Introducción y buenas prácticas

---
## Buenas prácticas
Se definió como un estándar programar utilizando la tabulación para la indentación, con un tamaño de 3 espacios.
Por otro lado, se usa el paradigma de programación orientada a objeto en el desarrollo de todo el trabajo.

---
## Dependencias
Para funcionalidad y control de tipado es necesaria una versión de Python.

*	pygame==2.0.1
*	numpy==1.21.2
*	mypy==0.910
*	lxml==4.6.3
*  Pyton ^3.6.x

---
## Entorno de desarrollo
Generación de un entorno de desarrollo con python.
```bash
	$py -m venv env/
```

### Verificación de archivos

```bash
	$mypy --config-file .mypy.ini src/
	$mypy --config-file .mypy.ini src/ --html-report src/__test__/
```

## Arquitectura del directorio.
En el siguiente apartado se describen los distintos archivos presentes en el proyecto.

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
	# Archivo destinado a la implementación de la interfaz gráfica del usuario.
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
## Colaboradores
*  Javier Almarza, **AKA** @Jajoscript
*  Vicente Salas, **AKA** @Vychon
*  Gonzalo Cañas, **AKA** @Gonzal0-c
*  Nicolás Cruz, **AKA** @NickCracker
