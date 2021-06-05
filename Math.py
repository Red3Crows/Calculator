import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType


class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def calculator(self, ctx):
        math_string = " "
        Calculator = discord.Embed(title=f"`{math_string}`")
        msg = await ctx.send(
            embed=Calculator,
            components=[[
                Button(style=ButtonStyle.grey, label='1'),
                Button(style=ButtonStyle.grey, label='2'),
                Button(style=ButtonStyle.grey, label='3'),
                Button(style=ButtonStyle.blue, label='×'),
                Button(style=ButtonStyle.red, label='Exit'),
            ], [
                Button(style=ButtonStyle.grey, label='4'),
                Button(style=ButtonStyle.grey, label='5'),
                Button(style=ButtonStyle.grey, label='6'),
                Button(style=ButtonStyle.blue, label='÷'),
                Button(style=ButtonStyle.red, label='←'),
            ], [
                Button(style=ButtonStyle.grey, label='7'),
                Button(style=ButtonStyle.grey, label='8'),
                Button(style=ButtonStyle.grey, label='9'),
                Button(style=ButtonStyle.blue, label='+'),
                Button(style=ButtonStyle.red, label='Clear'),
            ], [
                Button(style=ButtonStyle.gray, label='00'),
                Button(style=ButtonStyle.gray, label='0'),
                Button(style=ButtonStyle.gray, label='.'),
                Button(style=ButtonStyle.blue, label='-'),
                Button(style=ButtonStyle.green, label="="),
            ]])
        while True:
            def check(res):
                return ctx.author == res.user and res.channel == ctx.channel

            res = await self.client.wait_for("button_click", check=check)
            mmd = await res.respond(type=InteractionType.ChannelMessageWithSource,
                                    content=f"{res.component.label} pressed")
            if res.component.label == "×":
                math_string = math_string + "*"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            elif res.component.label == "÷":
                math_string = math_string + "/"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            elif res.component.label == "Exit":
                await msg.delete()
                break
            elif res.component.label == "=":
                javab = eval(math_string)
                math_string = ""
                Calculator = discord.Embed(title=f"`{javab}`")
                await msg.edit(embed=Calculator)
            elif res.component.label == "Clear":
                math_string = ""
                Calculator = discord.Embed(title=f"`{math_string} `")
                await msg.edit(embed=Calculator)
            elif res.component.label == "←":
                math_string = math_string[:-1]
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            else:
                math_string += res.component.label
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)


def setup(client):
    DiscordComponents(client)
    client.add_cog(Math(client))
