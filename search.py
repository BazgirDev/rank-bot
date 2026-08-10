"""داده‌ها و توابع محاسباتی ربات آکادمی الف."""

RANK_DATA = {
    "tajrobi": [
        {"min": 7000, "max": 7500, "ranks": {"1": "۲۵۰۰۰-۳۰۰۰۰", "2": "۳۲۰۰۰-۳۷۰۰۰", "3": "۲۳۰۰۰-۲۸۰۰۰"}},
        {"min": 7500, "max": 8000, "ranks": {"1": "۱۰۸۰۰-۱۳۰۰۰", "2": "۱۵۰۰۰-۲۰۰۰۰", "3": "۱۱۰۰۰-۱۳۲۰۰"}},
        {"min": 8000, "max": 8300, "ranks": {"1": "۸۸۰۰-۱۰۵۰۰", "2": "۱۲۰۰۰-۱۵۰۰۰", "3": "۹۰۰۰-۱۱۵۰۰"}},
        {"min": 8300, "max": 8700, "ranks": {"1": "۷۴۵۰-۹۰۵۰", "2": "۱۱۵۰۰-۱۳۷۰۰", "3": "۷۳۵۰-۹۲۰۰"}},
        {"min": 8700, "max": 9000, "ranks": {"1": "۳۹۰۰-۵۱۰۰", "2": "۵۳۰۰-۷۳۰۰", "3": "۳۱۵۰-۴۳۰۰"}},
        {"min": 9000, "max": 9300, "ranks": {"1": "۳۱۲۰-۴۰۰۰", "2": "۳۳۰۰-۴۸۰۰", "3": "۲۰۰۰-۳۰۰۰"}},
        {"min": 9300, "max": 9500, "ranks": {"1": "۱۴۸۰-۲۲۰۰", "2": "۲۳۲۰-۳۱۸۰", "3": "۸۸۰-۱۴۵۰"}},
        {"min": 9500, "max": 9800, "ranks": {"1": "۶۳۰-۹۸۰", "2": "۱۳۷۵-۲۰۷۰", "3": "۶۶۰-۱۱۸۰"}},
        {"min": 9800, "max": 10100, "ranks": {"1": "۶۱۰-۹۸۰", "2": "۵۲۰-۸۴۰", "3": "۳۰۰-۶۵۰"}},
        {"min": 10100, "max": 10400, "ranks": {"1": "۲۱۰-۵۸۰", "2": "۲۳۰-۴۸۰", "3": "۸۰-۲۸۰"}},
        {"min": 10400, "max": 99999, "ranks": {"1": "زیر ۲۰۰", "2": "زیر ۲۰۰", "3": "زیر ۷۰"}},
    ],
    "riazi": [
        {"min": 7000, "max": 7500, "ranks": {"1": "۸۱۰۰-۹۰۰۰", "2": "۵۴۰۰-۶۸۰۰", "3": "۲۵۰۰-۳۳۰۰"}},
        {"min": 7500, "max": 8000, "ranks": {"1": "۵۰۰۰-۶۴۰۰", "2": "۲۹۰۰-۳۶۰۰", "3": "۱۳۵۰-۱۸۰۰"}},
        {"min": 8000, "max": 8300, "ranks": {"1": "۳۱۰۰-۳۸۰۰", "2": "۲۴۰۰-۲۹۰۰", "3": "۶۳۰-۸۵۰"}},
        {"min": 8300, "max": 8700, "ranks": {"1": "۲۶۵۰-۳۳۳۰", "2": "۱۵۸۰-۲۲۳۰", "3": "۴۴۰-۶۳۰"}},
        {"min": 8700, "max": 9000, "ranks": {"1": "۱۷۵۰-۲۳۵۰", "2": "۹۵۰-۱۴۰۰", "3": "۱۶۰-۳۸۰"}},
        {"min": 9000, "max": 9300, "ranks": {"1": "۱۳۲۰-۱۷۵۰", "2": "۷۳۰-۱۰۵۰", "3": "۱۲۰-۱۶۰"}},
        {"min": 9300, "max": 9500, "ranks": {"1": "۱۴۰۰-۱۸۰۰", "2": "۷۵۰-۱۰۰۰", "3": "۱۲۰-۱۶۰"}},
        {"min": 9500, "max": 9800, "ranks": {"1": "۷۳۰-۱۰۲۰", "2": "۴۵۰-۶۹۰", "3": "۸۰-۱۳۰"}},
        {"min": 9800, "max": 10200, "ranks": {"1": "۴۴۰-۶۷۰", "2": "۱۹۰-۳۰۰", "3": "۸۰-۱۰۰"}},
        {"min": 10200, "max": 99999, "ranks": {"1": "زیر ۲۵۰", "2": "زیر ۱۵۰", "3": "زیر ۵۰"}},
    ],
}

