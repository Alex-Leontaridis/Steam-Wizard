import discord
from discord.ext import commands
import steamapi

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!',intents=intents)

steamapi.core.APIConnection(api_key="[Enter API Key]", validate_key=True)  # <-- Insert API key here

@client.event
async def on_ready():
    print("Logged in as a bot.")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Your Profile."))

@client.command()
async def check(ctx, *, arg):
    steam_user = steamapi.user.SteamUser(userurl=arg.lower())
    img = steam_user.avatar
    level = steam_user.level
    games = len(steam_user.games)
    frineds = len(steam_user.friends)
    currently_playing = (steam_user.currently_playing)
    recently_played = len(steam_user.recently_played)
    is_vac_banned = steam_user.is_vac_banned
    is_community_banned = steam_user.is_community_banned
    thumbnail = discord.File("[Enter Destination of Logo.png]", filename="logo.png")

    embedVar = discord.Embed(title=f"{steam_user}'s Profile", description=f"Check every public shown informatio of {steam_user}'s steam profile.", color=0x3c004c)
    embedVar.set_thumbnail(url='attachment://logo.png')
    embedVar.add_field(name="Level:", value=level, inline=False)
    embedVar.add_field(name="Games:", value=games, inline=False)
    embedVar.add_field(name="Frineds:", value=frineds, inline=False)
    embedVar.add_field(name="Currently Playing:", value=currently_playing, inline=False)
    embedVar.add_field(name="Recently Played:", value=recently_played, inline=False)
    embedVar.add_field(name="VAC Ban:", value=is_vac_banned, inline=False)
    embedVar.add_field(name="Community Ban:", value=is_community_banned, inline=False)
    embedVar.set_footer(text="Steam Wizard Discord Bot, made by Alexander Leontaridis.")
    await ctx.send(embed=embedVar, files=[thumbnail])
    
client.run("[Enter Token]")

