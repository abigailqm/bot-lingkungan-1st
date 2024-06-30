import discord
from discord.ext import commands
import random
import os
import requests


# membaca token dari file
with open("token.txt", "r") as f:
    token = f.read()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def lingkungan_rumah(ctx):
    await ctx.send(f'Memisahkan sampah organik dan nonorganik')
    
@bot.command(name='bot')
async def _bot(ctx,nama): 
    if nama == 'lingkungan_sekolah' :
     await ctx.send ("Membuang sampah pada tempatnya")

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passw(ctx, panjang = 5):
    await ctx.send(genn_pass(panjang))

@bot.command()
async def mem(ctx):
    random.choice(os.listdir("Images"))
    with open(f'Images/(img_name)', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run(token)