GPA_TARAZ_DATA = [
    (15.00, 5310, 5770), (15.20, 5481, 5710), (15.40, 5692, 5891),
    (15.60, 5791, 6110), (15.80, 5892, 6110), (16.00, 6018, 6219),
    (16.20, 6190, 6430), (16.40, 6430, 6640), (16.60, 6640, 6891),
    (16.80, 6987, 7124), (17.00, 7110, 7378), (17.20, 7319, 7650),
    (17.40, 7539, 7810), (17.60, 7514, 7750), (17.80, 7750, 8120),
    (18.00, 8017, 8210), (18.20, 8110, 8340), (18.40, 8380, 8590),
    (18.60, 8491, 8753), (18.80, 8765, 8920), (19.00, 8869, 9205),
    (19.20, 9210, 9410), (19.40, 9310, 9620), (19.50, 9510, 9720),
    (19.60, 9730, 9920), (19.80, 10400, 10700), (20.00, 10800, 10800),
]

GPA_COEF = {
    "tajrobi": [
        {"id": "dini", "name": "تعلیمات دینی ۳", "coef": 8.47}, {"id": "arabi", "name": "عربی ۳", "coef": 4.64},
        {"id": "farsi", "name": "ادبیات فارسی ۳", "coef": 11.09}, {"id": "zaban", "name": "زبان خارجی ۳", "coef": 6.05},
        {"id": "shimi", "name": "شیمی ۳", "coef": 9.19}, {"id": "salamat", "name": "سلامت و بهداشت", "coef": 1.76},
        {"id": "ejtemaei", "name": "علوم اجتماعی", "coef": 1.31}, {"id": "zist", "name": "زیست‌شناسی ۳", "coef": 10.66},
        {"id": "riazi", "name": "ریاضی ۳", "coef": 10.04}, {"id": "physic", "name": "فیزیک ۳", "coef": 8.45},
    ],
    "riazi": [
        {"id": "dini", "name": "تعلیمات دینی ۳", "coef": 8.47}, {"id": "arabi", "name": "عربی ۳", "coef": 4.64},
        {"id": "farsi", "name": "ادبیات فارسی ۳", "coef": 11.09}, {"id": "zaban", "name": "زبان خارجی ۳", "coef": 6.05},
        {"id": "hendese", "name": "هندسه ۳", "coef": 5.49}, {"id": "hesaban", "name": "حسابان ۳", "coef": 8.17},
        {"id": "physic", "name": "فیزیک ۳", "coef": 9.26}, {"id": "shimi", "name": "شیمی ۳", "coef": 10.7},
        {"id": "gossaste", "name": "ریاضیات گسسته", "coef": 4.71}, {"id": "salamat", "name": "سلامت و بهداشت", "coef": 1.76},
        {"id": "ejtemaei", "name": "علوم اجتماعی", "coef": 1.31},
    ],
}

