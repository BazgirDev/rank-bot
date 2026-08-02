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
    # زیرمنوها
    RANK_MENU, ACADEMY_MENU, SCHOOL_MENU,
) = range(17)


# ==================== MEDIA FILES ====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RANKS_IMAGE = os.path.join(BASE_DIR, "assets", "ranks.jpg")
PANSION_IMAGE = os.path.join(BASE_DIR, "assets", "pansion.jpg")
TEACHERS_IMAGE_1 = os.path.join(BASE_DIR, "assets", "teachers_1.jpg")
TEACHERS_IMAGE_2 = os.path.join(BASE_DIR, "assets", "teachers_2.jpg")
PLAN_IMAGE = os.path.join(BASE_DIR, "assets", "plan_4plus3.jpg")


# ==================== EDITABLE TEXTS ====================
RANKS_TEXT = (
    "🏆 *رتبه‌های برتر آکادمی الف*\n\n"
    "━━━━━━━━━━━━━━━━━━━━\n\n"
    "• جاوید جیشی — رتبه ۶۲ ریاضی\n"
    "• عرفان جعفری — رتبه ۱۱۱ ریاضی\n"
    "• محمدسالار اسمعیلیان — رتبه ۲۲۱ تجربی\n"
    "• هانیه فرحزادی — رتبه ۴۴۴ انسانی\n"
    "• هادی سوری — رتبه ۴۷۸ ریاضی\n"
    "• مینا امیریان‌مقدم — رتبه ۹۷۷ تجربی\n"
    "• آیناز قاسمی‌نژاد — رتبه ۱۰۵۸ تجربی\n"
    "• رضا عسگری — رتبه ۱۵۱۹ ریاضی\n"
    "• محمدطاها قربانیان — رتبه ۲۰۲۵ تجربی\n"
    "• امیرمهدی ظریفی — رتبه ۲۲۷۱ تجربی\n\n"
    "این نتایج، حاصل برنامه‌ریزی منظم، آموزش هدفمند و پیگیری مستمر دانش‌آموزان است."
)

PANSION_TEXT = (
    "🏠 *پانسیون مطالعاتی آکادمی الف*\n\n"
    "پانسیون، محیطی آرام، منظم و کاملاً آموزشی برای مطالعه عمیق و افزایش بازدهی است. "
    "دانش‌آموزان در روزهای برگزاری کلاس، از ساعت ۹:۰۰ تا ۱۲:۳۰ در پانسیون حضور دارند "
    "و پیش از شروع کلاس‌ها، پیش‌مطالعه، مرور و حل تمرین انجام می‌دهند.\n\n"
    "• تحویل موبایل و وسایل هوشمند برای حذف حواس‌پرتی\n"
    "• نظارت ناظران و مشاوران آموزشی در تمام ساعات\n"
    "• اصلاح عادت‌های اشتباه مطالعاتی\n"
    "• ایجاد نظم و انضباط پایدار\n"
    "• استفاده حداکثری از زمان پیش از کلاس\n"
    "• افزایش تمرکز و کیفیت یادگیری\n\n"
    "برنامه روزانه: ۹:۰۰ تا ۱۲:۳۰ پانسیون و مطالعه، ۱۳:۰۰ تا ۱۴:۰۰ استراحت و ناهار، "
    "و از ساعت ۱۴:۰۰ شروع کلاس‌ها."
)

