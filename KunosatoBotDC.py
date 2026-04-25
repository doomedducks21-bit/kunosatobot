
import discord
import logging
import os
from discord.ext import commands
from dotenv import load_dotenv
import webserver
webserver.keep_alive()
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
@bot.hybrid_command(name="chefs_kiss", description="meal")
@discord.app_commands.allowed_installs(guilds=True,users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def chef_g(ctx):
    glink = "https://cdn.discordapp.com/attachments/1473382001573625906/1489007834606731365/caption.gif?ex=69ed2c9c&is=69ebdb1c&hm=1ce9a1e11068b7dfd6a107b14af1a51192a7dee6a2ac13d1e655c00e415d2bbc&"
    embed1 = discord.Embed(url=glink, title="CLICK ON A GIF THEN PRESS THE ARROWS TO GET MORE, THERE IS 10 IN THIS SECTION")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1046810298075582518/1473369102549516389/caption.gif?ex=69eda127&is=69ec4fa7&hm=b5f5c4e34ada4b6dc8b28ea2cc550b9b617a9e48e445265c8911fa01aebb0a45")
    embed2 = discord.Embed(url=glink, title="Meal Gallery")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/1420498313555480606/1422979708462829568/caption.gif?ex=69ed90e0&is=69ec3f60&hm=02d66cc40c125b54ce34195003d07f7481d695c73d9909b92d0d54253cb92bf4&")
    embed3 = discord.Embed(url=glink, title="Meal Gallery")
    embed3.set_image(url="https://media.discordapp.net/attachments/1046810298075582518/1470894512330117173/togif.gif?ex=69eddb03&is=69ec8983&hm=e47029116a3fc875d69e7ad70ed227d129fa947d136163fe1afa4a02664caa5e&=&width=190&height=300")
    embed4 = discord.Embed(url=glink, title="Meal Gallery")
    embed4.set_image(url="https://media.discordapp.net/attachments/1046810298075582518/1468650873616990422/togif.gif?ex=69ed9a76&is=69ec48f6&hm=a9e753e6bda07df55fc6cd1bfd4636eb283b5bff05b9a79bb3bdbaa280f0dc0f&=&width=400&height=256")
    embed5 = discord.Embed(url=glink, title="Meal Gallery")
    embed5.set_image(url="https://media.discordapp.net/attachments/1328152654240682006/1464578459320713236/caption-48.gif?ex=69edf2fb&is=69eca17b&hm=d5bc055151aff9803fba3d5357f115b6d7799188bc5b2f19a7aabfa5a9b39b99&=")
    embed6 = discord.Embed(url=glink, title="Meal Gallery")
    embed6.set_image(url="https://media.discordapp.net/attachments/1469727517563944960/1489007455139532830/caption.gif?ex=69edd501&is=69ec8381&hm=ee66d56d33f93bd4bcf966f2cd14e89452f9aad731ae24477f918219b66050c7&=&width=211&height=300")
    embed7 = discord.Embed(url=glink, title="Meal Gallery")
    embed7.set_image(url="https://cdn.discordapp.com/attachments/1447640578123632782/1491875526531481814/caption.3535332c.gif?ex=69edb81b&is=69ec669b&hm=46f14f927fb538715230a446c1a3184d69ce024ab3ca364b3b2720501e5b5cbe&")
    embed8 = discord.Embed(url=glink, title="Meal Gallery")
    embed8.set_image(url="https://cdn.discordapp.com/attachments/1473382001573625906/1496927784453279916/togif.gif?ex=69eda463&is=69ec52e3&hm=5567157f608f665e3cc29efa37405af585abb9419f7b38cd3d4231968a7ac954&")
    embed9 = discord.Embed(url=glink, title="Meal Gallery")
    embed9.set_image(url="https://cdn.discordapp.com/attachments/1046810298075582518/1473835200869044357/caption.gif?ex=69ed58fe&is=69ec077e&hm=f4bc9797ca9b48a57e1a50344b8bcbbde56f4f8cce4b5b363f7416c22972c117&")
    embed10 = discord.Embed(url=glink, title="Meal Gallery")
    embed10.set_image(url="https://media.discordapp.net/attachments/1104321989100974163/1495188822898638928/IMG_3943.gif?ex=69ede85a&is=69ec96da&hm=5543273932ff42b57d8dee42bfed1bc144c2aaafa0a5f7b6845e18197b930e81&=")
    await ctx.send(f"CLICK ON A GIF THEN PRESS THE ARROWS TO GET MORE, THERE IS 10 IN THIS SECTION",embeds=[embed1,embed2,embed3,embed4,embed5,embed6,embed7,embed8,embed9,embed10],ephemeral=True)

@bot.hybrid_command(name="roblox_fun_pack",description="welcome to roblox friend")
@discord.app_commands.allowed_installs(guilds=True,users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def roblox_g(ctx):
    glink = "https://cdn.discordapp.com/attachments/1473382001573625906/1489007834606731365/caption.gif?ex=69ed2c9c&is=69ebdb1c&hm=1ce9a1e11068b7dfd6a107b14af1a51192a7dee6a2ac13d1e655c00e415d2bbc&"
    embed1 = discord.Embed(url=glink, title="Roblox create imagine explore")
    embed1.set_image(url="https://cdn.discordapp.com/attachments/1157023650457862247/1157029193385783379/ezgif-5-b998c47733.gif?ex=69edb828&is=69ec66a8&hm=48f3e9a64feec97559bc39dd63391d0d01384173f8041f1a57bef9b3282e438f&")
    embed2 = discord.Embed(url=glink, title="Roblox create imagine explore")
    embed2.set_image(url="https://media.discordapp.net/attachments/1160217148883480657/1245450450552225856/ezgif.com-video-to-gif-converter.gif?ex=69edb6de&is=69ec655e&hm=19b30fe761436a0f0395ddc86bfca69247d1e8af22b8e810ff744c3b23df519e&=")
    embed3 = discord.Embed(url=glink, title="Roblox create imagine explore")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/1473382001573625906/1490324209522704424/caption.gif?ex=69ee0214&is=69ecb094&hm=f5f8ad3f368271ea56be41114d674da4201778f00b352676c00233b5eb73ad74&")
    embed4 = discord.Embed(url=glink, title="Roblox create imagine explore")
    embed4.set_image(url="https://media.discordapp.net/attachments/1006632209232437272/1280565098594701415/ezgif-6-8e22c3abd1.gif?ex=69ed946f&is=69ec42ef&hm=8e75dfcfa8452b623de5c0d08f1ef27627631a41c06de84141710f00672b30be&")
    await ctx.send(embeds=[embed1,embed2,embed3,embed4],ephemeral=True)
@bot.hybrid_command(name="methods",description="Is that you... Ibrahim?")
@discord.app_commands.allowed_installs(guilds=True,users=True)
@discord.app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def method_g(ctx):
    glink = "https://cdn.discordapp.com/attachments/1473382001573625906/1489007834606731365/caption.gif?ex=69ed2c9c&is=69ebdb1c&hm=1ce9a1e11068b7dfd6a107b14af1a51192a7dee6a2ac13d1e655c00e415d2bbc&"
    embed1 = discord.Embed(url=glink, title="Ibrahim's methods!")
    embed1.set_image(url="https://media.discordapp.net/attachments/934630543637762109/965466390200975360/caption.gif?ex=69ed9224&is=69ec40a4&hm=45a7a2eee30a43b75058c2fcbfff5ad3c17be6543b8f96b6ce81d0b6c2371bee&")
    embed2 = discord.Embed(url=glink, title="Roblox create imagine explore")
    embed2.set_image(url="https://cdn.discordapp.com/attachments/878431660822110238/1261831129695125544/attachment_6.gif?ex=69edfb11&is=69eca991&hm=a636c68763fd7fd6b0f3dc98387fab93d0701dcb2802f253e1f215dac58e736b&")
    embed3 = discord.Embed(url=glink, title="Roblox create imagine explore")
    embed3.set_image(url="https://cdn.discordapp.com/attachments/860539149046906920/1274456254554574899/ezgif.com-crop.gif?ex=69edc4a1&is=69ec7321&hm=10bf6f958b346266b9552d5a759c16abb820c74d3a4189daed995dd0b4a97eb4&")
    embed4 = discord.Embed(url=glink, title="Roblox create imagine explore")
    embed4.set_image(url="https://media.discordapp.net/attachments/893508396718911511/1152971856735903826/nBOuHUOW.gif?ex=69ed75f7&is=69ec2477&hm=06fdedbb4fe243e9fed4c92228f904ac46a437efa1baa2d1faed7e53e64ba63e&")
    await ctx.send(embeds=[embed1,embed2,embed3,embed4],ephemeral=True)

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
