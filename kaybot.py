# bot.py
import os
import random
import subprocess
import discord
from discord.ext import commands

tokentxt = open('kaybot-token.txt', 'r')
TOKEN = (tokentxt.read())
tokentxt.close()

bot = commands.Bot()
@bot.slash_command(name="neofetch", guild_ids=[561696799950241792])
async def neofetch(ctx):
    neofetchOut = subprocess.getoutput("neofetch --stdout")
    await ctx.respond(neofetchOut)

@bot.slash_command(name="uname", guild_ids=[561696799950241792])
async def uname(ctx):
    unameOut = subprocess.getoutput("uname -a")
    await ctx.respond(unameOut)

@bot.slash_command(name="pingdns", guild_ids=[561696799950241792])
async def pingdns(ctx):
    pingOut = subprocess.getoutput("ping -c 1 -W 3 8.8.8.8")
    await ctx.respond(pingOut)

@bot.slash_command(name="homefilecount", guild_ids=[561696799950241792])
async def homefilecount(ctx):
    fileOut = subprocess.getoutput("find ~/ -type f | wc -l")
    await ctx.respond(fileOut + " files in the current user's home directory")

@bot.slash_command(name="lsusb", guild_ids=[561696799950241792])
async def lsusb(ctx):
    lsusbOut = subprocess.getoutput("lsusb")
    await ctx.respond(lsusbOut)

@bot.slash_command(name="lspci", guild_ids=[561696799950241792])
async def lspci(ctx):
    lspci = subprocess.getoutput("lspci")
    await ctx.respond(lspci)

@bot.slash_command(name="lsblk", guild_ids=[561696799950241792])
async def lsblk(ctx):
    lsblk = subprocess.getoutput("lsblk")
    await ctx.respond(lsblk)

bot.run(TOKEN)
