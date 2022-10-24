import discord
from discord.ext import commands
import youtube_dl
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN= os.getenv("MOGPDB_TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix ="/", description = "On découvre python c nice",intents=intents)
ytdl = youtube_dl.YoutubeDL()

# Start of the bot
@bot.event
async def on_ready():
    print("--- Ready ---")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Netflix"))
    channel = bot.get_channel(963007190308892702)
    await channel.send("< ON >",delete_after=15)

# Clear command
@bot.command(aliases= ['clear','clr']) 
@commands.has_permissions(manage_messages=True)
async def Clear(ctx,amount: int = None):
    if amount == None:
        await ctx.channel.purge(limit=1000000)
    else:
       await ctx.channel.purge(limit=amount+1)

# Greetings command
@bot.command
async def Hi(ctx):
    await ctx.send(f"Hello there {ctx.author.mention} !", )

# InfoServer command
@bot.command(aliases= ['Info'])
async def InfoServeur(ctx):
    server = ctx.guild
    message = f"Le serveur **{server.name}** contient {server.member_count} personnes. \nLe serveur possède {len(server.text_channels)} salons textuels et {len(server.voice_channels)} salons vocaux."
    await ctx.send(message)



bot.run(TOKEN)
