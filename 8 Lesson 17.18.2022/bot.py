
import datetime
import discord as d
from discord.ext import commands, tasks
from dataclasses import dataclass
import python_list as pl

BOT_TOKEN = 'MTA1OTM0MjQ1MTc3NDU5NTA4Mg.GZ0a9N.fpos6qjE-KNh6pzcArPeg_3xdifkSqseWB4oOc'
CHANNEL_ID = 1044596250525315244
MAX_SESSION_TIME_MINUTES = 120


@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0
    end_time: int = 0


bot = commands.Bot(command_prefix='!', intents=d.Intents.all())
session = Session()


@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('Hello guys, я Гейб Ньюэлл, исполняю ваши капризы, пиши !info')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    # print(message)
    # print(message.content)
    if message.author.bot:
        return
    if message.content.startswith('-'):
        if message.content == '-stop':
            with open('used_names.txt', 'w', encoding='utf-8') as f:
                f.write('')
        else:
            i = pl.get_city(message.content, 'used_names.txt')
            await message.channel.send(i)


@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
async def break_reminder():
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"**Take a break!** You've been studying for {MAX_SESSION_TIME_MINUTES} minutes")


@bot.command()
async def info(ctx):
    await ctx.send(f"1 - !start - начать сессию \n2 - Могу сыграть с тобой в Русские города, пиши название города через '-' и го, для того что бы начать заново напиши '-stop'")


@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("Сессия уже идет, бегом в дотку!")
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    human_readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    break_reminder.start()
    await ctx.send(f"Сессия ({human_readable_time}) начата дорогие мои, gl hf, через три часа я любезно напомню о том что вам стоило бы бороться с игроманией! Не забудь завершить сессию командой !end ")


@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("Сессия не начата!")
        return
    session.is_active = False
    session.end_time = ctx.message.created_at.timestamp()
    duration = session.end_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds=duration))
    break_reminder.stop()
    await ctx.send(f"Ну вообщем прокатал ты всего {human_readable_duration}.")
with open('used_names.txt', 'w', encoding='utf-8') as f:
                f.write('')

bot.run(BOT_TOKEN)
