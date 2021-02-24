import argparse

from bot.bad_apple import bot, bad_apple_bot_config
from bot.utils import convert_video_to_frames

parser = argparse.ArgumentParser(description='Helps us with rendering pngs out of video')
parser.add_argument("--render", '-r', dest="render_video", action="store_true", default=False)

if __name__ == "__main__":
    args = parser.parse_args()
    if args.render_video:
        convert_video_to_frames(bad_apple_bot_config.video_path.value)

    bot.run(bad_apple_bot_config.token.value)
