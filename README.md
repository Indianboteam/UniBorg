# 🇮🇳Indian Bot Ultra 🇮🇳

Pluggable [``asyncio``](https://docs.python.org/3/library/asyncio.html)
[Telegram](https://telegram.org) userbot based on
[Telethon](https://github.com/LonamiWebs/Telethon).

## installing

#### The Easy Way

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Other way 

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/indianboteam/Indianbotultra)

### Performance Test

[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/indianboteam/indianbotultra/?ref=repository-badge)

### Code Quality

[![CodeFactor](https://www.codefactor.io/repository/github/muhammedfurkan/uniborg/badge)](https://www.codefactor.io/repository/github/indianboteam/indianbotultra)

#### The Legacy Way
Simply clone the repository and run the main file:
```sh
git clone https://github.com/indianboteam/indianbotultra.git
cd uniborg
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create config.py with variables as given below>
python3 -m stdborg YourSessionName
```

An example `config.py` file could be:

**Not All of the variables are mandatory**

__The indian bot ultra should work by setting only these variables__

```python3
from sample_config import Config

class Development(Config):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
  TG_BOT_TOKEN_BF_HER = ""
  TG_BOT_USER_NAME_BF_HER = ""
  UB_BLACK_LIST_CHAT = [
    -1001220993104,
    -1001365798550,
    -1001158304289,
    -1001212593743,
    -1001195845680,
    -1001330468518,
    -1001221185967,
    -1001340243678,
    -1001311056733,
    -1001135438308,
    -1001038774929,
    -1001070622614,
    -1001119331451,
    -1001095401841
  ]
  # specify LOAD and NO_LOAD
  LOAD = []
  NO_LOAD = []
```

## internals

The core features offered by the custom `TelegramClient` live under the
[`uniborg/`](https://github.com/muhammedfurkan/uniborg/tree/master/uniborg)
directory, with some utilities, enhancements, the `_core` plugin, and the `_inline_bot` plugin.


## [@MarioDevs](https://telegram.dog/Mariodevs)

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will work without setting the non-mandatory environment variables.


async def handler(event):
    await event.reply("hey")
```


## learning

Check out the already-mentioned [plugins](https://github.com/SpEcHiDe/muhammedfurkan/tree/master/stdplugins) directory, or some third-party [plugins](https://telegram.dog/UniBorg) to learn how to write your own, and consider reading [Telethon's documentation](http://telethon.readthedocs.io/).


## credits


Thanks to:
- [lonami](https://lonami.dev) for creating [Telethon](https://github.com/lonamiwebs/Telethon)

