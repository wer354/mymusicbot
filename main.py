import discord
import os
from discord.ext import commands
from keepalive import keep_alive

client = commands.Bot(command_prefix = "$")

@client.command()
async def play(ctx, url : str, channel):
  voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = channel)

  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  if not voice.is_connected():
      await voiceChannel.connect()

@client.command()
async def leave(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  if voice.is_connected():
    await voice.disconnect
  else:
    await ctx.send("Error: Bot not connected to a voice channel")

@client.command()
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  if voice.is_playing():
    voice.pause()
  else: 
    await ctx.send("Error: No audio playing.")

@client.command()
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

  if voice.is_paused():
    voice.resume()
  else:
    await ctx.send("Error: Audio is not paused.")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run(os.getenv('TOKEN'))
keep_alive()