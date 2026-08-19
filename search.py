"""داده‌ها و توابع محاسباتی ربات آکادمی الف."""

RANK_DATA = {
    "tajrobi": [
        {"min": 0, "max": 5000, "ranks": {"1": "بالاتر از ۴۰۰۰۰", "2": "بالاتر از ۴۰۰۰۰", "3": "بالاتر از ۴۰۰۰۰"}},
        {"min": 5000, "max": 5500, "ranks": {"1": "۴۲۰۰۰-۴۴۰۰۰", "2": "۳۸۰۰۰-۴۰۰۰۰", "3": "۳۵۰۰۰-۳۷۰۰۰"}},
        {"min": 5500, "max": 6000, "ranks": {"1": "۴۰۰۰۰-۴۲۰۰۰", "2": "۳۸۰۰۰-۴۰۰۰۰", "3": "۳۳۰۰۰-۳۵۰۰۰"}},
        {"min": 6000, "max": 6500, "ranks": {"1": "25000-31000", "2": "50000-55000", "3": "25000-34000"}},
        {"min": 6500, "max": 6900, "ranks": {"1": "20000-25000", "2": "40000-47000", "3": "23000-30000"}},
        {"min": 6900, "max": 7600, "ranks": {"1": "14000-19000", "2": "۳۲۰۰۰-۳۷۰۰۰", "3": "15000-19000"}},
        {"min": 7600, "max": 8000, "ranks": {"1": "۱۰۸۰۰-۱۳۰۰۰", "2": "۱۵۰۰۰-۲۰۰۰۰", "3": "13300-14700"}},
        {"min": 8000, "max": 8300, "ranks": {"1": "۸۸۰۰-۱۰۵۰۰", "2": "۱۲۰۰۰-۱۵۰۰۰", "3": "۹۰۰۰-۱۱۵۰۰"}},
        {"min": 8300, "max": 8700, "ranks": {"1": "۷۴۵۰-۹۰۵۰", "2": "۱۱۵۰۰-۱۳۷۰۰", "3": "۷۳۵۰-۹۲۰۰"}},
        {"min": 8700, "max": 9000, "ranks": {"1": "۳۹۰۰-۵۱۰۰", "2": "۵۳۰۰-۷۳۰۰", "3": "۳۱۵۰-۴۳۰۰"}},
        {"min": 9000, "max": 9300, "ranks": {"1": "۳۱۲۰-۴۰۰۰", "2": "۳۳۰۰-۴۸۰۰", "3": "2200-3000"}},
        {"min": 9300, "max": 9500, "ranks": {"1": "۱۴۸۰-۲۲۰۰", "2": "۲۳۲۰-۳۱۸۰", "3": "820-1750"}},
        {"min": 9500, "max": 9800, "ranks": {"1": "۶۳۰-۹۸۰", "2": "۱۳۷۵-۲۰۷۰", "3": "۶۶۰-۱۱۸۰"}},
        {"min": 9800, "max": 10100, "ranks": {"1": "۶۱۰-۹۸۰", "2": "۵۲۰-۸۴۰", "3": "۳۰۰-۶۵۰"}},
        {"min": 10100, "max": 10400, "ranks": {"1": "۲۱۰-۵۸۰", "2": "۲۳۰-۴۸۰", "3": "۸۰-۲۸۰"}},
        {"min": 10400, "max": 99999, "ranks": {"1": "زیر ۲۰۰", "2": "زیر ۲۰۰", "3": "زیر ۷۰"}},
    ],
    "riazi": [
        {"min": 0, "max": 5000, "ranks": {"1": "25000-30000", "2": "20000-27000", "3": "5800-7000"}},
        {"min": 5000, "max": 5500, "ranks": {"1": "20000-25000", "2": "20000-25000", "3": "4700-5800"}},
        {"min": 5500, "max": 6000, "ranks": {"1": "۱۵۰۰۰-۲۰۰۰۰", "2": "12800-15400", "3": "4300-5000"}},
        {"min": 6000, "max": 6500, "ranks": {"1": "9000-10000", "2": "9000-10000", "3": "3000-4000"}},
        {"min": 6500, "max": 7000, "ranks": {"1": "۹۰۰۰-۱۲۰۰۰", "2": "6700-8100 ", "3": "2400-3200"}},
        {"min": 7000, "max": 7500, "ranks": {"1": "7700-8600", "2": "۵۴۰۰-۶۸۰۰", "3": "2000-2800"}},
        {"min": 7500, "max": 8000, "ranks": {"1": "5900-7200", "2": "۲۹۰۰-۳۶۰۰", "3": "۱۳۵۰-۱۸۰۰"}},
        {"min": 8000, "max": 8300, "ranks": {"1": "5100-6000", "2": "۲۴۰۰-۲۹۰۰", "3": "630-1050"}},
        {"min": 8300, "max": 8700, "ranks": {"1": "۲۶۵۰-۳۳۳۰", "2": "۱۵۸۰-۲۲۳۰", "3": "۴۴۰-۶۳۰"}},
        {"min": 8700, "max": 9000, "ranks": {"1": "۱۷۵۰-۲۳۵۰", "2": "۹۵۰-۱۴۰۰", "3": "۱۶۰-۳۸۰"}},
        {"min": 9000, "max": 9300, "ranks": {"1": "۱۳۲۰-۱۷۵۰ ", "2": "۷۳۰-۱۰۵۰", "3": "۱۲۰-۱۶۰"}},
        {"min": 9300, "max": 9500, "ranks": {"1": "۱۴۰۰-۱۸۰۰", "2": "۷۵۰-۱۰۰۰", "3": "۱۲۰-۱۶۰"}},
        {"min": 9500, "max": 9800, "ranks": {"1": "۷۳۰-۱۰۲۰", "2": "۴۵۰-۶۹۰", "3": "۸۰-۱۳۰"}},
        {"min": 9800, "max": 10200, "ranks": {"1": "۴۴۰-۶۷۰", "2": "۱۹۰-۳۰۰", "3": "۸۰-۱۰۰"}},
        {"min": 10200, "max": 99999, "ranks": {"1": "زیر ۲۵۰", "2": "زیر ۱۵۰", "3": "زیر ۵۰"}},
    ],
}

