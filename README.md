# Academy Alef Rank Bot — Deploy on Render

## فایل‌های مهم
- `bot.py` — کد اصلی ربات
- `search.py` — منطق تخمین رتبه و تراز
- `requirements.txt` — وابستگی‌ها
- `Procfile` — دستور اجرا برای Render
- `runtime.txt` — نسخه پایتون

## متغیر محیطی (Environment Variable)
در Render فقط این را اضافه کنید:

```
BOT_TOKEN=توکن_ربات_از_BotFather
```

## دستورات Render
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python bot.py`
- **Type:** Background Worker
