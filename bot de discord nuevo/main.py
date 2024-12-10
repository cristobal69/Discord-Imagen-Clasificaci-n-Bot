import discord
from discord.ext import commands
from imageai.Detection import ObjectDetection
import cv2
import os

# Configuración del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# Inicializar el detector
def inicializar_detector():
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("yolov3.pt")  # Asegúrate de que este archivo esté en el mismo directorio
    detector.loadModel()
    return detector

# Crear la instancia del detector
detector = inicializar_detector()

@bot.event
async def on_ready():
    print(f'Bot iniciado como {bot.user}')

@bot.command()
async def detectar(ctx):
    # Verificar si se subió una imagen
    if not ctx.message.attachments:
        await ctx.send("Por favor, sube una imagen junto con el comando.")
        return

    # Descargar la imagen subida
    attachment = ctx.message.attachments[0]
    input_path = "input_image.jpg"
    output_path = "output_image_with_text.jpg"
    await attachment.save(input_path)

    # Detectar objetos en la imagen
    detections = detector.detectObjectsFromImage(
        input_image=input_path,
        output_image_path=output_path,
        minimum_percentage_probability=30,
    )

    # Añadir texto en caso de detección de autos
    image = cv2.imread(output_path)
    texto_agregado = False
    for detection in detections:
        if detection['name'] == "car" and not texto_agregado:
            box_points = detection['box_points']
            top_left = (box_points[0], box_points[1])
            cv2.putText(image, "Espera o pare", (top_left[0], top_left[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            texto_agregado = True

    # Guardar la imagen procesada con texto
    cv2.imwrite(output_path, image)

    # Enviar la imagen procesada al canal
    await ctx.send("Aquí está la imagen procesada:", file=discord.File(output_path))

    # Limpiar archivos temporales
    os.remove(input_path)
    os.remove(output_path)

# Reemplaza "TOKEN" con tu token real
bot.run("MTI1NzQ4NDAwMzEyMDkwNjI5Mg.GPH_kB.l_9E96pI0j1SRv2axi007wnEZYlnWA4ajQM1Tg")