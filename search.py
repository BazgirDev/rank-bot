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


def percent_to_taraz(avg_percent: float) -> int:
    return min(10700, round(5000 + (avg_percent / 100) * 5700))


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
