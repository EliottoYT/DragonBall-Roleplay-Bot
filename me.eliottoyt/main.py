# Importaciones
import discord as ds
import json as js
import random as rnd
from discord.ext import commands as cmd
#import yaml as yml


# Utiles
async def gifs(ctx, tt: str, url: str, color):
    em = ds.Embed(title=tt, color=color)
    if url == "":
        pass
    else:
        em.set_image(url=url)
    await ctx.send(embed=em)


# Colores
verde = 0xFF000
rojo = 0xFF0000
azul = 0x0174DF
rosa = 0xFF00BF
blanco = 0xFFFFFF
plata = 0xD8D8D8
negro = 0x000000
amarillo = 0xF7FE2E


#with open('info.yml') as y:
    # Leer yml
#    info = yml.full_load(y)



dts = {}
def json():
    with open('config.json') as f:
        # Lectura json
        try:
            dts = js.load(f)
            return dts
        except:
            dts = {}
            return dts

def escribir(arch, datos):
    with open(arch, 'w') as fi:
        js.dump(datos, fi)

# Sacar path links
datos = json()
links = datos['links']
# Transformaciones
ssj = datos['links']['ssj']
ssj2 = datos['links']['ssj2']
ssj3 = datos['links']['ssj3']
ssjl = datos['links']['ssjl']
ssj4 = datos['links']['ssj4']
ssg = datos['links']['ssg']
ssgss = datos['links']['ssgss']
ssgsse = datos['links']['ssgsse']
ssgsskk = datos['links']['ssgsskk']
ssrose = datos['links']['ssrose']
mng = datos['links']['mng']
ozaru = datos['links']['ozaru']
gozaru = datos['links']['g-ozaru']
# Creador
dev_id = datos['dev-id']


# Inicio bot
desc = ''
inicio = True

bot = cmd.Bot(command_prefix='{0}'.format(datos['prefijo']), description=desc)


# Mensaje inicio
@bot.event
async def on_ready():
    print("Soy " + bot.user.name)
    print("ID: " + str(bot.user.id))
    print("<=================>")
    print('JSON:')
    print('Prefijo: ' + datos['prefijo'])
    for listaLnks in datos['links']:
        print('{0}: '.format(listaLnks))
        if listaLnks == links['ssj']:
            for i in links['ssj']:
                print('-' + i)
        elif listaLnks == links['ssj2']:
            for i in links['ssj2']:
                print('-' + i)
        elif listaLnks == links['ssj3']:
            for i in links['ssj3']:
                print('-' + i)
        elif listaLnks == links['ssj4']:
            for i in links['ssj4']:
                print('-' + i)
        elif listaLnks == links['ssjl']:
            for i in links['ssjl']:
                print('-' + i)
        elif listaLnks == links['ssg']:
            for i in links['ssg']:
                print('-' + i)
        elif listaLnks == links['ssgss']:
            for i in links['ssgss']:
                print('-' + i)
        elif listaLnks == links['ssgsse']:
            for i in links['ssgsse']:
                print('-' + i)
        elif listaLnks == links['ssgsskk']:
            for i in links['ssgsskk']:
                print('-' + i)
        elif listaLnks == links['ssrose']:
            for i in links['ssrose']:
                print('-' + i)
        elif listaLnks == links['mng']:
            for i in links['mng']:
                print('-' + i)
        elif listaLnks == links['ozaru']:
            for i in links['ozaru']:
                print('-' + i)
        elif listaLnks == links['g-ozaru']:
            for i in links['g-ozaru']:
                print('-' + i)


# Comandos
@bot.command(name="ssj")
async def ssj(ctx):
    gif = rnd.choice(links['ssj'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssj!!'.format(ctx), url=gif, color=amarillo)


@bot.command(name='ssj2')
async def ssj2(ctx):
    gif = rnd.choice(links['ssj2'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha tranformado en ssj2!!'.format(ctx), url=gif, color=amarillo)


@bot.command(name='ssj3')
async def ssj3(ctx):
    gif = rnd.choice(links['ssj3'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssj3!!'.format(ctx), url=gif, color=amarillo)


@bot.command(name='ssj4')
async def ssj4(ctx):
    gif = rnd.choice(links['ssj4'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssj4!!'.format(ctx), url=gif, color=rojo)


@bot.command(name='ssjl')
async def ssjl(ctx):
    gif = rnd.choice(links['ssjl'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssjl!!'.format(ctx), url=gif, color=verde)


@bot.command(name='ssg')
async def ssg(ctx):
    gif = rnd.choice(links['ssg'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssg!!'.format(ctx), url=gif, color=rojo)


@bot.command(name='ssgss')
async def ssgss(ctx):
    gif = rnd.choice(links['ssgss'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssgss!!'.format(ctx), url=gif, color=azul)


@bot.command(name='ssgsse')
async def ssgsse(ctx):
    gif = rnd.choice(links['ssgsse'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssgsse!!'.format(ctx), url=gif, color=azul)


@bot.command(name='ssgsskk')
async def ssgsskk(ctx):
    gif = rnd.choice(links['ssgsskk'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssgsskk!!'.format(ctx), url=gif, color=azul)


@bot.command(name='ssrose')
async def ssrose(ctx):
    gif = rnd.choice(links['ssrose'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ssrose!!'.format(ctx), url=gif, color=rosa)


@bot.command(name='mng')
async def mng(ctx):
    gif = rnd.choice(links['mng'])
    await gifs(ctx=ctx, tt='**{0.author.name}** ha conseguido el migatte no gokui!!'.format(ctx), url=gif, color=plata)


@bot.command(name='ozaru')
async def ozaru(ctx):
    gif = rnd.choice(links['ozaru'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ozaru!!'.format(ctx), url=gif, color=negro)


@bot.command(name='g-ozaru')
async def gozaru(ctx):
    gif = rnd.choice(links['g-ozaru'])
    await gifs(ctx=ctx, tt='**{0.author.name}** se ha transformado en ozaru dorado!!'.format(ctx), url=gif,
               color=amarillo)


# <------PREFIJO------->
@bot.command(name='set-prefix')
async def set_prefix(ctx, pr):
    dato = {"prefijo": pr}
    if pr == datos['prefijo']:
        await ctx.send(embed=ds.Embed(title='**NO PUEDES CAMBIAR EL PREFIJO POR EL MISMO**', color=rojo))
    else:
        escribir(arch='config.json', datos=dato)
        await ctx.send(embed=ds.Embed(title='**EL PREFIJO HA SIDO CAMBIADO POR {0}**'.format(datos['prefijo']),color=verde))

# <------MARCA DE AGUA------->
@bot.command(name='creator')
async def creator(ctx):
    await ctx.send('Mi creador es <@' + dev_id + '>')

# <------Repositorio GitHub------->
@bot.command(name='github')
async def github(ctx):
    await ctx.send('Repositorio GitHub: https://github.com/EliottoYT/DragonBall-Roleplay-Bot')

# Encender bot
if inicio:
    bot.run(datos['token'])
