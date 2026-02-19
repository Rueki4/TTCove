import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
import requests
import random
import cv2
import numpy as np

def crear_randomizador(tag : str) -> str:
    def nueva_funcion():
        
        last_soup_str = ":("
        error_code = 0
        try:
            url = "https://rule34.xxx/index.php?page=post&s=list&tags=" + tag + "+&pid=0"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }

            resp = requests.get(url, headers=headers)
            soup = BeautifulSoup(resp.text, "html.parser")

            soup_str = str(soup).split("\n")
            error_code = 1
            
            for i in range(len(soup_str)):
                if ";pid=" in soup_str[i]:
                    error_code = 2
                    last_pid = soup_str[i].split('pid=')[-1].split('"')[0]
                    if int(last_pid) > 200000:
                        last_pid = "200000"
                    pid = random.randint(0, int(last_pid))
                    url = f"{url[0:-1]}{pid}"

                    # print(f"{last_pid} -> {pid}")
                    
                    
                    resp = requests.get(url, headers=headers)
                    soup = BeautifulSoup(resp.text, "html.parser")
                    error_code = 3

                    new_soup_str = str(soup).split("\n")
                    error_code = 4
                    for j in range(len(new_soup_str)):
                        if "score" in new_soup_str[j]:
                            code = new_soup_str[j].split("?")[1].split('"')[0]
                            break
                    # print(code)
                    error_code = 5
                    url = f"https://rule34.xxx/index.php?page=post&s=view&id={code}"
                    error_code = 6
                    resp = requests.get(url, headers=headers)
                    error_code = 7
                    soup = BeautifulSoup(resp.text, "html.parser")
                    error_code = 8

                    last_soup_str = "https://wimg." + str(soup).split("https://wimg.")[1].split('"')[0]
        except:
            last_soup_str = error_code
        return last_soup_str
    return nueva_funcion

def random_de(tag : str, canal : str) -> str:
    try:
        url = "https://rule34.xxx/index.php?page=post&s=list&tags=" + tag + "+&pid=0"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")

        soup_str = str(soup).split("\n")
        indice_pass = 0
        for i in range(len(soup_str)):
            if ";pid=" in soup_str[i]:
                last_pid = soup_str[i].split('pid=')[-1].split('"')[0]
                pid = random.randint(0, int(last_pid))
                url = f"{url[0:-1]}{pid}"
                
                resp = requests.get(url, headers=headers)
                soup = BeautifulSoup(resp.text, "html.parser")

                new_soup_str = str(soup).split("\n")
                for j in range(len(new_soup_str)):
                    if "score" in new_soup_str[j]:
                        code = new_soup_str[j].split("?")[1].split('"')[0]
                        break
                url = f"https://rule34.xxx/index.php?page=post&s=view&id={code}"
                resp = requests.get(url, headers=headers)
                soup = BeautifulSoup(resp.text, "html.parser")

                last_soup_str = "https://wimg." + str(soup).split("https://wimg.")[1].split('"')[0]
    except:
        last_soup_str = "Enjoying the goon sesion?"
    return last_soup_str

def crear_interaccion(ctx : any) -> str:
    if len(ctx.message.mentions) != 0:
        name = str(ctx.message.mentions)
        
        print(name)
        name = '<@'+name.split(" ")[1][3:]+'>'
        author = '<@' + str(ctx.author.id) + '>'
    
        if name == '<@1385775560063451227>':
            message = 1,"",""
        elif name == author:
            message = 2,name,author
        else:
            message = 3,name,author
    
    else:
        message = 1,"",""
    
    return message


def obtener_interaction_index(matriz : list, interaccion : str):
    for i in range(len(matriz[0])):
        if matriz[0][i] == interaccion:
            return i



# def testing_imagenes():

#     # --- Entradas ---
#     import cv2, numpy as np

#     img = cv2.imread("aaa/normal.png")
#     mask = cv2.imread("aaa/blancoynegro.png", 0)        # blanco = pelo
#     varmap = cv2.imread("aaa/escala.png", 0)      # 0..255 controla fuerza local

#     # Parámetros del tinte
#     target_hue = 120        # 0..179 (OpenCV HSV): 120 ~ azul
#     sat_boost  = 1.3        # saturación del pelo
#     val_boost  = 1.0        # brillo del pelo

#     # Preparación
#     mask01 = (mask > 128).astype(np.float32)
#     alpha  = (varmap.astype(np.float32)/255.0) * mask01   # 0..1

#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
#     H,S,V = hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]

#     # Mezcla: empuja el tono hacia el objetivo según alpha
#     H_new = H*(1-alpha) + target_hue*alpha
#     S_new = np.clip(S*(1 + (sat_boost-1)*alpha), 0, 255)
#     V_new = np.clip(V*(1 + (val_boost-1)*alpha), 0, 255)

#     out = cv2.cvtColor(np.stack([H_new,S_new,V_new],2).astype(np.uint8), cv2.COLOR_HSV2BGR)
#     cv2.imwrite("pelo_tenido_variacion.png", out)

# testing_imagenes()