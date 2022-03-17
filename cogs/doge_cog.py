from twitchio.ext import commands


class DogeCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='doge')
    async def sillybot_command(self, ctx):
        message = f"nicovi11Dodg nicovi11Dodg nicovi11Dodg nicovi11Dodg nicovi11Dodg "
        await ctx.send(message)

