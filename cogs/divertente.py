import discord
from discord.ext import commands, tasks
from data import skyshit24
from gtts import gTTS
import re
from io import BytesIO
from tempfile import TemporaryFile


class divertente(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Manda informazioni dal mondo')
    async def news(self, ctx):
        text = skyshit24.news_picker()
        embed = discord.Embed(title=text, colour=discord.Colour.blue())
        embed.set_footer(text="https://t.me/skyshit24")
        await ctx.send(embed=embed)

    @commands.command(description='Invia un file mp3 con il testo che hai scritto')
    async def tts(self, ctx, *, message=None):
        if message:
            try:
                message = await commands.clean_content(use_nicknames=True).convert(ctx, message)
                message = re.sub("<(?P<animated>a?):(?P<name>[a-zA-Z0-9_]{2,32}):(?P<id>[0-9]{18,22})>", "", message)
                message = message.replace('@', '')
                tts = gTTS(text=message, lang='it')
                f = TemporaryFile()
                tts.write_to_fp(f)
                f.seek(0)  # file object
                await ctx.send(file=discord.File(BytesIO(f.read()), filename='tts.mp3'))
                f.close()
            except:
                await ctx.send('Cè qualcosa che non va...')
        else:
            await ctx.send('Esempio:\n tts Ciao CIRO')


def setup(bot):
    bot.add_cog(divertente(bot))