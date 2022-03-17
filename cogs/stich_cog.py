from twitchio.ext import commands


class StitchCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ohana')
    async def sillybot_command(self, ctx):
        message = f"nomadi19Stitch nomadi19Stitch nomadi19Stitch nomadi19Stitch nomadi19Stitch "
        await ctx.send(message)