PCT_SUBJECTS = {
    "tajrobi": [{"id": "riazi", "name": "ریاضی"}, {"id": "zist", "name": "زیست‌شناسی"}, {"id": "zamin", "name": "زمین‌شناسی"}, {"id": "physic", "name": "فیزیک"}, {"id": "shimi", "name": "شیمی"}],
    "riazi": [{"id": "riaziat", "name": "ریاضیات"}, {"id": "shimi", "name": "شیمی"}, {"id": "physic", "name": "فیزیک"}],
    "ensani": [
        {"id": "riazi", "name": "ریاضی"}, {"id": "eghtesad", "name": "اقتصاد"},
        {"id": "farsi", "name": "زبان و ادبیات فارسی"}, {"id": "arabi", "name": "عربی"},
        {"id": "tarikh_joghrafi", "name": "تاریخ و جغرافیا"}, {"id": "ejtemaei", "name": "علوم اجتماعی"},
        {"id": "falsafe_mantegh", "name": "فلسفه و منطق"}, {"id": "ravanshenasi", "name": "روان‌شناسی"},
    ],
}

# داده‌برداری مستقیم از kanoon.ir/Public/EstimateSarasari، کنکور تیر ۱۴۰۳.
# در هر نقطه درصد تمام درس‌های تخصصی برابر بوده است. کلید جدول «شاخص عملکرد»
# نرمال‌شده با سهم ۶۰٪ معدل و ۴۰٪ درصد است. برای نقاط بین دو نمونه، نتیجه
# محافظه‌کارانه‌ی نزدیک‌ترین نقطه پایین‌تر برگردانده می‌شود.
KANOON_COMBINED_RANK_DATA = {
    "riazi": [
        {"percent": -33, "gpa": 8.0, "ranks": {"1": "۳۵۰۰۰-۳۸۰۰۰", "2": "۴۱۰۰۰-۴۴۰۰۰", "3": "۲۲۰۰۰-۲۹۰۰۰"}},
        {"percent": -20, "gpa": 9.2, "ranks": {"1": "۳۵۰۰۰-۳۸۰۰۰", "2": "۴۱۰۰۰-۴۴۰۰۰", "3": "۲۲۰۰۰-۲۹۰۰۰"}},
        {"percent": -10, "gpa": 10.1, "ranks": {"1": "۳۵۰۰۰-۳۸۰۰۰", "2": "۴۱۰۰۰-۴۴۰۰۰", "3": "۲۲۰۰۰-۲۹۰۰۰"}},
        {"percent": 0, "gpa": 11.0, "ranks": {"1": "۲۴۰۰۰-۲۵۰۰۰", "2": "۳۸۰۰۰-۴۱۰۰۰", "3": "۱۴۰۰۰-۱۵۰۰۰"}},
        {"percent": 5, "gpa": 11.4, "ranks": {"1": "۲۳۰۰۰-۲۴۰۰۰", "2": "۱۷۰۰۰-۱۸۰۰۰", "3": "۸۵۰۰-۹۰۰۰"}},
        {"percent": 10, "gpa": 11.9, "ranks": {"1": "۱۶۰۰۰-۱۷۰۰۰", "2": "۹۵۰۰-۱۰۰۰۰", "3": "۴۰۰۰-۵۰۰۰"}},
        {"percent": 15, "gpa": 12.3, "ranks": {"1": "۱۰۰۰۰-۱۱۰۰۰", "2": "۷۵۰۰-۸۰۰۰", "3": "۳۵۰۰-۴۰۰۰"}},
        {"percent": 20, "gpa": 12.8, "ranks": {"1": "۶۵۰۰-۷۰۰۰", "2": "۷۰۰۰-۷۵۰۰", "3": "۱۵۰۰-۲۰۰۰"}},
        {"percent": 25, "gpa": 13.2, "ranks": {"1": "۸۰۰۰-۸۵۰۰", "2": "۴۰۰۰-۴۵۰۰", "3": "۱۰۰۰-۱۵۰۰"}},
        {"percent": 30, "gpa": 13.7, "ranks": {"1": "۴۵۰۰-۵۰۰۰", "2": "۳۰۰۰-۳۵۰۰", "3": "۸۰۰-۱۰۰۰"}},
        {"percent": 35, "gpa": 14.1, "ranks": {"1": "۳۵۰۰-۴۰۰۰", "2": "۲۵۰۰-۳۰۰۰", "3": "۵۰۰-۶۰۰"}},
        {"percent": 40, "gpa": 14.6, "ranks": {"1": "۲۵۰۰-۳۰۰۰", "2": "۱۵۰۰-۲۰۰۰", "3": "۴۰۰-۵۰۰"}},
        {"percent": 45, "gpa": 15.0, "ranks": {"1": "۳۰۰۰-۳۵۰۰", "2": "۱۰۰۰-۱۵۰۰", "3": "۳۰۰-۴۰۰"}},
        {"percent": 50, "gpa": 15.5, "ranks": {"1": "۲۰۰۰-۲۵۰۰", "2": "۱۰۰۰-۱۵۰۰", "3": "۲۰۰-۳۰۰"}},
        {"percent": 55, "gpa": 15.9, "ranks": {"1": "۱۰۰۰-۱۵۰۰", "2": "۶۰۰-۸۰۰", "3": "۱۰۰-۲۰۰"}},
        {"percent": 60, "gpa": 16.4, "ranks": {"1": "۸۰۰-۱۰۰۰", "2": "۳۰۰-۴۰۰", "3": "۱۰۰-۲۰۰"}},
        {"percent": 65, "gpa": 16.8, "ranks": {"1": "۴۰۰-۵۰۰", "2": "۲۰۰-۳۰۰", "3": "۱-۱۰۰"}},
        {"percent": 70, "gpa": 17.3, "ranks": {"1": "۵۰۰-۶۰۰", "2": "۱۰۰-۲۰۰", "3": "۱-۱۰۰"}},
        {"percent": 75, "gpa": 17.7, "ranks": {"1": "۳۰۰-۴۰۰", "2": "۱۰۰-۲۰۰", "3": "۱-۱۰۰"}},
        {"percent": 80, "gpa": 18.2, "ranks": {"1": "۱۰۰-۲۰۰", "2": "۱-۱۰۰", "3": "۱-۱۰۰"}},
        {"percent": 85, "gpa": 18.6, "ranks": {"1": "۱۰۰-۲۰۰", "2": "۱-۱۰۰", "3": "۱-۱۰۰"}},
        {"percent": 90, "gpa": 19.1, "ranks": {"1": "۱۰۰-۲۰۰", "2": "۱-۱۰۰", "3": "۱-۱۰۰"}},
        {"percent": 95, "gpa": 19.5, "ranks": {"1": "۱-۱۰۰", "2": "۱-۱۰۰", "3": "۱-۱۰۰"}},
        {"percent": 100, "gpa": 20.0, "ranks": {"1": "۱-۱۰۰", "2": "۱-۱۰۰", "3": "۱-۱۰۰"}},
    ],
}


