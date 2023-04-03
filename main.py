import datetime
import disnake
from disnake.ext import commands
import asyncio
from disnake.ui import Button
from disnake.enums import ButtonStyle, TextInputStyle
from disnake import Embed
from disnake.utils import get
from disnake.ui import Select
import configs


log_in = str(input("token /> "))
conf = configs.Configs(log_in)
bot = commands.Bot(command_prefix="faq>", case_insensitive=True, intents=disnake.Intents.all())

@bot.event
async def on_ready():
    print(f"""BOT CONNECTED SUCCESSFUL!
{datetime.datetime.now()}""")

@bot.command()
async def set(ctx):
  if conf.is_admin(ctx.author.id):
    """FIRST STAGE"""
    white = bot.get_emoji(1086292088863342653)
    welcome = bot.get_channel(conf.get_welcome_channel())
    embed=Embed(
        title=f"{white} Welcome to ReMolla Support Server!",
        description="Choose your language, please :)",
        color=conf.default_color
    )
    components = disnake.ui.View()
    components.add_item(Button(style=disnake.ButtonStyle.blurple, label="English", custom_id="set_eng", emoji="🇬🇧"))
    components.add_item(Button(style=disnake.ButtonStyle.blurple, label="Russian", custom_id="set_ru", emoji="🇷🇺"))
    await welcome.send(embed=embed, view=components)

    """SECOND STAGE"""
    rule = bot.get_channel(conf.get_rules_channel())
    protect = bot.get_emoji(1084301542120759366)
    embed=Embed(
        title=f"{protect} OUR RULES (follow it!)",
        color=conf.default_color
    )
    embed.set_image("https://media.discordapp.net/attachments/1078429568572080243/1083864902176870485/81_20230310230245.png?width=1440&height=545")
    embed.add_field(name="1) No spamming", value="`mute/ban`")
    embed.add_field(name="2) No advertisements", value="`ban`")
    embed.add_field(name="3) No flooding", value="`mute/ban`")
    embed.add_field(name="4) Follow the Discord Community Guidelines", value="`ban`")
    embed.add_field(name="5) No pornographic/adult/NSFW or NSFL material", value="`ban`")
    embed.add_field(name="6) Don’t share illegal or pirated content", value="`ban`")
    embed.add_field(name="7) No sharing or distributing viruses or malicious software", value="`ban`")
    embed.add_field(name="8) No bullying members", value="`mute/ban`")
    embed.add_field(name="9) Don't insult the values, race, religion of members", value="`mute/ban`")
    embed.add_field(name="10) Don't send links to sites that don't use SSL certificate", value="`(nothing, but the bot will delete your message)`")
    components = disnake.ui.View()
    components.add_item(Button(style=ButtonStyle.blurple, label="Translate into Russian", custom_id="translate_rule_ru", emoji="🇷🇺"))
    await rule.send(embed=embed, view=components)
  else:
    return await ctx.send(":x: You don't have enough permissions!")


@bot.event
async def on_button_click(interaction):
    if interaction.component.custom_id == "set_eng":
        eng =  interaction.guild.get_role(conf.get_eng_community_role())
        ru = interaction.guild.get_role(conf.get_ru_community_role())
        try:
            await interaction.author.add_roles(eng)
            await interaction.author.remove_roles(ru)
            await interaction.send("Nice! Now enjoy our server and meet your country's community ;)", ephemeral=True)
        except:
            await interaction.send(":x: Something went wrong! Try again later :(", ephemeral=True)
    if interaction.component.custom_id == "set_ru":
        eng =  interaction.guild.get_role(conf.get_eng_community_role())
        ru = interaction.guild.get_role(conf.get_ru_community_role())
        try:
            await interaction.author.add_roles(ru)
            await interaction.author.remove_roles(eng)
            await interaction.send("Отлично! Наслаждайся нашим сервером и познакомься с теплым русским комьюнити ;)", ephemeral=True)
        except:
            await interaction.send(":x: Something went wrong! Try again later :(", ephemeral=True)

    if interaction.component.custom_id == "translate_rule_ru":
        protect = bot.get_emoji(1084301542120759366)
        embed = Embed(
            title=f"{protect} НАШИ ПРАВИЛА (Соблюдай их!)",
            color=conf.default_color
        )
        embed.add_field(name="1) Не спамить", value="`мут/бан`")
        embed.add_field(name="2) Реклама запрещена", value="`бан`")
        embed.add_field(name="3) Не флудить", value="`мут/бан`")
        embed.add_field(name="4) Соблюдай Discord Community Guidelines", value="`бан`")
        embed.add_field(name="5) Запрещена порнография/NSFW или NSFL контент", value="`бан`")
        embed.add_field(name="6) Запрещено распространять нелегальный контент или ПО", value="`бан`")
        embed.add_field(name="7) Запрещено распространять вредоносное ПО", value="`бан`")
        embed.add_field(name="8) Запрещено оскорблять участников", value="`мут/бан`")
        embed.add_field(name="9) Запрещено оскорблять ценности, расу, религию участников", value="`мут/бан`")
        embed.add_field(name="10) Запрещено отправлять ссылки на сайты, которые не имеют SSL-сертификат",
                        value="`(ничего, но бот просто удалит сообщение)`")
        await interaction.send(embed=embed, ephemeral=True)


@bot.event
async def on_message(message):
    if "http://" in message.content and "." in message.content:
        print(message.content)
        await message.delete()



try:
    bot.run(conf.token)
except Exception:
    raise Exception("Invalid bot OAuth2 token")