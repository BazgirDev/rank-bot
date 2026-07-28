import os
import asyncio
import logging

from dotenv import load_dotenv
from telegram import (
    Update,
    BotCommand,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
)
from telegram.constants import ParseMode, ChatAction
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    ContextTypes,
    filters,
)

from search import (
    find_rank,
    gpa_to_taraz,
    percent_to_taraz,
    calc_weighted_gpa,
    format_rank_result,
    get_status,
    GPA_COEF,
    PCT_SUBJECTS,
    evaluate_exam_taraz,
)

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
PROXY_URL = os.getenv("PROXY_URL")

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ==================== STATES ====================
(
    MAIN_MENU,
    # Rank by Taraz
    RANK_FIELD, RANK_REGION, RANK_SCORE,
    # GPA → Taraz
    GPA_FIELD, GPA_MODE, GPA_TOTAL, GPA_SINGLE,
    # Percent + GPA
    PCT_FIELD, PCT_REGION, PCT_GPA, PCT_SUBJECTS_INPUT,
    # آزمون آزمایشی
    EXAM_TYPE, EXAM_TARAZ,
    # درباره مدرسه
    ABOUT_MENU,
) = range(15)


# ==================== KEYBOARDS ====================
main_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📊 تخمین رتبه با تراز کل")],
        [KeyboardButton("📈 تخمین تراز از معدل")],
        [KeyboardButton("🧪 تخمین رتبه از درصد + معدل")],
        [KeyboardButton("📝 تخمین از آزمون آزمایشی")],
        [KeyboardButton("🏫 درباره مدرسه الف")],
        [KeyboardButton("❌ لغو")],
    ],
    resize_keyboard=True,
)

field_keyboard = ReplyKeyboardMarkup(
    [[KeyboardButton("🧬 تجربی"), KeyboardButton("📐 ریاضی")]],
    resize_keyboard=True,
    one_time_keyboard=True,
)

region_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🥇 منطقه ۱"),
            KeyboardButton("🥈 منطقه ۲"),
            KeyboardButton("🥉 منطقه ۳"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

gpa_mode_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📘 معدل کل")],
        [KeyboardButton("📚 تک‌درس (با ضریب)")],
        [KeyboardButton("🔙 بازگشت")],
    ],
    resize_keyboard=True,
)

exam_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📌 ماز"), KeyboardButton("📌 قلمچی")],
        [KeyboardButton("📌 گزینه دو")],
        [KeyboardButton("🔙 بازگشت به منوی اصلی")],
    ],
    resize_keyboard=True,
)

about_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🔢 فرمول ۴+۳")],
        [KeyboardButton("🏠 پانسیون مطالعاتی VIP")],
        [KeyboardButton("🏆 رتبه‌های ۱۴۰۴")],
        [KeyboardButton("👨‍🏫 اساتید")],
        [KeyboardButton("📞 تماس و شعب")],
        [KeyboardButton("🔙 بازگشت به منوی اصلی")],
    ],
    resize_keyboard=True,
)


# ==================== HELPERS ====================
async def typing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING,
    )


def parse_number(text: str):
    text = text.strip().replace(",", "").replace("،", "").replace(" ", "")
    try:
        return float(text)
    except ValueError:
        return None


# ==================== START ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await typing(update, context)

    welcome = (
        "🎓 *آکادمی الف | Academy Alef*\n"
        "«یادگیری هوشمند، موفقیت پایدار»\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "ارائه خدمات آموزشی و مشاوره‌ای:\n\n"
        "🏠 تحصیل در منزل (Homeschool)\n"
        "📝 آزمون‌های آموزشی\n"
        "🌙 کلاس‌های شب امتحان\n"
        "🎯 کلاس‌های کنکور و جمع‌بندی سه‌پایه\n"
        "💬 مشاوره تحصیلی و انگیزشی\n"
        "🧭 انتخاب رشته\n"
        "📚 پانسیون مطالعاتی\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "✨ *آینده را آگاهانه بساز.*\n\n"
        "از منوی زیر سرویس مورد نظرت را انتخاب کن 👇"
    )

    await update.message.reply_text(
        welcome,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=main_keyboard,
    )
    return MAIN_MENU


