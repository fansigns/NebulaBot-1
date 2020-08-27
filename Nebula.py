import discord
import requests
import numpy
import threading
import random
import time
import os
import json
import asyncio
import functools
import itertools
import math

from colorama import Fore, init
from datetime import datetime
from itertools import cycle
from discord.ext import commands
from colorama import Fore, init, Style, Back
from discord_webhook import DiscordWebhook, DiscordEmbed

client = commands.Bot(command_prefix="x")
client.remove_command('help')
prefix = "x"
Footer = "Nebula"
init(convert=True)
guildsIds = []
friendsIds = []
clear = lambda: os.system('cls')
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
 
        for f in self.user.friends:
            friendsIds.append(f.id)

        await self.logout()

        
@client.event
async def on_ready():
    activity = discord.Game(name="Nebula | Prefix X", type=1)
    await client.change_presence(status=discord.Status.online, activity=activity)
    'cls'
    print(f'''{Fore.RESET}
    {Fore.WHITE}[{Fore.GREEN}Info{Fore.WHITE}] Logged in!
      '''+Fore.RESET)

@client.command()
async def webss(ctx, URL):
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}Web Screenshot")
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/createscreenshot?key=&url={URL}").text
    embed=discord.Embed(title=f" __**{URL} Screenshot**__ ", description=f"{r}", color=0xfa1e2e)
    await ctx.send(embed=embed)


@client.command()
async def portscan(ctx, ipadd: str):
    await ctx.message.delete()
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}Portscan")
    r = requests.get(f"https://api.c99.nl/portscanner?key=&host={ipadd}").text
    embed = discord.Embed(title=f" __**Port Scan For {ipadd}**__ ", color=0xff0000)
    embed.add_field(name="Open Ports: ", value=f"{r}", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def subscan(ctx, domain: str):
    await ctx.message.delete()
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}SubScan")
    r = requests.get(f"https://api.c99.nl/subdomainfinder?key=&domain={domain}").text
    embed = discord.Embed(title=f" __**Subdomain Scan For {domain}**__ ", color=0xff0000)
    embed.add_field(name="Sub Domains ", value=f"{r}", inline=False)
    embed.set_footer(text=f"{Footer}")
    await ctx.send(embed=embed)

@client.command()
async def geoip(ctx, ip: str):
    await ctx.message.delete()
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}Geo Ip")
    r = requests.get(url=f"http://api.ipstack.com/{ip}?access_key=54082d4a5c4de095265ba3185db4c1f4")
    if r.status_code == 200:
        if(r.json()['type'] == None):
            embed=discord.Embed(title=f"{ip} is an invalid IP", color=0xff0000)
            await ctx.send(embed=embed)
        else:
            flag = f":flag_{r.json()['continent_code'].lower()}:"
            embed=discord.Embed(title=f"{flag}  __**Whois**__  {flag}", description=f"IP | **{ip}**\n Type | **{r.json()['type']}\n Continent | **{r.json()['continent_name']}**\n Continent Code| **{r.json()['continent_code']}**\n Country| **{r.json()['country_name']}**\n Country Code| **{r.json()['country_code']}**\n Region| **{r.json()['region_name']}**\n City| **{r.json()['city']}**\n Zip| **{r.json()['zip']}**\n Latitude| **{r.json()['latitude']}**\n Longitude| **{r.json()['longitude']}**", color=0xff0000)
            embed.set_footer(text=f"{Footer}")
            await ctx.send(embed=embed)

@client.command()
async def resolve(ctx, HOST):
    await ctx.message.delete()
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}Resolve")
    r = requests.get(f"https://api.c99.nl/dnsresolver?key=&host={HOST}").text
    embed=discord.Embed(title=f" __**IP For {HOST}**__ ", description="** **", color=0xff0000)
    embed.add_field(name=f"**{r}**", value=f"** **", inline=False)
    embed.set_thumbnail(url=f"{IconURL}")
    embed.set_footer(text=f"{Footer}")
    await ctx.send(embed=embed)

@client.command()
async def ipcheck(ctx, IP):
    await ctx.message.delete()
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}IP Check")
    r = requests.get(f"https://api.c99.nl/ipvalidator?key=&ip={IP}").text
    embed=discord.Embed(title=f" __**{IP} Check**__ ", description=f"{r}", color=0xff0000)
    embed.set_thumbnail(url=f"{IconURL}")
    embed.set_footer(text=f"{Footer}")
    await ctx.send(embed=embed)

@client.command()
async def proxycheck(ctx, IP):
    await ctx.message.delete()
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}Proxy Check")
    r = requests.get(f"https://api.c99.nl/proxydetector?key=&ip={IP}").text
    embed=discord.Embed(title=f" __**{IP} Check**__ ", description=f"{r}", color=0xff0000)
    embed.set_thumbnail(url=f"{IconURL}")
    embed.set_footer(text=f"{Footer}")
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed=discord.Embed(title=f"**Commands**", description=f"\n **fun** |  `Shows all Fun Commands`\n **admin** | `Shows All Admin Commands`\n **text** | `Shows all Text Commands`\n **bot** | `All the needed bot info`\n **iptools** | `Shows all IP Tools`\n", color=0xff0000)
    embed.set_footer(text='Nebula')
    await ctx.send(embed=embed)

