import disnake
from disnake.ext import commands
import json
import classes
from jinja2 import *
import require

# TODO: make render in function

class dbs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        
        f = open("eventshandler.json", "r")
        jsondump = json.load(f)
        f.close()

        for event in jsondump["events"]:
            if event["event"] not in ["prefix_command", "message"]:
                continue

            if event["event"] == "prefix_command":

                prefix = jsondump["commands_prefix"]
                if not msg.content.startswith(prefix):
                    continue

                if event["data"] == msg.content[len(prefix):].split()[0]:
                    renderpath = event["path"]
                    
                    jinja_env = Environment(loader=FileSystemLoader("scripts"), extensions=['jinja2.ext.do'], enable_async=True)
                    d = jinja_env.get_template(renderpath)
                    await d.render_async(context=msg, action=classes.action(self.bot), require=require.require, enum=classes.enum(self.bot))

            else:
                renderpath = event["path"]
                
                jinja_env = Environment(loader=FileSystemLoader("scripts"), extensions=['jinja2.ext.do'], enable_async=True)
                d = jinja_env.get_template(renderpath)
                await d.render_async(message=msg, action=classes.action(self.bot), require=require.require, enum=classes.enum(self.bot))

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        f = open("eventshandler.json", "r")
        jsondump = json.load(f)
        f.close()

        for event in jsondump["events"]:
            if event["event"] == "on_guild_join":
                renderpath = event["path"]
                
                jinja_env = Environment(loader=FileSystemLoader("scripts"), extensions=['jinja2.ext.do'], enable_async=True)
                d = jinja_env.get_template(renderpath)
                await d.render_async(guild=guild, action=classes.action(self.bot), require=require.require, enum=classes.enum(self.bot))


def setup(bot: commands.Bot):
    bot.add_cog(dbs(bot))