# ==================== MAIN MENU ====================
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "📊 تخمین رتبه با تراز کل":
        await typing(update, context)
        await update.message.reply_text(
            "📊 *تخمین رتبه با تراز کل*\n\nابتدا رشته خودت را انتخاب کن:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=field_keyboard,
        )
        return RANK_FIELD

    elif text == "📈 تخمین تراز از معدل":
        await typing(update, context)
        await update.message.reply_text(
            "📈 *تخمین تراز از معدل*\n\nرشته خودت را انتخاب کن:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=field_keyboard,
        )
        return GPA_FIELD

    elif text == "🧪 تخمین رتبه از درصد + معدل":
        await typing(update, context)
        await update.message.reply_text(
            "🧪 *تخمین رتبه از درصد دروس + معدل*\n\nرشته خودت را انتخاب کن:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=field_keyboard,
        )
        return PCT_FIELD

    elif text == "📝 تخمین از آزمون آزمایشی":
        await typing(update, context)
        await update.message.reply_text(
            "📝 *تخمین سطح بر اساس آزمون آزمایشی*\n\n"
            "کدام آزمون را شرکت کرده‌ای؟",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=exam_keyboard,
        )
        return EXAM_TYPE

    elif text == "🏫 درباره مدرسه الف":
        await typing(update, context)
        await update.message.reply_text(
            "🏫 *درباره مدرسه کنکور الف*\n\n"
            "یکی از موضوعات زیر را انتخاب کن:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=about_keyboard,
        )
        return ABOUT_MENU

    elif text == "❌ لغو":
        return await cancel(update, context)

    else:
        await update.message.reply_text(
            "لطفاً یکی از گزینه‌های منو را انتخاب کن.",
            reply_markup=main_keyboard,
        )
        return MAIN_MENU


