import discord
KEY = '' # Not Today!

client = discord.Client()

@client.event
async def on_ready():
    print('Client Connected')

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 943925071712493679:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        role = discord.utils.get(guild.roles, name=payload.emoji.name)
        

        # This is if emojiName != the Role name 
        # if payload.emoji.name == 'GasAlert':
        #     role = discord.utils.get(guild.roles, name='GasAlert')
        # elif payload.emoji.name == 'Whatever':
        #     do anything
            
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.add_roles(role)
                print('Done!')
            else: print('Member not found')
        else: print('Role not found')

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 943925071712493679:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        role = discord.utils.get(guild.roles, name=payload.emoji.name)
        

        # This is if emojiName != the Role name 
        # if payload.emoji.name == 'GasAlert':
        #     role = discord.utils.get(guild.roles, name='GasAlert')
        # elif payload.emoji.name == 'Whatever':
        #     do anything
            
        if role is not None:
            member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
            if member is not None:
                await member.remove_roles(role)
                print('Done!')
            else: print('Member not found')
        else: print('Role not found')

client.run(KEY)