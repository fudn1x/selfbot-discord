import discord
from discord.ext import commands
import asyncio
import random
import re

token = input("🔐 Cole seu token ").strip()

bot = commands.Bot(command_prefix="!", self_bot=True)

MIN_DELAY = 1.5
MAX_DELAY = 3.5

def log(msg):
    print(f"[SELFLOG] {msg}")

async def safe_delete(message):
    try:
        await message.delete()
        log(f"✔️ Apagada: {message.content[:30]}")
        await asyncio.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
        return True
    except Exception as e:
        log(f"❌ Erro: {e}")
        return False

@bot.event
async def on_ready():
    print(f"\n✅ Logado como: {bot.user}")
    print("📦 Comandos: !nuke, !apagar <n>, !apagarpalavra <txt>, !apagarlinks")

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    count = 0
    async for msg in ctx.channel.history(limit=1000):
        if msg.author == bot.user:
            if await safe_delete(msg):
                count += 1
    await ctx.send(f"💣 Nuke finalizado: {count} mensagens apagadas", delete_after=6)

@bot.command()
async def apagar(ctx, quantidade: int = 50):
    await ctx.message.delete()
    count = 0
    async for msg in ctx.channel.history(limit=quantidade):
        if msg.author == bot.user:
            if await safe_delete(msg):
                count += 1
    await ctx.send(f"🧹 Apaguei {count} mensagens com segurança", delete_after=5)

@bot.command()
async def apagarpalavra(ctx, *, palavra):
    await ctx.message.delete()
    count = 0
    async for msg in ctx.channel.history(limit=1000):
        if msg.author == bot.user and palavra.lower() in msg.content.lower():
            if await safe_delete(msg):
                count += 1
    await ctx.send(f"🧹 Apaguei {count} mensagens com '{palavra}'", delete_after=5)

@bot.command()
async def apagarlinks(ctx):
    await ctx.message.delete()
    regex = re.compile(r'https?://')
    count = 0
    async for msg in ctx.channel.history(limit=1000):
        if msg.author == bot.user and regex.search(msg.content):
            if await safe_delete(msg):
                count += 1
    await ctx.send(f"🔗 Apaguei {count} mensagens com links", delete_after=5)

bot.run(token, log_handler=None)