def estimate_kanoon_rank(field: str, region: str, gpa: float, avg_percent: float) -> tuple[str, float] | None:
    """تخمین مستقیم رتبه از جدول کانون برای معدل ۸..۲۰ و درصد ۳۳-..۱۰۰."""
    field = field.lower().strip()
    region = str(region).strip()
    data = KANOON_COMBINED_RANK_DATA.get(field)
    if data is None or region not in {"1", "2", "3"}:
        return None
    if not 8 <= gpa <= 20 or not -33 <= avg_percent <= 100:
        return None

    percent_part = (avg_percent + 33) / 133
    gpa_part = (gpa - 8) / 12
    performance_index = round(100 * (0.4 * percent_part + 0.6 * gpa_part), 2)
    selected = data[0]["ranks"]
    for point in data:
        point_percent = (point["percent"] + 33) / 133
        point_gpa = (point["gpa"] - 8) / 12
        threshold = round(100 * (0.4 * point_percent + 0.6 * point_gpa), 2)
        if performance_index + 1e-9 < threshold:
            break
        selected = point["ranks"]
    return selected[region], performance_index

# داده‌برداری از تخمین رتبه ماز برای کنکور ۱۴۰۴ (biomaze.ir/rank-estimate).
# در هر ردیف درصد همه دروس تخصصی برابر مقدار ستون اول بوده و مقدار تراز،
# میانگین ابتدا و انتهای بازه «تراز تخمینی آزمون اختصاصی» ماز است.
PERCENT_TARAZ_DATA_1404 = {
    "tajrobi": [
        (0, 3712), (5, 4855), (10, 5773), (15, 6512), (20, 7113),
        (25, 7615), (30, 8048), (35, 8442), (40, 8818), (45, 9197),
        (50, 9591), (55, 10011), (60, 10459), (65, 10936), (70, 11438),
        (75, 11953), (80, 12470), (85, 12967), (90, 13422), (95, 13807),
        (100, 14087),
    ],
    "riazi": [
        (0, 4489), (5, 5477), (10, 6328), (15, 7056), (20, 7675),
        (25, 8202), (30, 8650), (35, 9035), (40, 9371), (45, 9674),
        (50, 9958), (55, 10239), (60, 10531), (65, 10850), (70, 11209),
        (75, 11625), (80, 12112), (85, 12685), (90, 13358), (95, 14148),
        (100, 14200),
    ],
}

