import asyncio

from discord.ext import commands
from discord.ext.commands import Bot
from spread_sheet import update_counters

class Tracker(commands.Cog):
    """
    Tracker command events, where datasheet is updated based on otter status.
    Commands:
        tracker apply [company]: Update database with the applyment
        tracker offer [company] : Update database with the new incoming offer  
    """
    def __init__(self, bot: Bot, channel_id: str) -> None:
        self.bot = bot
        self.channel_id = channel_id
    
    @commands.group(
        brief = "Commands related to application tracker",
        invoke_without_command = True,
        pass_context = True
    )
    async def tracker(self, ctx, *, content: str):
        """
        Tracker will be a helpful tool to keep track of application process between otters
        """
        await ctx.send_help(ctx.command)

    @tracker.command(brief="Command for update apply process of any user")
    async def apply(self, ctx, company: str):
        """
        Apply update spreadsheet for new aplicants
        """
        aplicant_name = ctx.author.name
        applyment_message = f"Congrats! {aplicant_name}, good luck during your application process in {company} 🥳" 
        print(applyment_message)
        response: bool = update_counters.update_applyment(company)
        if response:
            await ctx.send(applyment_message)
        else:
            await ctx.send("Sorry, please try again with a valid company!")
def setup(bot):
    bot.add_cog(Tracker(bot, "830899815680180226"))