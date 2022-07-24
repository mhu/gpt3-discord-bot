# GPT-3 Discord Bot

The GPT-3 Discord Bot uses OpenAI's implementation of the [GPT-3 language model](https://en.wikipedia.org/wiki/GPT-3).

## Getting Started

### Prerequisites

You should be running Python 3 and have the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed.

### Installing

```sh
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
```

## Deployment

```sh
make deploy
```

To check Heroku logs:

```sh
make logs
```

## Built With

* [discord.py](https://github.com/Rapptz/discord.py) - Discord API wrapper
* [openai-python](https://github.com/openai/openai-python) - Access to the OpenAI API
