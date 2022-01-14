from twitchio.ext import commands
from util import get_chance
from web_scrapers import SaucyInsultScraper

class RivalCog(commands.Cog):

    # AutoCogs only can accept bot as an init argument which is passed automatically
    def __init__(self, bot):
        self.bot = bot
        self.rivals = {
            'nightbot': 25,
            'franklysilly': 5, 
            'sniperqueen1813': 5,
            'hgtv_nico': 5
        }
        self.saucy_scraper = SaucyInsultScraper()
    
    def should_insult(self, author):
        return author in self.rivals.keys() and get_chance(self.rivals.get(author), max=999)

    async def insult_rival(self, message, rival):
        insult = self.saucy_scraper.scrape()
        text = f"Get out of here {rival}. {insult}"
        await message.channel.send(text)
