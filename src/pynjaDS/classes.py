import disnake
import asyncio
import time
import random
from disnake.ext import commands


class action:

    def __init__(self, bot: commands.Bot):
        self.rawbot = bot
        self.embed = disnake.Embed

    async def reply(self, message, text):
        await message.reply(text)

    async def sendMessage(self, channel, text = None, embed: disnake.Embed = None):
        await self.rawbot.get_guild(channel.guild.id).get_channel_or_thread(channel.id).send(text, embed=embed)

    # parse

    async def toGuild(self, id):
        return await self.rawbot.get_guild(id)
    
    def toChannel(self, guild, id):
        return guild.get_channel(id)
    
    def toChannelOrThread(self, guild, id):
        return guild.get_channel_or_thread(id)
    
    def toMember(self, guild, id):
        return guild.get_member(id)
    
    def toRole(self, guild, id):
        return guild.get_role(id)
    
    def mentionToMember(self, guild, mention: str):
        return self.toMember(guild, int(mention[2:][:-1]))

    def canToGuild(self, id):
        try:
            self.rawbot.get_guild(id)
            return True
        except:
            return False
    
    def canToChannel(self, guild, id):
        try:
            guild.get_channel(id)
            return True
        except:
            return False
    
    def canToChannelOrThread(self, guild, id):
        try:
            guild.get_channel_or_thread(id)
            return True
        except:
            return False
        
    def canToMember(self, guild, id):
        try:
            guild.get_member(guild, id)
            return True
        except:
            return False
        
    def canToRole(self, guild, id):
        try:
            guild.role(id)
            return True
        except:
            return False

    def canMentionToMember(self, guild, mention: str):
        try:
            self.toMember(guild, int(mention[2:][:-1]))
            return True
        except:
            return False
    # end parse

    async def combineArgs(self, args):
        return " ".join(args)
    
    async def addRoles(self, user, *roles):
        await user.add_roles(*roles)

    async def removeRoles(self, user, *roles):
        await user.remove_roles(*roles)

    async def ban(self, user, reason: str = None):
        await user.ban(reason=reason)

    async def kick(self, user, reason: str = None):
        await user.kick(reason=reason)

    async def giveTimeout(self, user, duration, reason: str = None):
        await user.timeout(reason=reason, duration=duration)
    
    async def moveTo(self, user, channel, reason: str = None):
        await user.move_to(reason=reason, channel=channel)

    def getPermissions(self, user):
        return user.guild_permissions

    # not discord

    async def sleep(self, seconds):
        await asyncio.sleep(seconds)

    def block(self, seconds):
        time.sleep(seconds)

    def toInt(self, convert):
        return int(convert)
    
    def toStr(self, convert):
        return str(convert)
    
    def randomize(self, min, max):
        return random.randint(min, max)
    
    def randomChoice(self, iterable):
        return random.choice(iterable)
    
    def getLen(self, iterable):
        return len(iterable)

class enum:
    
    def __init__(self, client):
        self.Colors = disnake.Color
        self.Client = client