EXAM_RANGES = {
    "maz": {"name": "ماز", "min": 7000, "max": 13000, "levels": [(12000, 13001, "عالی 🔥 (رتبه زیر ۵۰۰ محتمل)"), (11000, 12000, "خیلی خوب ⭐ (رتبه حدود ۵۰۰–۱۵۰۰)"), (10000, 11000, "خوب (رتبه حدود ۱۵۰۰–۴۰۰۰)"), (9000, 10000, "متوسط رو به بالا"), (8000, 9000, "متوسط"), (7000, 8000, "ضعیف رو به متوسط")]},
    "ghalamchi": {"name": "قلمچی", "min": 4000, "max": 8500, "levels": [(7800, 8501, "عالی 🔥"), (7200, 7800, "خیلی خوب ⭐"), (6500, 7200, "خوب"), (5800, 6500, "متوسط رو به بالا"), (5000, 5800, "متوسط"), (4000, 5000, "ضعیف")]},
    "gozine2": {"name": "گزینه دو", "min": 5000, "max": 14000, "levels": [(12000, 14001, "عالی 🔥"), (11000, 12000, "خیلی خوب ⭐"), (10000, 11000, "خوب"), (9000, 10000, "متوسط رو به بالا"), (7500, 9000, "متوسط"), (5000, 7500, "ضعیف رو به متوسط")]},
}


def find_rank(field: str, region: str, score: float) -> str | None:
    for item in RANK_DATA.get(field.lower().strip(), []):
        if item["min"] <= score < item["max"]:
            return item["ranks"].get(str(region).strip())
    return None


def gpa_to_taraz_range(gpa: float, field: str | None = None) -> tuple[int, int] | None:
    """بازه تراز معدل مشترک برای تجربی، ریاضی و انسانی."""
    if field is not None and field not in {"tajrobi", "riazi", "ensani"}:
        return None
    if not 15 <= gpa <= 20:
        return None
    for i, (g1, low1, high1) in enumerate(GPA_TARAZ_DATA):
        if abs(gpa - g1) < 1e-9:
            return low1, high1
        if i + 1 < len(GPA_TARAZ_DATA):
            g2, low2, high2 = GPA_TARAZ_DATA[i + 1]
            if g1 < gpa < g2:
                ratio = (gpa - g1) / (g2 - g1)
                return round(low1 + ratio * (low2 - low1)), round(high1 + ratio * (high2 - high1))
    return None


