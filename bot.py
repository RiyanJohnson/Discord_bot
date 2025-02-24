import discord
from discord.ext import commands

Token = '<your token>'

intents = discord.Intents.default()  
intents.message_content = True #allowing the bot to read messages

client = commands.Bot(command_prefix='!',intents = intents)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

    #run the bot after removing the comment if you want to send msg as your bot from the terminal
    '''channel = client.get_channel(1340663063908712512)
    while True:   
        message = input("Enter message to send (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break
        await channel.send(message)
    return'''

@client.event
async def on_message(ctx):

    username = str(ctx.author).split('#')[0]
    user_ctx = str(ctx.content)
    channel = str(ctx.channel.name)
    print(f'{username}: {user_ctx} (#{channel})')

    if ctx.author == client.user:
        return
    
    if user_ctx.lower() == 'hello' or user_ctx.lower() == 'hey' or user_ctx.lower() == 'hi':
        await ctx.channel.send(f"Hello {ctx.author}! I'm Weee")
        return 
    elif user_ctx.lower() == 'bye' or user_ctx.lower() == 'cya':
        await ctx.channel.send(f"Bye {ctx.author} Have a great day ahead!")
        return
    await client.process_commands(ctx)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')

@client.command()
@commands.has_permissions(manage_roles = True)
async def mute(ctx, member: discord.Member, *, reason=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    try:
        await member.add_roles(muted_role)
        await ctx.send(f"{member.mention} has been muted")
    except discord.Forbidden:
        await ctx.send("You do not have permissions to add these roles")

@client.command()
@commands.has_permissions(manage_roles = True)
async def unmute(ctx, member: discord.Member, *, reason = None):
    muted_role = discord.utils.get(ctx.guild.roles, name = "Muted")
    try:
        await member.remove_roles(muted_role)
        await ctx.send(f"{member.mention} has been unmuted")
    except discord.Forbidden:
        await ctx.send("You do not have permissions to remove these roles")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member:discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'{member.mention} has been banned')

client.run(Token)   