TEACHERS_TEXT_1 = (
    "👨‍🏫 *اساتید آکادمی الف — بخش اول*\n\n"
    "📐 *دپارتمان ریاضی*\n"
    "• رضا بغدادیچی: فوق‌لیسانس مهندسی صنایع؛ ۲۰ سال سابقه تدریس در مدارس تهران.\n"
    "• سامان سلیمان: دکترای روان‌شناسی و مهندسی عمران دانشگاه امیرکبیر؛ مدرس فیلم‌های آموزشی گاج.\n\n"
    "⚛️ *دپارتمان فیزیک*\n"
    "• علی عباسی: ۱۷ سال سابقه تدریس در مدارس و آموزشگاه‌های معتبر تهران.\n\n"
    "🧬 *دپارتمان زیست‌شناسی*\n"
    "• ابوالفضل جعفری: کارشناس زیست‌شناسی؛ مؤلف کتاب‌های زیست تصویری و زیست جیبی.\n\n"
    "🧪 *دپارتمان شیمی*\n"
    "• پرهام اشتهاردی: کارشناسی ارشد شیمی آلی؛ مؤلف کتاب شیمی جامع علوی.\n"
    "• امیر اصلانی‌زاده: کارشناسی ارشد مهندسی شیمی دانشگاه شریف؛ رتبه ۶ کنکور ارشد و رتبه ۲۰۰ کنکور."
)

TEACHERS_TEXT_2 = (
    "👨‍🏫 *اساتید آکادمی الف — بخش دوم*\n\n"
    "📏 *دپارتمان هندسه و گسسته*\n"
    "• میثم امین: مؤلف کتاب «سوت پایان» رشته ریاضی و کتاب آمار و احتمال یازدهم؛ مدرس مدارس برتر تهران از جمله فرزانگان و پیشگامان.\n"
    "• محمد ارباب‌بهرامی: مؤلف کتاب‌های میکرو گاج، طراح و تحلیل‌گر آزمون‌های قلم‌چی؛ مدرس مدارس علامه حلی و ملاصدرا.\n\n"
    "📖 *دپارتمان عربی*\n"
    "• پیمان کشاورز: فوق‌لیسانس مهندسی صنایع از دانشگاه تربیت مدرس؛ بیش از ۲۰ سال سابقه تدریس.\n\n"
    "🇬🇧 *دپارتمان زبان انگلیسی*\n"
    "• فریبا کمال‌آبادی: کارشناسی ارشد آموزش زبان انگلیسی؛ ۲۲ سال سابقه تدریس.\n\n"
    "📝 *دپارتمان ادبیات فارسی*\n"
    "• ابراهیم کاظمی‌مقدم: دکترای زبان و ادبیات فارسی؛ مؤلف کتاب‌های پیک نخبگان و نادوشان؛ ۲۸ سال سابقه فعالیت آموزشی و ۱۲ سال سابقه تدریس پروازی."
)