def gpa_to_taraz(gpa: float, field: str | None = None) -> int | None:
    result = gpa_to_taraz_range(gpa, field)
    return round(sum(result) / 2) if result else None


def percent_to_taraz(avg_percent: float, field: str = "tajrobi") -> int | None:
    """تبدیل میانگین درصد به تراز کنکور ۱۴۰۴ با درون‌یابی داده‌های ماز."""
    data = PERCENT_TARAZ_DATA_1404.get(field)
    if data is None or not 0 <= avg_percent <= 100:
        return None

    for i, (percent1, taraz1) in enumerate(data):
        if abs(avg_percent - percent1) < 1e-9:
            return taraz1
        if i + 1 < len(data):
            percent2, taraz2 = data[i + 1]
            if percent1 < avg_percent < percent2:
                ratio = (avg_percent - percent1) / (percent2 - percent1)
                return round(taraz1 + ratio * (taraz2 - taraz1))
    return None


def calc_weighted_gpa(scores: dict, field: str) -> float | None:
    total = coef_sum = 0.0
    for item in GPA_COEF.get(field, []):
        val = scores.get(item["id"])
        if val is not None and 10 <= val <= 20:
            total += val * item["coef"]
            coef_sum += item["coef"]
    return total / coef_sum if coef_sum else None


def get_status(rank_str: str) -> str:
    if not rank_str:
        return "—"
    if "زیر" in rank_str:
        return "عالی 🔥"
    nums = []
    for part in rank_str.replace("–", "-").split("-"):
        digits = "".join(c for c in part if c.isdigit())
        if digits:
            nums.append(int(digits))
    if not nums:
        return "—"
    avg = sum(nums) / len(nums)
    return "عالی 🔥" if avg < 500 else "خیلی خوب ⭐" if avg < 1500 else "خوب" if avg < 5000 else "متوسط" if avg < 15000 else "نیاز به تلاش"


def format_rank_result(field: str, region: str, score: float, rank: str | None) -> str:
    field_name = {"tajrobi": "تجربی", "riazi": "ریاضی", "ensani": "انسانی"}.get(field, field)
    return f"🎉 *نتیجه تخمین رتبه*\n\n━━━━━━━━━━━━━━━━━━━━\n\n🎓 رشته: *{field_name}*\n📍 منطقه: *{region}*\n📊 تراز: *{score}*\n\n━━━━━━━━━━━━━━━━━━━━\n\n🏆 تخمین رتبه:\n*{rank or 'خارج از بازه تعریف‌شده'}*\n\n📈 وضعیت: *{get_status(rank) if rank else '—'}*\n\n━━━━━━━━━━━━━━━━━━━━\n\n💡 این تخمین تقریبی است و ممکن است با نتیجه نهایی اختلاف داشته باشد."


def evaluate_exam_taraz(exam_type: str, taraz: float) -> str:
    data = EXAM_RANGES.get(exam_type)
    if not data:
        return "❌ نوع آزمون نامعتبر است."
    if taraz < data["min"] or taraz > data["max"]:
        return f"⚠️ تراز وارد شده خارج از بازه معمول {data['name']} است.\nبازه تقریبی: {data['min']} تا {data['max']}"
    level = next((desc for low, high, desc in data["levels"] if low <= taraz < high), "نیاز به تلاش بیشتر")
    return f"📝 *نتیجه تحلیل تراز {data['name']}*\n\n━━━━━━━━━━━━━━━━━━━━\n\n📊 تراز شما: *{taraz}*\n\n📈 سطح تقریبی:\n*{level}*\n\n━━━━━━━━━━━━━━━━━━━━\n\n💡 این تحلیل تقریبی است و بستگی به جامعه آماری همان آزمون دارد."
