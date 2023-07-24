Aplicación Flask Cliente
Esta es una aplicación web desarrollada con Flask que te permite escribir notas
secretas y almacenarlas para luego ser mostradas una vez al insertar el codigo.

Requisitos
Antes de ejecutar la aplicación, asegúrate de tener Python instalado en tu sistema. Además, se recomienda utilizar un entorno virtual para evitar conflictos con las dependencias. Sigue los siguientes pasos para configurar el entorno virtual y ejecutar la aplicación:

Clona el repositorio desde GitHub:

git clone https://github.com/miryamsanchez/secreto.git

Accede al directorio del proyecto:

cd secreto

Instala las dependencias:

pip install -r requirements.txt

Uso
Para ejecutar la aplicación, sigue estos pasos:

Asegúrate de estar en el directorio del proyecto y de tener el entorno virtual activado.

Ejecuta el siguiente comando:

python app.py

Con el enlace que te aparece en el terminal, con el siguiente formato

http://localhost:5000

Esto te llevará a la página principal de la aplicación, donde podrás crear la nota, guardarla y leerla. 

Estructura del proyecto
El proyecto tiene la siguiente estructura de archivos y directorios:

app.py: El archivo principal de la aplicación que contiene la lógica del servidor Flask.
modelo.py: El archivo que define los métodos para leer, guardar y borrar nota.
templates/: Directorio que contiene las plantillas HTML utilizadas para renderizar las páginas web.
base.html: Plantilla base que define la estructura común de las páginas.
crearnota.html: Plantilla en la cual se escribe la nota.
enlace.html: Plantilla para mostrar el enlace en el que se almaceno la nota y el qr.
leernota.html: Plantilla que muestra la nota.
error.html: Plantilla de error.



