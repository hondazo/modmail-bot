# IMPORTS
import discord
import asyncio
from discord.ext import commands
from discord import Embed, Color
 

PREFIX = ''
client = commands.Bot(command_prefix = commands.when_mentioned_or(PREFIX), case_insensitive=True)
TOKEN = "BOT TOKEN HERE"

# The guild that the message will be sent to
GUILD = 

# The channel taht the message will be sent to 
CHANNEL = 

@client.event
async def on_ready():
	print("Bot online")
	while True:
		await client.change_presence(activity=discord.Game(name="DM me for help"))
		await asyncio.sleep(600)

@client.command(aliases=['mail', 'r', 'm'])
async def reply(ctx, member: discord.Member, *, text):
	await member.send(text)


@client.event 
async def on_message(message):
	# Returns if the messager is a bot
	if message.author.id == client.user.id:
		return


	if message.author != message.author.bot:
		
		# If the message's sent to the bot, then the bot will send an embed to the channel specified above
		if not message.guild:
			embed = Embed(color=discord.Color.orange())
			embed.add_field(name="**Mod Mail**", value=f"Mention: {message.author.mention}\nUsername: {message.author}\nUser ID: {message.author.id}\n**Message Content**\n{message.content}")
			await client.get_guild(GUILD).get_channel(CHANNEL).send(embed=embed)

	await client.process_commands(message)

client.run(TOKEN)