# ============================================================
# 1) تخمین رتبه با تراز کل
# ============================================================
async def rank_field(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "تجربی" in text:
        context.user_data["field"] = "tajrobi"
    elif "ریاضی" in text:
        context.user_data["field"] = "riazi"
    else:
        await update.message.reply_text("لطفاً یکی از دکمه‌ها را انتخاب کن.", reply_markup=field_keyboard)
        return RANK_FIELD

    await typing(update, context)
    await update.message.reply_text(
        "✅ رشته ثبت شد.\n\n📍 حالا منطقه را انتخاب کن:",
        reply_markup=region_keyboard,
    )
    return RANK_REGION


async def rank_region(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    region_map = {
        "🥇 منطقه ۱": "1", "🥈 منطقه ۲": "2", "🥉 منطقه ۳": "3",
        "منطقه ۱": "1", "منطقه ۲": "2", "منطقه ۳": "3",
    }
    if text not in region_map:
        await update.message.reply_text("لطفاً یکی از مناطق را انتخاب کن.", reply_markup=region_keyboard)
        return RANK_REGION

    context.user_data["region"] = region_map[text]
    await typing(update, context)
    await update.message.reply_text(
        "📈 حالا *تراز کل* خودت را وارد کن:\n\nمثال: `8750`",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=ReplyKeyboardRemove(),
    )
    return RANK_SCORE


async def rank_score(update: Update, context: ContextTypes.DEFAULT_TYPE):
    score = parse_number(update.message.text)
    if score is None or score < 5000 or score > 13000:
        await update.message.reply_text("⚠️ تراز معتبر وارد کن (حدود ۵۰۰۰ تا ۱۳۰۰۰).")
        return RANK_SCORE

    field = context.user_data["field"]
    region = context.user_data["region"]

    await typing(update, context)
    loading = await update.message.reply_text("⏳ در حال محاسبه...")

    await asyncio.sleep(0.15)
    rank = find_rank(field, region, score)
    result = format_rank_result(field, region, score, rank)

    await loading.edit_text(result, parse_mode=ParseMode.MARKDOWN)
    await update.message.reply_text("برای ادامه از منوی زیر استفاده کن:", reply_markup=main_keyboard)
    context.user_data.clear()
    return MAIN_MENU


# ============================================================
# 2) تخمین تراز از معدل
# ============================================================
async def gpa_field(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "تجربی" in text:
        context.user_data["field"] = "tajrobi"
    elif "ریاضی" in text:
        context.user_data["field"] = "riazi"
    else:
        await update.message.reply_text("لطفاً یکی از دکمه‌ها را انتخاب کن.", reply_markup=field_keyboard)
        return GPA_FIELD

    await typing(update, context)
    await update.message.reply_text(
        "کدام روش را می‌خواهی؟",
        reply_markup=gpa_mode_keyboard,
    )
    return GPA_MODE


async def gpa_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "📘 معدل کل":
        await typing(update, context)
        await update.message.reply_text(
            "معدل نهایی (دیپلم) خودت را وارد کن:\n\nمثال: `18.50`",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=ReplyKeyboardRemove(),
        )
        return GPA_TOTAL

    elif text == "📚 تک‌درس (با ضریب)":
        field = context.user_data["field"]
        subjects = GPA_COEF[field]
        context.user_data["gpa_scores"] = {}
        context.user_data["gpa_index"] = 0
        context.user_data["gpa_subjects"] = subjects

        first = subjects[0]
        await typing(update, context)
        await update.message.reply_text(
            f"نمره درس *{first['name']}* را وارد کن (۱۰ تا ۲۰):\n"
            f"ضریب: `{first['coef']}`",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=ReplyKeyboardRemove(),
        )
        return GPA_SINGLE

    elif text == "🔙 بازگشت":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)
        return MAIN_MENU

    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کن.", reply_markup=gpa_mode_keyboard)
        return GPA_MODE


async def gpa_total(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gpa = parse_number(update.message.text)
    if gpa is None or gpa < 10 or gpa > 20:
        await update.message.reply_text("⚠️ معدل معتبر وارد کن (۱۰ تا ۲۰).")
        return GPA_TOTAL

    taraz = gpa_to_taraz(gpa)
    field_name = "تجربی" if context.user_data["field"] == "tajrobi" else "ریاضی"

    result = (
        f"📈 *نتیجه تخمین تراز از معدل*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎓 رشته: *{field_name}*\n"
        f"📊 معدل: *{gpa}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏆 تراز تخمینی:\n*{taraz}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💡 این تب فقط تراز می‌دهد و رتبه محاسبه نمی‌شود."
    )

    await typing(update, context)
    await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN, reply_markup=main_keyboard)
    context.user_data.clear()
    return MAIN_MENU


async def gpa_single(update: Update, context: ContextTypes.DEFAULT_TYPE):
    score = parse_number(update.message.text)
    if score is None or score < 10 or score > 20:
        await update.message.reply_text("⚠️ نمره معتبر وارد کن (۱۰ تا ۲۰).")
        return GPA_SINGLE

    subjects = context.user_data["gpa_subjects"]
    idx = context.user_data["gpa_index"]
    current = subjects[idx]

    context.user_data["gpa_scores"][current["id"]] = score
    idx += 1
    context.user_data["gpa_index"] = idx

    if idx < len(subjects):
        next_subj = subjects[idx]
        await update.message.reply_text(
            f"نمره درس *{next_subj['name']}* را وارد کن (۱۰ تا ۲۰):\n"
            f"ضریب: `{next_subj['coef']}`",
            parse_mode=ParseMode.MARKDOWN,
        )
        return GPA_SINGLE

    weighted = calc_weighted_gpa(context.user_data["gpa_scores"], context.user_data["field"])
    if weighted is None:
        await update.message.reply_text("خطا در محاسبه معدل وزنی.", reply_markup=main_keyboard)
        return MAIN_MENU

    taraz = gpa_to_taraz(weighted)
    field_name = "تجربی" if context.user_data["field"] == "tajrobi" else "ریاضی"

    result = (
        f"📈 *نتیجه تخمین تراز از معدل وزنی*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎓 رشته: *{field_name}*\n"
        f"📊 معدل وزنی: *{weighted:.2f}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏆 تراز تخمینی:\n*{taraz}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💡 این تب فقط تراز می‌دهد و رتبه محاسبه نمی‌شود."
    )

    await typing(update, context)
    await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN, reply_markup=main_keyboard)
    context.user_data.clear()
    return MAIN_MENU


# ============================================================
# 3) تخمین رتبه از درصد + معدل
# ============================================================
async def pct_field(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if "تجربی" in text:
        context.user_data["field"] = "tajrobi"
    elif "ریاضی" in text:
        context.user_data["field"] = "riazi"
    else:
        await update.message.reply_text("لطفاً یکی از دکمه‌ها را انتخاب کن.", reply_markup=field_keyboard)
        return PCT_FIELD

    await typing(update, context)
    await update.message.reply_text(
        "✅ رشته ثبت شد.\n\n📍 حالا منطقه را انتخاب کن:",
        reply_markup=region_keyboard,
    )
    return PCT_REGION


async def pct_region(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    region_map = {
        "🥇 منطقه ۱": "1", "🥈 منطقه ۲": "2", "🥉 منطقه ۳": "3",
        "منطقه ۱": "1", "منطقه ۲": "2", "منطقه ۳": "3",
    }
    if text not in region_map:
        await update.message.reply_text("لطفاً یکی از مناطق را انتخاب کن.", reply_markup=region_keyboard)
        return PCT_REGION

    context.user_data["region"] = region_map[text]
    await typing(update, context)
    await update.message.reply_text(
        "معدل نهایی (دیپلم) خودت را وارد کن:\n\nمثال: `18.20`",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=ReplyKeyboardRemove(),
    )
    return PCT_GPA


async def pct_gpa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gpa = parse_number(update.message.text)
    if gpa is None or gpa < 10 or gpa > 20:
        await update.message.reply_text("⚠️ معدل معتبر وارد کن (۱۰ تا ۲۰).")
        return PCT_GPA

    context.user_data["gpa"] = gpa
    field = context.user_data["field"]
    subjects = PCT_SUBJECTS[field]
    context.user_data["pct_scores"] = {}
    context.user_data["pct_index"] = 0
    context.user_data["pct_subjects"] = subjects

    first = subjects[0]
    await typing(update, context)
    await update.message.reply_text(
        f"درصد درس *{first['name']}* را وارد کن (۰ تا ۱۰۰):\n\nمثال: `55`",
        parse_mode=ParseMode.MARKDOWN,
    )
    return PCT_SUBJECTS_INPUT


async def pct_subjects_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pct = parse_number(update.message.text)
    if pct is None or pct < 0 or pct > 100:
        await update.message.reply_text("⚠️ درصد معتبر وارد کن (۰ تا ۱۰۰).")
        return PCT_SUBJECTS_INPUT

    subjects = context.user_data["pct_subjects"]
    idx = context.user_data["pct_index"]
    current = subjects[idx]

    context.user_data["pct_scores"][current["id"]] = pct
    idx += 1
    context.user_data["pct_index"] = idx

    if idx < len(subjects):
        next_subj = subjects[idx]
        await update.message.reply_text(
            f"درصد درس *{next_subj['name']}* را وارد کن (۰ تا ۱۰۰):",
            parse_mode=ParseMode.MARKDOWN,
        )
        return PCT_SUBJECTS_INPUT

    scores = list(context.user_data["pct_scores"].values())
    avg_pct = sum(scores) / len(scores)
    gpa = context.user_data["gpa"]
    field = context.user_data["field"]
    region = context.user_data["region"]

    gpa_taraz = gpa_to_taraz(gpa)
    pct_taraz = percent_to_taraz(avg_pct)
    final_taraz = min(10700, round(gpa_taraz * 0.6 + pct_taraz * 0.4))
    rank = find_rank(field, region, final_taraz)

    field_name = "تجربی" if field == "tajrobi" else "ریاضی"
    status = get_status(rank) if rank else "—"
    rank_text = rank if rank else "خارج از بازه"

    result = (
        f"🎉 *نتیجه تخمین رتبه (درصد + معدل)*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎓 رشته: *{field_name}*\n"
        f"📍 منطقه: *{region}*\n"
        f"📊 معدل: *{gpa}*\n"
        f"🧪 میانگین درصد: *{avg_pct:.1f}%*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"تراز معدل: `{gpa_taraz}`\n"
        f"تراز درصد: `{pct_taraz}`\n"
        f"تراز نهایی (۶۰٪ + ۴۰٪): *{final_taraz}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏆 تخمین رتبه:\n*{rank_text}*\n\n"
        f"📈 وضعیت: *{status}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💡 این تخمین تقریبی است."
    )

    await typing(update, context)
    await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN, reply_markup=main_keyboard)
    context.user_data.clear()
    return MAIN_MENU


# ============================================================
# 4) تخمین از آزمون آزمایشی
# ============================================================
async def exam_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    mapping = {
        "📌 ماز": "maz",
        "📌 قلمچی": "ghalamchi",
        "📌 گزینه دو": "gozine2",
    }

    if text == "🔙 بازگشت به منوی اصلی":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)
        return MAIN_MENU

    if text not in mapping:
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کن.", reply_markup=exam_keyboard)
        return EXAM_TYPE

    context.user_data["exam_type"] = mapping[text]
    exam_name = {"maz": "ماز", "ghalamchi": "قلمچی", "gozine2": "گزینه دو"}[mapping[text]]

    await typing(update, context)
    await update.message.reply_text(
        f"✅ آزمون: *{exam_name}*\n\n"
        f"حالا تراز خودت را وارد کن:",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=ReplyKeyboardRemove(),
    )
    return EXAM_TARAZ


async def exam_taraz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    taraz = parse_number(update.message.text)
    if taraz is None:
        await update.message.reply_text("⚠️ لطفاً یک عدد معتبر وارد کن.")
        return EXAM_TARAZ

    exam_type_val = context.user_data.get("exam_type")
    result = evaluate_exam_taraz(exam_type_val, taraz)

    await typing(update, context)
    await update.message.reply_text(result, parse_mode=ParseMode.MARKDOWN, reply_markup=main_keyboard)
    context.user_data.clear()
    return MAIN_MENU


# ============================================================
# 5) درباره مدرسه الف
# ============================================================
async def about_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "🔙 بازگشت به منوی اصلی":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)
        return MAIN_MENU

    await typing(update, context)

    if text == "🔢 فرمول ۴+۳":
        msg = (
            "🔢 *فرمول آموزش مؤثر ۴+۳*\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "۳ روز آموزش و یادگیری (شنبه، دوشنبه، چهارشنبه)\n"
            "• از ساعت ۹ صبح حضور در پانسیون\n"
            "• از ساعت ۱۳ کلاس‌های تدریس مفهومی\n\n"
            "۴ روز تسلط و تثبیت (یکشنبه، سه‌شنبه، پنجشنبه، جمعه)\n"
            "• تمرین و تست در منزل\n"
            "• مرور و رفع اشکال\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "این فرمول باعث می‌شود هم برای امتحانات نهایی و هم برای کنکور آماده شوید."
        )

    elif text == "🏠 پانسیون مطالعاتی VIP":
        msg = (
            "🏠 *پانسیون مطالعاتی VIP*\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "• مطالعه با کیفیت بالاتر از منزل\n"
            "• نظم و انضباط مطالعاتی بالا\n"
            "• تحت نظارت ناظر آموزشی\n"
            "• اصلاح عادات اشتباه مطالعاتی\n"
            "• پیش‌مطالعه و مرور مطالب هفته قبل\n\n"
            "صبح روزهایی که کلاس دارید، در پانسیون پیش‌مطالعه می‌کنید تا با آمادگی ۱۰۰٪ وارد کلاس شوید."
        )

    elif text == "🏆 رتبه‌های ۱۴۰۴":
        msg = (
            "🏆 *رتبه‌های آکادمی الف در کنکور ۱۴۰۴*\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "• جاوید جیشی — رتبه ۶۲ (ریاضی)\n"
            "• عرفان جعفری — رتبه ۱۱۱ (ریاضی)\n"
            "• محمدسالار اسمعیلیان — رتبه ۲۲۱ (تجربی)\n"
            "• هانیه فرحزادی — رتبه ۴۴۴ (انسانی)\n"
            "• هادی سوری — رتبه ۴۷۸ (ریاضی)\n"
            "• مینا امیریان مقدم — رتبه ۹۷۷ (تجربی)\n"
            "• آیناز قاسمی‌نژاد — رتبه ۱۰۵۸ (تجربی)\n"
            "• رضا عسگری — رتبه ۱۵۱۹ (ریاضی)\n"
            "• محمدطاها قربانیان — رتبه ۲۰۲۵ (تجربی)\n"
            "• امیرمهدی ظریفی — رتبه ۲۲۷۱ (تجربی)\n\n"
            "و بسیاری رتبه‌های دیگر..."
        )

    elif text == "👨‍🏫 اساتید":
        msg = (
            "👨‍🏫 *برترین اساتید کنکور ایران*\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "📐 *دپارتمان ریاضی*\n"
            "• رضا بغدادی\n• سیاوش محب\n• سامان سلامیان\n\n"
            "⚛️ *دپارتمان فیزیک*\n"
            "• فرزاد حقوقی\n• علی عباسی\n\n"
            "🧬 *دپارتمان زیست*\n"
            "• عارف اثناعشری\n• ابوالفضل جعفری\n\n"
            "🧪 *دپارتمان شیمی*\n"
            "• پرهام اشتهاردی\n• امیر اصلانی‌زاده\n\n"
            "و اساتید قوی در دروس عمومی..."
        )

    elif text == "📞 تماس و شعب":
        msg = (
            "📞 *راه‌های ارتباطی و شعب*\n\n"
            "━━━━━━━━━━━━━━━━━━━━\n\n"
            "☎️ تلفن: ۰۲۱-۹۱۰۱۷۹۳۵\n\n"
            "📍 *شعبه سیدخندان (شرق)*\n"
            "خیابان خواجه عبدالله، خیابان هشتم، نبش کوچه یاس، پلاک ۱۶\n"
            "تلفن: ۰۲۱-۲۲۸۶۴۲۶۲\n\n"
            "📍 *شعبه ستارخان (غرب)*\n"
            "خیابان ستارخان، نبش خیابان بهبودی، پلاک ۱۸۸\n"
            "تلفن: ۰۲۱-۶۶۵۰۸۵۸۶ | ۰۲۱-۶۶۵۵۳۷۴۴\n\n"
            "🌐 وبسایت: alefac.ir\n"
            "📸 اینستاگرام: @arsalan.firouznia\n"
            "✈️ تلگرام: @arsalanfirouznia"
        )

    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کن.", reply_markup=about_keyboard)
        return ABOUT_MENU

    await update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=about_keyboard)
    return ABOUT_MENU