PLAN_4PLUS3_TEXT = (
    "🎯 *پلن جامع ۴+۳ مدرسه کنکور الف*\n\n"
    "پلن ۴+۳ یک برنامه هفتگی یکپارچه برای آمادگی هم‌زمان در امتحانات نهایی و کنکور سراسری است. "
    "در این مدل، آموزش، آزمون، مشاوره و سبک مطالعه در یک مسیر هماهنگ قرار می‌گیرند تا دانش‌آموز "
    "میان برنامه تشریحی مدرسه و برنامه تستی کنکور دچار تداخل نشود.\n\n"
    "📘 *۳ روز آموزش مفهومی*\n"
    "شنبه، دوشنبه و چهارشنبه روزهای آموزش هستند. دانش‌آموز از ساعت ۹:۰۰ تا ۱۲:۳۰ در پانسیون "
    "مطالعاتی، پیش‌مطالعه و مرور انجام می‌دهد؛ سپس بعد از زمان استراحت و ناهار، کلاس‌های آموزشی "
    "از ساعت ۱۳ یا ۱۴ آغاز می‌شوند و برنامه آموزشی تا حدود ساعت ۱۹ ادامه دارد. تدریس‌ها هم‌زمان "
    "ابعاد تشریحی و تستی هر درس را پوشش می‌دهند.\n\n"
    "📚 *۴ روز تسلط و تثبیت*\n"
    "یکشنبه، سه‌شنبه، پنجشنبه و جمعه برای تمرین، تست، مرور، تکمیل تکالیف، رفع اشکال و تثبیت مطالب "
    "سه روز آموزشی در نظر گرفته شده‌اند. این فاصله هدفمند میان جلسات باعث می‌شود مطالب فقط شنیده "
    "نشوند، بلکه با تمرین و بازیابی فعال به یادگیری پایدار تبدیل شوند.\n\n"
    "🧭 *مشاوره و پایش تحصیلی*\n"
    "برنامه‌ریزی به‌صورت سال‌محور و هفته‌محور انجام می‌شود. جلسات گروهی ماهانه با مهندس ارسلان "
    "فیروزنیا، امکان طرح مستقیم پرسش‌ها، بررسی روند مطالعه و اصلاح برنامه، دانش‌آموز را در تمام مسیر "
    "همراهی می‌کند. ناظران آموزشی نیز نظم، حضور و کیفیت اجرای برنامه را پیگیری می‌کنند.\n\n"
    "🧠 *تراپی و سلامت روان*\n"
    "در کنار آموزش، خدمات روان‌شناسی، مدیتیشن، مشاوره انگیزشی و مشاوره تغذیه برای مدیریت اضطراب، "
    "فرسودگی و افت انگیزه در نظر گرفته شده است. هدف این است که دانش‌آموز مسیر کنکور را با تمرکز، "
    "تعادل روانی و انرژی پایدار طی کند.\n\n"
    "✨ نتیجه این ساختار، استفاده بهتر از زمان، حذف رفت‌وآمدهای غیرضروری، افزایش نظم مطالعاتی و "
    "آمادگی هماهنگ برای کسب معدل نهایی بالا و درصدهای رقابتی در کنکور است."
)

PLAN_STRATEGY_TEXT = (
    "🧩 *استراتژی پلن ۴+۳*\n\n"
    "این استراتژی بر چرخه «آموزش ← تمرین ← بازخورد ← تثبیت» استوار است:\n\n"
    "۱) سه روز تدریس مفهومی و هم‌زمان تستی–تشریحی\n"
    "۲) چهار روز تمرین، تست، مرور و رفع اشکال\n"
    "۳) پیش‌مطالعه در پانسیون پیش از ورود به کلاس\n"
    "۴) پایش مستمر توسط مشاور و ناظر آموزشی\n"
    "۵) پشتیبانی روان‌شناختی، مدیتیشن و مشاوره تغذیه\n\n"
    "در این مدل هر جلسه آموزشی فرصت کافی برای تبدیل‌شدن به مهارت و تسلط واقعی پیدا می‌کند."
)

CONTACT_TEXT = (
    "📞 *ارتباط با آکادمی الف*\n\n"
    "📍 *شعبه سیدخندان (شرق تهران)*\n"
    "خیابان خواجه عبدالله، خیابان هشتم، نبش کوچه یاس، پلاک ۱۶\n"
    "تلفن: ۰۲۱-۲۲۸۶۴۲۶۲\n\n"
    "📍 *شعبه ستارخان (غرب تهران)*\n"
    "خیابان ستارخان، نبش خیابان بهبودی، پلاک ۱۸۸\n"
    "تلفن: ۰۲۱-۶۶۵۰۸۵۸۶\n"
    "تلفن: ۰۲۱-۶۶۵۵۳۷۴۴\n\n"
    "🌐 وب‌سایت: alefac.ir\n"
    "📸 اینستاگرام: @arsalan.firouznia\n"
    "✈️ تلگرام: @arsalanfirouznia\n"
    "💬 بله: @arsalanfiruznia"
)


# ==================== KEYBOARDS ====================
main_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🎯 تخمین رتبه کنکور سراسری")],
        [KeyboardButton("🏛 درباره آکادمی الف")],
        [KeyboardButton("🏫 مدرسه کنکور الف")],
        [KeyboardButton("📞 ارتباط با ما")],
    ],
    resize_keyboard=True,
)

