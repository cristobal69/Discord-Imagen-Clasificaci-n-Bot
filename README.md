Bot de Discord con Detección de Objetos
Este es un bot de Discord que utiliza ImageAI y el modelo YOLOv3 para detectar objetos en imágenes enviadas por los usuarios. El bot procesa la imagen, detecta objetos, y añade texto en caso de encontrar autos. Finalmente, devuelve la imagen procesada al canal.

Características
Detecta objetos en imágenes usando un modelo preentrenado (YOLOv3).
Agrega texto a las imágenes procesadas cuando detecta autos.
Devuelve las imágenes procesadas directamente al canal de Discord.
Comandos
$detectar: Procesa una imagen enviada junto con el comando, detecta objetos, y responde con la imagen procesada.
Requisitos
Python 3.8 o superior.
Librerías: discord.py, imageai, opencv-python.
Modelo preentrenado yolov3.pt.
