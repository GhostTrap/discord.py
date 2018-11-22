import discord

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('.bork'):
        msg = '***B o r k***'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NTE1MDAyMjk5MjU3NzE2NzQ2.Dte87Q.mcMZyssKyQSPZselsQbRlzl2Mig')
