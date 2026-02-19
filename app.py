import discord
from discord.ext import commands, tasks
import threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from bs4 import BeautifulSoup
import requests
import funciones
import os
from auto_iniciar import hardcodeo
import leer_gs
import random

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

# 2) Arranca el servidor en un hilo aparte
def start_health_server():
    port = int(os.environ.get('PORT', 8080))
    server = ThreadingHTTPServer(('0.0.0.0', port), HealthHandler)
    server.serve_forever()

interaction_gifs = leer_gs.obtener_interaction_gifs()



if __name__ == '__main__':
    # Inicia el health-check server
    threading.Thread(target=start_health_server, daemon=True).start()
    index = -1
    intents = discord.Intents.all()
    intents.messages = True
    intents.members = True

    bot = commands.Bot(command_prefix="'", intents=intents, allowed_contexts="users", help_command=None)
    lista_auto = hardcodeo()
    # lista_auto = []

    @bot.event
    async def on_ready():
        print(f"Conectado como {bot.user}")
        lista_automatica.start() 
        actividad = discord.Activity(
        name="'commandlist for the command list",
        type=discord.ActivityType.listening  # playing, streaming, listening, watching, competing
        )
        await bot.change_presence(
            status=discord.Status.idle,   # online, idle, dnd, invisible
            activity=actividad
        )

    @tasks.loop(minutes = 30)
    async def lista_automatica():
        for i in range(len(lista_auto)):
            content = ":("
            intentos = 0
            while content == ":(" and intentos < 4:
                content = lista_auto[i]["funcion"]()
                intentos += 1
            canal = bot.get_channel(lista_auto[i]["canal"])
            if canal:
                await canal.send(content)

    @bot.command()
    async def randomrule(ctx, tag : str = ""):
        global lista_auto
        nuevo_diccionario = {}
        nuevo_diccionario["funcion"] = funciones.crear_randomizador(tag)
        nuevo_diccionario["canal"] = ctx.channel.id
        lista_auto.append(nuevo_diccionario)

    @bot.command()
    async def deleterandom(ctx):
        global lista_auto
        for i in range(len(lista_auto)):
            if lista_auto[i]["canal"] == ctx.channel.id:
                lista_auto.pop(i)
                break
    @bot.command()
    async def rule(ctx, tag : str, score : int = 0):

        await ctx.send(funciones.random_de(tag, ctx.channel.id, score))
    
    @bot.command()
    async def info(ctx):
        await ctx.send('A bot just for u ♥, By Rueki')

    @bot.command()
    async def hug(ctx):
        mensaje = funciones.crear_interaccion(ctx)
        if mensaje[0] == 1:
            mensaje = "You need to mention someone who is real..."
        elif mensaje[0] == 2:
            mensaje = "Okay... that's a bit sad..."
        else:
            mensaje = f"{mensaje[2]} gave {mensaje[1]} a warm hug."
            indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "hug")
            my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
            my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def kill(ctx):
        mensaje = funciones.crear_interaccion(ctx)
        if mensaje[0] == 1:
            mensaje = "You need to mention someone who is real..."
        elif mensaje[0] == 2:
            mensaje = "Hey... Do you need help?"
        else:
            mensaje = f"{mensaje[2]} killed {mensaje[1]} D:"
            indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "kill")
            my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
            my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def fuck(ctx):
        if(ctx.channel.is_nsfw()):
            mensaje = funciones.crear_interaccion(ctx)
            if mensaje[0] == 1:
                mensaje = "You need to mention someone who is real..."
            elif mensaje[0] == 2:
                mensaje = "Self-love is also important"
            else:
                mensaje = f"{mensaje[2]} fucked {mensaje[1]} with a lot of passion~"
                indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "fuck")
                my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
                my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        else:
            mensaje = "Get yourself a room... (This channel is SFW)"
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def commandlist(ctx):
        my_embed = discord.Embed(title="Command List", description="hug \n" \
        "kiss \n" \
        "slap \n" \
        "leanin \n" \
        "pat \n" \
        "kill \n"
        "----- \n" \
        "fuck \n" \
        "grabbutt \n" \
        "lick \n" \
        "tie\n")
        await ctx.send(embed = my_embed)

    @bot.command()
    async def lick(ctx):
        if(ctx.channel.is_nsfw()):
            mensaje = funciones.crear_interaccion(ctx)
            if mensaje[0] == 1:
                mensaje = "You need to mention someone who is real..."
            elif mensaje[0] == 2:
                mensaje = f"{mensaje[2]}... is he licking oneself?"
            else:
                mensaje = f"{mensaje[2]} licked {mensaje[1]}~"
                indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "lick")
                my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
                my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        else:
            mensaje = "Get yourself a room... (This channel is SFW)"
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)
    @bot.command()
    async def grabbutt(ctx):
        if(ctx.channel.is_nsfw()):
            mensaje = funciones.crear_interaccion(ctx)
            if mensaje[0] == 1:
                mensaje = "You need to mention someone who is real..."
            elif mensaje[0] == 2:
                mensaje = f"{mensaje[2]} touches themself ass, tempting~"
            else:
                mensaje = f"{mensaje[2]} grabs {mensaje[1]} ass <:ButtGrab:1394329433568968754>"
                indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "grabbutt")
                my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
                my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])

        else:
            mensaje = "Get yourself a room... (This channel is SFW)"
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def tie(ctx):
        if(ctx.channel.is_nsfw()):
            mensaje = funciones.crear_interaccion(ctx)
            if mensaje[0] == 1:
                mensaje = "You need to mention someone who is real..."
            elif mensaje[0] == 2:
                mensaje = f"everyone has the right to their own fetishes..."
            else:
                mensaje = f"{mensaje[2]} tied {mensaje[1]} tightly~"
                indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "tie")
                my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
                my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        else:
            mensaje = "Get yourself a room... (This channel is SFW)"
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def kiss(ctx):
        mensaje = funciones.crear_interaccion(ctx)
        if mensaje[0] == 1:
            mensaje = "You need to mention someone who is real..."
        elif mensaje[0] == 2:
            mensaje = f"{mensaje[2]} is practicing with the pillow..."
        else:
            mensaje = f"{mensaje[2]} kissed {mensaje[1]} ♥"
            indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "kiss")
            my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
            my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def leanin(ctx):
        mensaje = funciones.crear_interaccion(ctx)
        if mensaje[0] == 1:
            mensaje = "You need to mention someone who is real..."
        elif mensaje[0] == 2:
            mensaje = f"Yes... You can't do it alone."
        else:
            mensaje = f"{mensaje[2]} leans in {mensaje[1]} lips almost touching"
            indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "leanin")
            my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
            my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def pat(ctx):
        mensaje = funciones.crear_interaccion(ctx)
        if mensaje[0] == 1:
            mensaje = "You need to mention someone who is real..."
        elif mensaje[0] == 2:
            mensaje = f"{mensaje[2]} is needing love."
        else:
            mensaje = f"{mensaje[2]} pats {mensaje[1]} ♥"
            indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "pat")
            my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
            my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)


    
    @bot.command()
    async def slap(ctx):
        mensaje = funciones.crear_interaccion(ctx)
        if mensaje[0] == 1:
            mensaje = "You need to mention someone who is real..."
        elif mensaje[0] == 2:
            mensaje = f"{mensaje[2]} is clapping?"
        else:
            mensaje = f"{mensaje[2]} slapped {mensaje[1]}! Ouch!"
            indice_nuevo = funciones.obtener_interaction_index(interaction_gifs, "slap")
            my_embed = discord.Embed(description=mensaje, url=interaction_gifs[random.randint(1,10)][indice_nuevo])
            my_embed.set_image(url = interaction_gifs[random.randint(1,10)][indice_nuevo])
        try:
            await ctx.send(embed = my_embed)
        except:
            await ctx.send(mensaje)

    @bot.command()
    async def intento(ctx, nombre : str):
        await ctx.send(nombre)

    users = {}

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        valor = users.get(message.author.id, False)
        if valor != False:
            if len(valor) > 1:
                if valor[-1].content == message.content:
                    if valor[-2].content == message.content:
                        for msg in users[message.author.id]:
                            try:
                                await msg.delete()
                            except:
                                pass
                        await message.author.kick(reason="TEST BOT- spam")
                        await message.delete()
                    else:
                        await message.channel.send(f"<@{message.author.id}> Avoid sending the same message across multiple channels. Doing so may result in a ban!")
                        await message.delete()
            elif len(valor) > 0:
                if valor[-1].content == message.content:
                    await message.channel.send(f"<@{message.author.id}> Avoid sending the same message across multiple channels. Doing so may result in a ban!")
                    await message.delete()
            
            users[message.author.id].append(message)
            if len(valor) > 5:
                valor.pop(0)
        else:
            users[message.author.id] = [message] 
        await bot.process_commands(message)

    token_a = "MTM4NTc3NTU2MDA2MzQ1MTIyNw."
    token_b = "GzW8GX.6gHVgapzMm8L40X8LQpasXj1wP8iLU7mVRfX50"
    bot.run(token_a + token_b)