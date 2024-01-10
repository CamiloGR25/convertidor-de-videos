from moviepy.editor import VideoFileClip #edicion de videos
import os #modulo para usar funciones dependientes del sistema operativo

def convertirFormato(archivo, nombre):

    ruta=os.path.join("videos", archivo) #obtener la ruta del video
    video=VideoFileClip(ruta)#lee el video
    #resolucion_original = video.size #obtiene la resolución original del video
    
    #Convertir el video en otro formato 
    video.write_videofile(os.path.join("salida", nombre+nuevo_tipo_archivo))
    #video.resize(resolucion_original[0], resolucion_original[1]).write_videofile(nombre+nuevo_tipo_archivo)

videos=os.listdir("videos") #guarda los archivos de la carpeta videos

tipo_archivo=".MOV"
nuevo_tipo_archivo=".mp4"


for video in videos:
    if video.endswith(tipo_archivo):
        nombre, extension = os.path.splitext(video)
        convertirFormato(video, nombre)