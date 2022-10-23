import discord
from discord.ext import commands
import youtube_dl


bot = commands.Bot(command_prefix ="$", description = "On découvre python c nice",intents=intents)
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print("--- Ready ---")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Netflix"))
    channel = bot.get_channel(963007190308892702)
    await channel.send("< ON >",delete_after=10)
    

bot.run("OTYzMzg1MTY3MjgyNTg5NzA3.YlVUWg.DAEkTP7NxDCOdSbbd6n6Qpg9o-U")