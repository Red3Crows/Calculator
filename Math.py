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
            if res.component.label == "1":
                math_string = math_string + "1"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "2":
                math_string = math_string + "2"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "3":
                math_string = math_string + "3"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "4":
                math_string = math_string + "4"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "5":
                math_string = math_string + "5"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "6":
                math_string = math_string + "6"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "7":
                math_string = math_string + "7"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "8":
                math_string = math_string + "8"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "9":
                math_string = math_string + "9"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "0":
                math_string = math_string + "0"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "00":
                math_string = math_string + "00"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "+":
                math_string = math_string + "+"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "-":
                math_string = math_string + "-"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "×":
                math_string = math_string + "*"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "÷":
                math_string = math_string + "/"
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == ".":
                math_string = math_string + "."
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "Exit":
                await msg.delete()
                break
            if res.component.label == "=":
                javab = eval(math_string)
                math_string = ""
                Calculator = discord.Embed(title=f"`{javab}`")
                await msg.edit(embed=Calculator)
            if res.component.label == "Clear":
                math_string = ""
                Calculator = discord.Embed(title=f"`{math_string} `")
                await msg.edit(embed=Calculator)
            if res.component.label == "←":
                math_string = math_string[:-1]
                Calculator = discord.Embed(title=f"`{math_string}`")
                await msg.edit(embed=Calculator)


def setup(client):
    DiscordComponents(client)
    client.add_cog(Math(client))