GPA_TARAZ_DATA = [
    (15.00, 6121, 6421), (15.20, 6221, 6359), (15.40, 6359, 6412),
    (15.60, 6412, 6582), (15.80, 6582, 6791), (16.00, 6791, 7021),
    (16.20, 6480, 6760), (16.40, 6580, 6840), (16.60, 6640, 6991),
    (16.80, 6887, 7394), (17.00, 7110, 7510), (17.20, 7319, 7750),
    (17.40, 7489, 7710), (17.60, 7514, 7880), (17.80, 7750, 8120),
    (18.00, 8017, 8290), (18.20, 8110, 8340), (18.40, 8380, 8590),
    (18.60, 8491, 8753), (18.80, 8765, 8920), (19.00, 8869, 9205),
    (19.20, 9210, 9410), (19.40, 9310, 9620), (19.50, 9510, 9720),
    (19.60, 9730, 9920), (19.80, 10400, 10700), (20.00, 10800, 10800),
]

GPA_TARAZ_BANDS = [
    (10.0, 11.0, 4321, 4782),
    (11.0, 12.0, 4782, 5198),
    (12.0, 12.5, 5198, 5431),
    (12.5, 13.2, 5431, 5571),
    (13.2, 13.8, 5571, 5631),
    (13.8, 14.2, 5631, 5710),
    (14.2, 14.7, 5810, 5921),
    (14.7, 15.0, 5971, 6321),
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
    "tajrobi": [
        {"id": "riazi", "name": "ریاضی", "coef": 7},
        {"id": "zist", "name": "زیست‌شناسی", "coef": 12},
        {"id": "zamin", "name": "زمین‌شناسی", "coef": 1},
        {"id": "physic", "name": "فیزیک", "coef": 7},
        {"id": "shimi", "name": "شیمی", "coef": 9},
    ],
    "riazi": [
        {"id": "riaziat", "name": "ریاضیات", "coef": 12},
        {"id": "shimi", "name": "شیمی", "coef": 6},
        {"id": "physic", "name": "فیزیک", "coef": 9},
    ],
    "ensani": [
        {"id": "riazi", "name": "ریاضی"}, {"id": "eghtesad", "name": "اقتصاد"},
        {"id": "farsi", "name": "زبان و ادبیات فارسی"}, {"id": "arabi", "name": "عربی"},
        {"id": "tarikh_joghrafi", "name": "تاریخ و جغرافیا"}, {"id": "ejtemaei", "name": "علوم اجتماعی"},
        {"id": "falsafe_mantegh", "name": "فلسفه و منطق"}, {"id": "ravanshenasi", "name": "روان‌شناسی"},
    ],
}

PERCENT_TARAZ_DATA_1404 = {
    "tajrobi": [
        (0, 3712), (5, 5721), (10, 6411), (15, 7210), (20, 7513),
        (25, 7983), (30, 8380), (35, 8740), (40, 9021), (45, 9397),
        (50, 9700), (55, 10311), (60, 10699), (65, 11192), (70, 11588),
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
    if not 10 <= gpa <= 20:
        return None
    if gpa < 15:
        for low_gpa, high_gpa, low_taraz, high_taraz in GPA_TARAZ_BANDS:
            if low_gpa <= gpa < high_gpa:
                return low_taraz, high_taraz
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
    """تبدیل میانگین درصد به تراز با داده مرجع و درون‌یابی خطی."""
    data = PERCENT_TARAZ_DATA_1404.get(field)
    if data is None or not -33 <= avg_percent <= 100:
        return None
    if avg_percent < 0:
        return 3500

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


def calc_weighted_percent(scores: dict, field: str) -> float | None:
    """محاسبه میانگین وزنی درصدهای کنکور با ضرایب اختصاصی هر رشته."""
    subjects = PCT_SUBJECTS.get(field, [])
    if not subjects:
        return None

    total = coef_sum = 0.0
    for subject in subjects:
        value = scores.get(subject["id"])
        if value is None or not -33 <= value <= 100:
            return None
        coef = subject.get("coef")
        if coef is None:
            return None
        total += value * coef
        coef_sum += coef

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