# ==================== CANCEL ====================
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        "🛑 عملیات لغو شد.\n\nبرای شروع دوباره /start را بزن.",
        reply_markup=ReplyKeyboardRemove(),
    )
    return ConversationHandler.END


# ==================== COMMANDS ====================
async def set_commands(application: Application):
    await application.bot.set_my_commands(
        [
            BotCommand("start", "شروع ربات و منوی اصلی"),
            BotCommand("cancel", "لغو عملیات"),
        ]
    )


# ==================== MAIN ====================
def main():
    if not TOKEN:
        print("❌ BOT_TOKEN پیدا نشد.")
        return

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    builder = Application.builder().token(TOKEN)
    if PROXY_URL:
        print(f"🌐 Proxy: {PROXY_URL}")
        builder = builder.proxy(PROXY_URL).get_updates_proxy(PROXY_URL)

    app = builder.build()
    app.post_init = set_commands

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MAIN_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu)],
            # Rank by taraz
            RANK_FIELD: [MessageHandler(filters.TEXT & ~filters.COMMAND, rank_field)],
            RANK_REGION: [MessageHandler(filters.TEXT & ~filters.COMMAND, rank_region)],
            RANK_SCORE: [MessageHandler(filters.TEXT & ~filters.COMMAND, rank_score)],
            # GPA → Taraz
            GPA_FIELD: [MessageHandler(filters.TEXT & ~filters.COMMAND, gpa_field)],
            GPA_MODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, gpa_mode)],
            GPA_TOTAL: [MessageHandler(filters.TEXT & ~filters.COMMAND, gpa_total)],
            GPA_SINGLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, gpa_single)],
            # Percent + GPA
            PCT_FIELD: [MessageHandler(filters.TEXT & ~filters.COMMAND, pct_field)],
            PCT_REGION: [MessageHandler(filters.TEXT & ~filters.COMMAND, pct_region)],
            PCT_GPA: [MessageHandler(filters.TEXT & ~filters.COMMAND, pct_gpa)],
            PCT_SUBJECTS_INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, pct_subjects_input)],
            # Exam
            EXAM_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, exam_type)],
            EXAM_TARAZ: [MessageHandler(filters.TEXT & ~filters.COMMAND, exam_taraz)],
            # About
            ABOUT_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, about_menu)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
    )

    app.add_handler(conv)
    app.add_handler(CommandHandler("cancel", cancel))

    print("=" * 45)
    print("🎓 Academy Alef Rank Bot Started")
    print("=" * 45)
    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
        timeout=10,
    )


if __name__ == "__main__":
    main()
