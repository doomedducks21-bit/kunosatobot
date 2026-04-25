import dis
import discord
import logging
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
handler = logging.FileHandler(filename="discord.log", encoding="UTF-8", mode="w")


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    try:
        
        await bot.tree.sync()
        print("Global Sync Complete")
    except Exception as e:
        print(f"Sync Error: {e}")


@bot.hybrid_command(name="help_me") 
@discord.app_commands.allowed_installs(guilds=True, users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def help_me(ctx):
    await ctx.send("This bot is developed by duahopp tech. You do not need help bum ass nigger")

@bot.hybrid_command(name="the_butcher", description="The butcher revives")
@discord.app_commands.allowed_installs(guilds=True, users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def the_butcher(ctx):
    link = "https://cdn.discordapp.com/attachments/1473382001573625906/1489007834606731365/caption.gif?ex=69ed2c9c&is=69ebdb1c&hm=1ce9a1e11068b7dfd6a107b14af1a51192a7dee6a2ac13d1e655c00e415d2bbc&"
    await ctx.send(f"The Butcher: {link}", ephemeral=True)
@bot.hybrid_command(name="butcher_gallery",description="all de butchers")
@discord.app_commands.allowed_installs(guilds=True,users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def butcher_g(ctx):
    glink = "https://cdn.discordapp.com/attachments/1473382001573625906/1489007834606731365/caption.gif?ex=69ed2c9c&is=69ebdb1c&hm=1ce9a1e11068b7dfd6a107b14af1a51192a7dee6a2ac13d1e655c00e415d2bbc&"
    embed1 = discord.Embed(url=glink, title="Butcher Gallery")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1473382001573625906/1489007834606731365/caption.gif?ex=69ed2c9c&is=69ebdb1c&hm=1ce9a1e11068b7dfd6a107b14af1a51192a7dee6a2ac13d1e655c00e415d2bbc&")
    embed2 = discord.Embed(url=glink, title="Butcher Gallery")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/1473382001573625906/1495068734203891752/caption.gif?ex=69eccfc3&is=69eb7e43&hm=6453366eefe9eb68be980a33e56a8039b9ad9f241ee538958edf5f9803d99817&")
    embed3 = discord.Embed(url=glink, title="Butcher Gallery")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/1473382001573625906/1495068549872619571/caption.gif?ex=69eccf97&is=69eb7e17&hm=26d39fbbfe2b2a147957401ca4899d2d4f4fdbc7fb3a04d5ccfd72726f891413&")
    embed4 = discord.Embed(url=glink, title="Butcher Gallery")
    embed4.set_image(url="https://cdn.discordapp.com/attachments/1473382001573625906/1479984517153296476/caption.gif?ex=69ed4e7d&is=69ebfcfd&hm=33cfd25d7b6c5e7ec123be930d0c4d7c720dd4faceca2ec936700af871ef4afc&")
    await ctx.send(embeds=[embed1,embed2,embed3,embed4],ephemeral=True)
    
bot.run(token, log_handler=handler, log_level=logging.DEBUG)