@client.command()
async def tools(ctx):
    embed=discord.Embed(title=f"**Tools**", description=f"\n**phonelookup** | `Looks up phone number for info`\n", color=0xff0000)
    embed.set_footer(text=f"{Footer}")
    await ctx.send(embed=embed)


@client.command()
async def iptools(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f" __**IP Tools**__ ", description=f"{prefix}**portscan [ip]** | `Portscan all open ports on an ip`\n {prefix}**geoip [ip]** | `GeoIP looks up an IP`\n {prefix}**resolve [url]** | `Gets the IP Address of a website`\n{prefix}**ipcheck [ip]** | `See if an IP is valid or not`\n {prefix}**proxycheck [ip]** | `See if an IP is a proxy or not`\n", color=0xff0000)
    await ctx.send(embed=embed)


@client.command()
async def fun(ctx):
    embed=discord.Embed(title=f"**Fun Commands**", description=f"{prefix}**joke** | `Says a joke`\n {prefix}**supreme** | `Does a supreme logo of what you said`\n {prefix}**_8ball** | `Shakes and 8ball`\n {prefix}**wyr** | `Would You Rather`\n {prefix}**dick** | `Shows the size of your dick`\n {prefix}**fml** | `Send a Fuck My life moment`\n", color=0xff0000)    
    embed.set_footer(text='Nebula')
    await ctx.send(embed=embed)

@client.command()
async def text(ctx):
    embed=discord.Embed(title=f"**Text Commands**\n", description=f"**embed** | Embeds given message\n **say** | Says what you did\n")
    embed.set_footer(text='Nebula')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clean(ctx, limit: int, *, user: discord.Member = None):
        await ctx.channel.purge(limit=limit)
        await ctx.send('Cleared by {}'.format(ctx.author.mention))
        await ctx.message.delete()

@clean.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cant do that!")

@client.command()
async def admin(ctx):
    embed=discord.Embed(title=f"**Admin Commands**\n", description=f"**ban** | Bans user\n **kick** | kicks user \n **clear** | purges given number of messages\n **mute** | mutes given user\n **poll** | creates a poll\n", color=0xff0000)
    embed.set_footer(text='Nebula')
    await ctx.send(embed=embed)

                                                      
@client.command()
async def ip2domain(ctx, IP):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}IP2Domain")
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/ip2domains?key=&ip={IP}").text
    embed=discord.Embed(title=f" __**Domains on {IP}**__ ", description=f"{r}", color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
async def phonelookup(ctx, phone):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Phone Lookup")
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/phonelookup?key=&number={phone}").text
    embed=discord.Embed(title=f" __**Info On {phone}**__ ", description=f"{r}", color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
async def botinfo(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}                    [{Fore.RED}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.RED}Credits {Fore.WHITE}UwU")
    embed=discord.Embed(title=f" __** Credits**__", description=f"Neubla Discord Bot is the most usefull open-source discord bot.\n\nIt is made By chrge#0001\n\n**Website**\nhttps://proxysec.xyz/\n\n**Discord**\nhttps://discord.gg/isis", color=0xfa1e2e)
    embed.set_footer(text=f"{Footer}")
    await ctx.send(embed=embed)



@client.command()
async def pingweb(ctx, website = None):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}PingWeb")
    await ctx.message.delete()
    if website is None: 
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            embed=discord.Embed(title=f"Site is up, Status code {r}", color=0x37ff00)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f"Site is Down, Status code {r}", color=0xff0000)  
            await ctx.send(embed=embed)

