from pathlib import Path

from ConfigFramework import (
    BaseConfig,ConfigVariable,
    CompositeConfigLoader, EnvironmentConfigLoader,
    JSONFileConfigLoader
)

from bot.config import config_validators
from bot.utils import CLIP_FRAMES, convert_video_to_frames, frames_path

JSON_CONFIG_PATH = Path(__file__).parent / "config.json"

if not JSON_CONFIG_PATH.is_file():
    # Make empty json file
    JSON_CONFIG_PATH.write_text("{}")
    JSONFileConfigLoader.load(
        JSON_CONFIG_PATH,
        defaults={"token": "DISCORD_TOKEN", "video_path": "bad_apple.mp4", "prefix": "!"}
    ).dump()

    raise FileNotFoundError(
        "Please, edit bot/config/config.json and edit token variable or pass variables "
        "as env variables (token, video_path, prefix) for bot"
    )


loader = CompositeConfigLoader.load(
    EnvironmentConfigLoader.load(mute_warn=True),
    JSONFileConfigLoader.load(
        JSON_CONFIG_PATH,
        defaults={"token": "DISCORD_TOKEN", "video_path": "bad_apple.mp4", "prefix": "!"}
    )
)


class BadAppleBotConfig(BaseConfig):
    token = ConfigVariable.variable("token", loader)
    prefix = ConfigVariable.variable("prefix", loader, validator=config_validators.validate_prefix)
    video_path = ConfigVariable.variable("video_path", loader, caster=Path, validator=Path.is_file)

    def __post_init__(self, *args, **kwargs):
        frames_found = 0
        for frames, _ in enumerate(frames_path.iterdir(), start=1):
            frames_found = frames

        if frames_found < CLIP_FRAMES:
            convert_video_to_frames(self.video_path.value)


bad_apple_bot_config = BadAppleBotConfig()
