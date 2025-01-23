import discord
from discord.ext import commands
from openai import OpenAI
import os

defaultEmbedColor=discord.Color(0xb253d6)
green = discord.Color(0x00FF00)
red = discord.Color(0xFF0000)
checkmark = ":white_check_mark:"
xmark = ":x:"


class Chatbot(commands.Cog):
    description=""
    def __init__(self,bot):
        self.bot = bot

    # Print code here
    @commands.Cog.listener()
    async def on_message(self, msg):
         if self.bot.user not in msg.mentions:
              return
         parse = msg.content.split(self.bot.user.mention)
         prompt = ""
         for string in parse:
            prompt += string
         client = OpenAI()

         completion = client.chat.completions.create(
             model="gpt-4o",
             messages=[
                 {"role": "developer", "content": "You are a helpful assistant."},
                 {
                     "role": "user",
                     "content": prompt,
                 }
             ]
         )

         await msg.reply(completion.choices[0].message.content)
         
         #await msg.reply(response)

        
async def setup(bot):
	await bot.add_cog(Chatbot(bot))