rank_tools_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📊 تخمین رتبه کنکور با تراز کل")],
        [KeyboardButton("📈 تخمین تراز معدل امتحان نهایی")],
        [KeyboardButton("🧪 تخمین رتبه با درصد + معدل نهایی")],
        [KeyboardButton("📝 تخمین تراز از آزمون آزمایشی")],
        [KeyboardButton("🔙 بازگشت به منوی اصلی")],
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
        [KeyboardButton("🔙 بازگشت به تخمین رتبه")],
    ],
    resize_keyboard=True,
)

academy_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🏆 رتبه‌های برتر")],
        [KeyboardButton("🏠 پانسیون مطالعاتی")],
        [KeyboardButton("👨‍🏫 اساتید")],
        [KeyboardButton("🔙 بازگشت به منوی اصلی")],
    ],
    resize_keyboard=True,
)

school_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("📘 پلن جامع ۴+۳")],
        [KeyboardButton("🧩 استراتژی پلن ۴+۳")],
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


async def send_photo_with_caption(update: Update, context: ContextTypes.DEFAULT_TYPE, photo_path, caption):
    """عکس را با کپشن می‌فرستد و اگر فایل موجود نباشد، فقط متن را ارسال می‌کند."""
    if os.path.isfile(photo_path):
        with open(photo_path, "rb") as photo:
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo,
                caption=caption,
                parse_mode=ParseMode.MARKDOWN,
            )
    else:
        logger.warning("Image file not found: %s", photo_path)
        await update.message.reply_text(caption, parse_mode=ParseMode.MARKDOWN)


