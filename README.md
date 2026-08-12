# Academy Alef Rank Bot

A Persian Telegram bot for estimating Iranian university entrance exam ranks and educational scores using configurable, table-driven data.

## Features

- Estimate exam rank from total score, field, and quota region
- Estimate final-exam score from overall GPA
- Calculate a weighted GPA from individual course grades
- Estimate rank from subject percentages and final GPA
- Evaluate scores from major mock-exam providers
- Persian-first conversational interface with structured Telegram keyboards
- Ready for deployment as a Render background worker

## Supported fields

- Experimental Sciences (Tajrobi)
- Mathematics and Physics (Riazi)
- Humanities support is available where the underlying dataset defines it

## Project structure

| Path | Purpose |
| --- | --- |
| `bot.py` | Telegram handlers, conversation states, menus, and user-facing responses |
| `search.py` | Rank tables, score conversion data, and calculation helpers |
| `assets/` | Images used by the bot |
| `requirements.txt` | Python dependencies |
| `Procfile` | Render worker command |
| `runtime.txt` | Python runtime version |
| `.env.example` | Environment variable template |

## Requirements

- Python 3.10 or newer
- A Telegram bot token from [BotFather](https://t.me/BotFather)

## Local setup

1. Clone the repository:

   ```bash
   git clone https://github.com/gonderak/rank-bot.git
   cd rank-bot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:

   ```env
   BOT_TOKEN=your_telegram_bot_token
   ```

5. Run the bot:

   ```bash
   python bot.py
   ```

## Environment variables

| Variable | Required | Description |
| --- | --- | --- |
| `BOT_TOKEN` | Yes | Telegram bot token issued by BotFather |
| `PROXY_URL` | No | Optional proxy URL for Telegram API requests |

Never commit real tokens or credentials.

## Deploying on Render

Create a **Background Worker** with:

- Build command: `pip install -r requirements.txt`
- Start command: `python bot.py`
- Environment variable: `BOT_TOKEN`

The included `Procfile` and `runtime.txt` provide the corresponding deployment configuration.

## Calculation model

The bot uses explicit datasets and interpolation helpers defined in `search.py`. Rank and score estimates are approximate and should not be treated as official examination results.

When updating calculation data:

1. Preserve continuous score boundaries.
2. Validate every supported region.
3. Compile-check both Python files.
4. Test boundary values before deployment.

## Security

- Keep `.env` out of version control.
- Rotate the Telegram token immediately if it is exposed.
- Store production secrets only in the deployment provider's environment settings.

## Disclaimer

This project provides educational estimates. Actual ranks and admission outcomes depend on official results, annual scoring rules, quota policies, and the applicant population.

## License

No license has been published for this repository. All rights are reserved unless the owner adds a license file.
