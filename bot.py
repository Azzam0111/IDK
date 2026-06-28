import discord
 
from bot_logic import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan memindahkan hak istimewa
client = discord.Client(intents=intents)
 
 
# Setelah bot siap, ia akan mencetak namanya!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}') 
 



# Saat bot menerima pesan, bot akan mengirimkan pesan di saluran yang sama!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Saya! Saya bot!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startwith('rocket'):
        await message.channel.send("\U0001F680")
    elif message.content.startswith('$help'):
        await message.channel.send("Perintah yang tersedia: $hello, $smile, $coin, $pass, $help")
    elif message.content.startswith('kapan kursus python saya dimulai'):
        await message.channel.send("Kursus python anda dimulai pada setiap hari minggu malam tepat pada jam 07.00") 
        await message.channel.send("Jangan lupa untuk menyiapkan laptop anda karena sebentar lagi kursus akan segera dimulai")
    else:
        await message.channel.send("Tidak dapat memproses perintah ini, maaf")
 
client.run("ADADEH")