# ==================== START ====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await typing(update, context)

    welcome = (
        "🎓 *آکادمی الف | Academy Alef*\n"
        "«یادگیری هوشمند، موفقیت پایدار»\n\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "به دستیار هوشمند آکادمی الف خوش آمدید.\n\n"
        "از منوی زیر یکی از چهار بخش اصلی را انتخاب کنید 👇"
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

    if text == "🎯 تخمین رتبه کنکور سراسری":
        await typing(update, context)
        await update.message.reply_text(
            "🎯 *تخمین رتبه کنکور سراسری*\n\nروش موردنظر را انتخاب کنید:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=rank_tools_keyboard,
        )
        return RANK_MENU

    elif text == "🏛 درباره آکادمی الف":
        await typing(update, context)
        await update.message.reply_text(
            "🏛 *درباره آکادمی الف*\n\n"
            "آکادمی الف مجموعه‌ای آموزشی با تمرکز بر آموزش هدفمند، مشاوره، "
            "پانسیون مطالعاتی و همراهی مستمر دانش‌آموزان است.\n\n"
            "موضوع موردنظر را انتخاب کنید:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=academy_keyboard,
        )
        return ACADEMY_MENU

    elif text == "🏫 مدرسه کنکور الف":
        await typing(update, context)
        await update.message.reply_text(
            "🏫 *مدرسه کنکور الف*\n\n"
            "مدرسه‌ای تحت نظارت مهندس ارسلان فیروزنیا که کلاس، آزمون، "
            "مشاوره و سبک مطالعاتی آن برای موفقیت در کنکور و امتحان نهایی هماهنگ شده است.\n\n"
            "یکی از گزینه‌های زیر را انتخاب کنید:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=school_keyboard,
        )
        return SCHOOL_MENU

    elif text == "📞 ارتباط با ما":
        await typing(update, context)
        await update.message.reply_text(
            CONTACT_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=main_keyboard,
        )
        return MAIN_MENU

    else:
        await update.message.reply_text(
            "لطفاً یکی از گزینه‌های منو را انتخاب کن.",
            reply_markup=main_keyboard,
        )
        return MAIN_MENU


async def rank_tools_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "📊 تخمین رتبه کنکور با تراز کل":
        await typing(update, context)
        await update.message.reply_text(
            "📊 *تخمین رتبه کنکور با تراز کل*\n\nابتدا رشته خودت را انتخاب کن:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=field_keyboard,
        )
        return RANK_FIELD

    if text == "📈 تخمین تراز معدل امتحان نهایی":
        await typing(update, context)
        await update.message.reply_text(
            "📈 *تخمین تراز معدل امتحان نهایی*\n\nرشته خودت را انتخاب کن:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=field_keyboard,
        )
        return GPA_FIELD

    if text == "🧪 تخمین رتبه با درصد + معدل نهایی":
        await typing(update, context)
        await update.message.reply_text(
            "🧪 *تخمین رتبه با درصد دروس + معدل نهایی*\n\nرشته خودت را انتخاب کن:",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=field_keyboard,
        )
        return PCT_FIELD

    if text == "📝 تخمین تراز از آزمون آزمایشی":
        await typing(update, context)
        await update.message.reply_text(
            "📝 *تخمین تراز از آزمون آزمایشی*\n\nکدام آزمون را شرکت کرده‌ای؟",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=exam_keyboard,
        )
        return EXAM_TYPE

    if text == "🔙 بازگشت به منوی اصلی":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)
        return MAIN_MENU

    await update.message.reply_text(
        "لطفاً یکی از روش‌های تخمین را انتخاب کنید.",
        reply_markup=rank_tools_keyboard,
    )
    return RANK_MENU


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
    }

    if text == "🔙 بازگشت به تخمین رتبه":
        await update.message.reply_text("به منوی تخمین رتبه بازگشتید.", reply_markup=rank_tools_keyboard)
        return RANK_MENU

    if text not in mapping:
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کن.", reply_markup=exam_keyboard)
        return EXAM_TYPE

    context.user_data["exam_type"] = mapping[text]
    exam_name = {"maz": "ماز", "ghalamchi": "قلمچی"}[mapping[text]]

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
# 5) درباره آکادمی الف
# ============================================================
async def academy_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "🔙 بازگشت به منوی اصلی":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)
        return MAIN_MENU

    await typing(update, context)

    if text == "🏆 رتبه‌های برتر":
        await send_photo_with_caption(update, context, RANKS_IMAGE, RANKS_TEXT)
    elif text == "🏠 پانسیون مطالعاتی":
        await send_photo_with_caption(update, context, PANSION_IMAGE, PANSION_TEXT)
    elif text == "👨‍🏫 اساتید":
        await send_photo_with_caption(update, context, TEACHERS_IMAGE_1, TEACHERS_TEXT_1)
        await send_photo_with_caption(update, context, TEACHERS_IMAGE_2, TEACHERS_TEXT_2)
    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کنید.", reply_markup=academy_keyboard)
        return ACADEMY_MENU

    await update.message.reply_text("موضوع دیگری را انتخاب کنید:", reply_markup=academy_keyboard)
    return ACADEMY_MENU


# ============================================================
# 6) مدرسه کنکور الف و پلن ۴+۳
# ============================================================
async def school_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "🔙 بازگشت به منوی اصلی":
        await update.message.reply_text("به منوی اصلی بازگشتید.", reply_markup=main_keyboard)
        return MAIN_MENU

    await typing(update, context)

    if text == "📘 پلن جامع ۴+۳":
        await update.message.reply_text(
            PLAN_4PLUS3_TEXT,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=school_keyboard,
        )
    elif text == "🧩 استراتژی پلن ۴+۳":
        await send_photo_with_caption(update, context, PLAN_IMAGE, PLAN_STRATEGY_TEXT)
        await update.message.reply_text("گزینه دیگری را انتخاب کنید:", reply_markup=school_keyboard)
    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌ها را انتخاب کنید.", reply_markup=school_keyboard)

    return SCHOOL_MENU


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
            RANK_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, rank_tools_menu)],
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
            # Academy and school
            ACADEMY_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, academy_menu)],
            SCHOOL_MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, school_menu)],
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
