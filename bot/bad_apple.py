from asyncio import sleep
from concurrent.futures import ProcessPoolExecutor

import discord
from PIL import Image
from discord import Intents
from discord.ext import commands

from bot.config import bad_apple_bot_config
from bot.utils import CLIP_FRAMES, CLIP_LENGTH, FRAME_LENGTH, frames_path, process_image

PROCESS_POOL_SIZE = 5
bot = commands.AutoShardedBot(
    command_prefix=commands.when_mentioned_or(bad_apple_bot_config.prefix.value),
    description="Bot that sends bad apple video frames to you channel!",
    intents=Intents.default()
)
bot.__version__ = "1.0.0"


@bot.event
async def on_ready():
    print(
        "Logged in as",
        f"Name: {bot.user.name}",
        f"DevID: {bot.user.id}",
        f"Discord.py {discord.__version__}",
        f"Bot version: {bot.__version__}",
        "Fork by @Rud356 (https://github.com/Rud356)",
        "Original bot by: @NPCat (https://github.com/NPCat)",
        sep='\n'
    )


@commands.cooldown(rate=1, per=CLIP_LENGTH, type=commands.BucketType.channel)
@bot.command()
async def bad_apple(ctx: commands.Context):
    for frame_index in range(0, CLIP_FRAMES, 4):
        frame_path = frames_path / f"frame {frame_index}.png"
        if not frame_path.is_file():
            continue

        try:
            frame = Image.open(frame_path)
        except Image.UnidentifiedImageError:
            continue

        with ProcessPoolExecutor(PROCESS_POOL_SIZE) as pool:
            converted_frame = await bot.loop.run_in_executor(
                pool, process_image, frame
            )

        await ctx.send(content=converted_frame)
        await sleep(FRAME_LENGTH)

    await ctx.send(content="Done!")
