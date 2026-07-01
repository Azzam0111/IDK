from email import message
import base64
import discord
import random
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Semua data emoji disimpan di satu tempat ini
DAFTAR_EMOJI = {
    "fire": "🔥", "stone": "🗿", "happy": "😀", "sad": "😭", "love": "❤️", "rocket": "🚀", "smile": "😊", "thumbs": "👍",
    "clap": "👏", "laugh": "😂", "lol": "🤣", "tired": "😴", "angry": "😡", "lazy": "😪", "poop": "💩", "cry": "😢",
    "cool": "😎", "cringe": "😬", "party": "🥳", "clown": "🤡", "think": "🤔", "sick": "🤢", "hoek": "🤮", "confused": "😕", "shocked": "😱", 
      
} 
# Daftar kata kasar sudah disembunyikan dalam bentuk teks acak
_rahasia = "YW5qaW5nLGJhYmksYmFuZ3NhdCxrb250b2wsam9oLGFzdSxwdWtpLHB1a2ltYWstdGFpLHJhaW11LG1hdGFtdSxiYWppbmdhbixiYW5na2U="

# Kode ini otomatis mengembalikan teks acak di atas menjadi daftar kata semula saat program berjalan
KATA_KASAR = base64.b64decode(_rahasia).decode('utf-8').split(',')

lasttime_user = {} 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content_lower = message.content.lower() 

    # FITUR ANTI-TOXIC: Memeriksa apakah ada kata kasar di dalam kalimat user
    # Menggunakan loop 'any' agar bot tetap mendeteksi meskipun kata kasarnya ada di tengah kalimat
    if any(kata in content_lower for kata in KATA_KASAR):
        try:
            await message.delete() # Menghapus pesan toxic tersebut
            # Menegur user yang mengetik kata kasar
            await message.channel.send(f"Heii {message.author.mention}, jaga ucapanmu ya! 🤫❌", delete_after=5)
        except discord.Forbidden:
            # Jika bot tidak punya izin 'Manage Messages' di server Discord
            print("Bot tidak memiliki izin untuk menghapus pesan!")
        return
    
    ontime = time.time()
    user_id = message.author.id
    
    if user_id in lasttime_user:
        lasttime = lasttime_user[user_id]
        if ontime - lasttime < 3:  # Jika user mengirim pesan dalam waktu kurang dari 5 detik
            await message.delete()  # Menghapus pesan spam tersebut
            await message.channel.send(f"Heii {message.author.mention}, jangan spam ya! ⏱️❌", delete_after=5)
            return
        
    lasttime_user[user_id] = ontime  # Update waktu terakhir user mengirim pesan
    
    choosen_emoji = DAFTAR_EMOJI.get(content_lower)

    if choosen_emoji:
        await message.channel.send(choosen_emoji)
        return
    
    await bot.process_commands(message)  # Memastikan perintah bot tetap diproses

    if message.content.startswith('kapan kursus python saya dimulai'):
        await message.channel.send("Kursus python anda dimulai pada setiap hari minggu malam tepat pada jam 07.00") 
        await message.channel.send("Jangan lupa untuk menyiapkan laptop anda karena sebentar lagi kursus akan segera dimulai")
    elif message.content.startswith('juni j nya apa'):
        await message.channel.send("JUST FRIEND YAA HAHAHAAHAAHA KASIAN DEH LOo🤣🫵🫵🫵🫵")

 

@bot.command()
async def hello(ctx):
    """Says hello."""
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh: int =5):
    """Repeats 'he' a specified number of times."""
    if count_heh > 50:
        await ctx.send("the maximum number is 50 so that the bot is not Error")
        return   
    else:
        await ctx.send("he" * count_heh)

@bot.command()
async def bye(ctx):
    """Draw Random Emoji"""
    await ctx.send("\U0001f642")

@bot.command()
async def roket(ctx):
    """Send Rocket Emoji"""
    await ctx.send("\U0001F680")

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')
 

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


bot.run("Taruh Tokeh Anda Disini")
