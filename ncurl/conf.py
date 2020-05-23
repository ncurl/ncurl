from collections import namedtuple
from pathlib import Path
import json

Config = namedtuple('Config', ['server_url', 'expiredAt', 'isUpload'])
_default_config = Config(
    server_url='https://api.ncurl.sh/api',
    expiredAt=1800,  # default expired at half hour
    isUpload=True
)


def load_or_init_config():
    config_path = Path.joinpath(Path.home(), Path('.ncurl'))
    if not config_path.exists():
        with open(str(config_path), 'w') as f:
            f.write(json.dumps(_default_config._asdict(), indent="  "))
            return _default_config

    with open(str(config_path)) as f:
        return json.loads(f.read(), object_hook=lambda json_data: Config(**json_data))