@client.command()
async def embed(ctx,*, message):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Embed")
    await ctx.message.delete()
    embed=discord.Embed(title=f" ", description=f"{message}", color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
async def say(ctx,*, message):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Say")
    await ctx.message.delete()
    await ctx.send(f"{message}")

@client.command()
async def spanish(ctx,*, text):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Spanish")
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/translate?key=&text={text}&tolanguage=ES").text
    embed = discord.Embed(title="__**Spanish Text**__", description=f"**{r}**", color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
async def russian(ctx,*, text):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Russian")
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/translate?key=&text={text}&tolanguage=ru").text
    embed = discord.Embed(title="__**Russian Text**__", description=f"**{r}**", color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
async def fact(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Fact")
    await ctx.message.delete()
    r = requests.get("https://useless-facts.sameerkumar.website/api")
    res = r.json()
    embed = discord.Embed(title=":notebook: :notebook: :notebook: ", description=res["data"], color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
async def fml(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}FML")
    await ctx.message.delete()
    r = requests.get("https://api.alexflipnote.dev/fml")
    res = r.json()
    embed = discord.Embed(title="FML", description=res["text"], color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
async def joke(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Joke")
    await ctx.message.delete()
    await ctx.send(
        requests.get(url="https://icanhazdadjoke.com/", headers={"Accept": "application/json"}).json()['joke'])

@client.command(name='8ball')
async def _8ball(ctx, *, question):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}8Ball")
    await ctx.message.delete()
    responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'That is a definite yes!',
        'Maybe',
        'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed(color=0xff0000)
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/720348929043988572/722447275561058314/1200px-8-Ball_Pool.svg.png")
    await ctx.send(embed=embed)
 


@client.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Would You Rather")
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}', color=0xff0000)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/729845783238672454/730078326441377922/image0.png")
    await ctx.send(embed=em)

@client.command()
async def covid(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}covid")
    await ctx.message.delete()
    r = requests.get("https://api.covid19api.com/world/total")
    res = r.json()
    totalc = 'TotalConfirmed'
    totald = 'TotalDeaths'
    totalr = 'TotalRecovered'
    embed = discord.Embed(title='Updated Just Now:', description=f"Deaths | **{res[totald]}**\nConfirmed | **{res[totalc]}**\nRecovered | **{res[totalr]}**") # create embed
    embed.colour = (0x000000)
    await ctx.send(embed=embed)

@client.command()
async def supreme(ctx, *, text):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Supreme")
    await ctx.message.delete()
    embed = discord.Embed(
        title=f'Supreme {text} output:',
        colour=discord.Colour.red()
    )

    embed.set_image(url=f"https://api.alexflipnote.dev/supreme?text={text}")
    await ctx.send(embed=embed)

@client.command()
async def youtube(ctx, *, key):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}YouTube")
    await ctx.message.delete()
    embed=discord.Embed(title="Youtube Video", color=0xff0000)
    embed.set_thumbnail(url="http://assets.stickpng.com/images/580b57fcd9996e24bc43c545.png")
    embed.add_field(name="URL: ", value=f"https://www.youtube.com/results?search_query={key}", inline=True)
    await ctx.send(embed=embed)


@client.command()
async def pornhub(ctx, *, phkey):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}PornHub")
    await ctx.message.delete()
    embed=discord.Embed(title="Pornhub Search", color=0xff0000)
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Pornhub-logo.svg/512px-Pornhub-logo.svg.png")
    embed.add_field(name="URL: ", value=f"https://www.pornhub.com/video/search?search={phkey}", inline=True)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def gay(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Gay")
    await ctx.message.delete()
    variable = [
        " so gay ur not ",
        " incredibly gay lmao ",
        " So straight ur gay ",
		" "]
    await ctx.send("You're" "{}".format(random.choice(variable)) + "gay")

@client.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Dick")
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", color=0xff0000)
    await ctx.send(embed=em)

@client.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.red(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)        

@client.command()
@commands.has_role('Admin')
async def mod(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Mod")
    await ctx.message.delete()
    embed=discord.Embed(title=f"__**Moderation Commands**__", description=f"{prefix}mute [user] | **mute a user**\n{prefix}bans | **gives list of banned users**\n{prefix}clear [ammount] | **clear ammount of messages**\n{prefix}ban [user] | **ban a user**\n{prefix}poll [question] | **make a poll**\n\n__**Website**__\nhttps://proxysec.xyz", color=0xff0000)
    await ctx.send(embed=embed)

@client.command()
@commands.has_role('Admin')
async def poll(ctx, *, question: str):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Poll")
    await ctx.message.delete()
    msg = await ctx.send("**{}** asks: {}".format(ctx.message.author, question.replace("@", "@\u200b")))
    try:
        await ctx.message.delete()
    except:
        pass
    if ctx.guild.id == 207943928018632705:
        # Essential :sexthumb:
        yes_thumb = discord.utils.get(
            ctx.guild.emojis, id=287711899943043072)
        no_thumb = discord.utils.get(
            ctx.guild.emojis, id=291798048009486336)
    else:
        yes_thumb = "👍"
        no_thumb = "👎"
    await msg.add_reaction(yes_thumb)
    await msg.add_reaction(no_thumb)

@client.command()
@commands.has_role('Admin')
async def bans(ctx):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Bans")
    await ctx.message.delete()
    bans = await ctx.guild.bans()
    em = discord.Embed(title=f'List of Banned Members ({len(bans)}):')
    em.description = ', '.join([str(b.user) for b in bans])
    em. color=0xff0000
    await ctx.send(embed=em)


@client.command()
@commands.has_role('Admin')
async def ban(ctx, member : discord.Member, *, reason = None):
    print(f"{Back.BLACK}{Fore.WHITE}[{Fore.GREEN}{current_time}{Fore.WHITE}] {Fore.WHITE}Command Used {Fore.WHITE}- {Fore.GREEN}Ban")
    await ctx.message.delete()
    await member.ban(reason = reason)
    embed=discord.Embed(title=f"Banned {member}")

    await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
    embed=discord.Embed(title=f"**Bot Invite**", description=f"https://discord.com/api/oauth2/authorize?client_id=748058083858710598&permissions=8&scope=bot")
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)



client.run("")
