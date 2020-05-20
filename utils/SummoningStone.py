import discord
from discord.ext import commands
from discord.utils import get
import time as t
#  TOKEN = input("ENTER BOT TOKEN HERE:\n")
file = open('token.txt', 'r')
for a in file:
    TOKEN = a.replace('\n','')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='"$toggle" = STOP ME'))
    global spam
    spam = True
    global password
    password = 'now'

@bot.command()
async def killswitch(ctx, password):
    await ctx.send('imma commit sudoku')
    exit('KILLSWITCH ACTIVATED')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Summoning Stone", description="Summon your friends in no time!", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="M81V4N")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # Count of all pings!
    #file.open('pingCount.txt','r')
    #embed.add_field(name='Ping count', value=str(int(file.read())))
    #file.close()

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def doom(ctx, user):
    while spam == True:
        await ctx.send(user)
        t.sleep(1.25)  # note: this is necessary, any faster and discord slaps you with 5 secs of mute
    if spam == False:
        await ctx.send('Doom finished: spamming has been toggled off.')

@bot.command()
async def toggle(ctx):
    global spam
    if spam == True:
        spam = False
        await ctx.send('Spamming is now off.')
    elif spam == False:
        spam = True
        await ctx.send('Spamming is now allowed.')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="SUMMONING STONE", description="Summons people. Made by m81v4n", color=0xeee657)

    embed.add_field(name="$doom [mention]", value="Constantly pings mentioned user. Stop it with $toggle command.")
    embed.add_field(name="$toggle", value="Toggles spamming mode.", inline=False)
    embed.add_field(name="$help", value="Shows this message.", inline=False)
    embed.add_field(name="$info", value="Display some details about me.", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)
