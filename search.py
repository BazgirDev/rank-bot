# ==================== DATA ====================
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
    ]
}

# ضرایب دروس نهایی
GPA_COEF = {
    "tajrobi": [
        {"id": "dini", "name": "تعلیمات دینی ۳", "coef": 8.47},
        {"id": "arabi", "name": "عربی ۳", "coef": 4.64},
        {"id": "farsi", "name": "ادبیات فارسی ۳", "coef": 11.09},
        {"id": "zaban", "name": "زبان خارجی ۳", "coef": 6.05},
        {"id": "shimi", "name": "شیمی ۳", "coef": 9.19},
        {"id": "salamat", "name": "سلامت و بهداشت", "coef": 1.76},
        {"id": "ejtemaei", "name": "علوم اجتماعی", "coef": 1.31},
        {"id": "zist", "name": "زیست‌شناسی ۳", "coef": 10.66},
        {"id": "riazi", "name": "ریاضی ۳", "coef": 10.04},
        {"id": "physic", "name": "فیزیک ۳", "coef": 8.45},
    ],
    "riazi": [
        {"id": "dini", "name": "تعلیمات دینی ۳", "coef": 8.47},
        {"id": "arabi", "name": "عربی ۳", "coef": 4.64},
        {"id": "farsi", "name": "ادبیات فارسی ۳", "coef": 11.09},
        {"id": "zaban", "name": "زبان خارجی ۳", "coef": 6.05},
        {"id": "hendese", "name": "هندسه ۳", "coef": 5.49},
        {"id": "hesaban", "name": "حسابان ۳", "coef": 8.17},
        {"id": "physic", "name": "فیزیک ۳", "coef": 9.26},
        {"id": "shimi", "name": "شیمی ۳", "coef": 10.7},
        {"id": "gossaste", "name": "ریاضیات گسسته", "coef": 4.71},
        {"id": "salamat", "name": "سلامت و بهداشت", "coef": 1.76},
        {"id": "ejtemaei", "name": "علوم اجتماعی", "coef": 1.31},
    ]
}

# دروس درصد کنکور
PCT_SUBJECTS = {
    "tajrobi": [
        {"id": "riazi", "name": "ریاضی"},
        {"id": "zist", "name": "زیست‌شناسی"},
        {"id": "zamin", "name": "زمین‌شناسی"},
        {"id": "physic", "name": "فیزیک"},
        {"id": "shimi", "name": "شیمی"},
    ],
    "riazi": [
        {"id": "riaziat", "name": "ریاضیات"},
        {"id": "shimi", "name": "شیمی"},
        {"id": "physic", "name": "فیزیک"},
    ]
}

# آزمون‌های آزمایشی
EXAM_RANGES = {
    "maz": {
        "name": "ماز",
        "min": 7000,
        "max": 13000,
        "levels": [
            (12000, 13001, "عالی 🔥 (رتبه زیر ۵۰۰ محتمل)"),
            (11000, 12000, "خیلی خوب ⭐ (رتبه حدود ۵۰۰–۱۵۰۰)"),
            (10000, 11000, "خوب (رتبه حدود ۱۵۰۰–۴۰۰۰)"),
            (9000, 10000, "متوسط رو به بالا"),
            (8000, 9000, "متوسط"),
            (7000, 8000, "ضعیف رو به متوسط"),
        ]
    },
    "ghalamchi": {
        "name": "قلمچی",
        "min": 4000,
        "max": 8500,
        "levels": [
            (7800, 8501, "عالی 🔥"),
            (7200, 7800, "خیلی خوب ⭐"),
            (6500, 7200, "خوب"),
            (5800, 6500, "متوسط رو به بالا"),
            (5000, 5800, "متوسط"),
            (4000, 5000, "ضعیف"),
        ]
    },
    "gozine2": {
        "name": "گزینه دو",
        "min": 5000,
        "max": 14000,
        "levels": [
            (12000, 14001, "عالی 🔥"),
            (11000, 12000, "خیلی خوب ⭐"),
            (10000, 11000, "خوب"),
            (9000, 10000, "متوسط رو به بالا"),
            (7500, 9000, "متوسط"),
            (5000, 7500, "ضعیف رو به متوسط"),
        ]
    }
}


# ==================== FUNCTIONS ====================
def find_rank(field: str, region: str, score: float) -> str | None:
    field = field.lower().strip()
    region = str(region).strip()
    if field not in RANK_DATA:
        return None
    for item in RANK_DATA[field]:
        if item["min"] <= score < item["max"]:
            return item["ranks"].get(region)
    return None


def gpa_to_taraz(gpa: float) -> int:
    """معدل ۱۰ تا ۲۰ → تراز تقریبی ۵۵۰۰ تا ۱۰۷۰۰"""
    factor = max(0.0, min(1.0, (gpa - 10) / 10))
    return min(10700, round(5500 + factor * 5200))


def percent_to_taraz(avg_percent: float) -> int:
    """میانگین درصد ۰ تا ۱۰۰ → تراز تقریبی"""
    return min(10700, round(5000 + (avg_percent / 100) * 5700))


def calc_weighted_gpa(scores: dict, field: str) -> float | None:
    """scores: {id: score} — محاسبه معدل وزنی با ضرایب"""
    coefs = GPA_COEF.get(field, [])
    total = 0.0
    coef_sum = 0.0
    count = 0
    for item in coefs:
        val = scores.get(item["id"])
        if val is not None and 10 <= val <= 20:
            total += val * item["coef"]
            coef_sum += item["coef"]
            count += 1
    if count == 0 or coef_sum == 0:
        return None
    return total / coef_sum


def get_status(rank_str: str) -> str:
    if not rank_str:
        return "—"
    if "زیر" in rank_str:
        return "عالی 🔥"
    nums = []
    for part in rank_str.replace("–", "-").split("-"):
        part = "".join(c for c in part if c.isdigit())
        if part:
            nums.append(int(part))
    if not nums:
        return "—"
    avg = sum(nums) / len(nums)
    if avg < 500:
        return "عالی 🔥"
    if avg < 1500:
        return "خیلی خوب ⭐"
    if avg < 5000:
        return "خوب"
    if avg < 15000:
        return "متوسط"
    return "نیاز به تلاش"


def format_rank_result(field: str, region: str, score: float, rank: str | None) -> str:
    field_name = "تجربی" if field == "tajrobi" else "ریاضی"
    status = get_status(rank) if rank else "—"
    rank_text = rank if rank else "خارج از بازه تعریف‌شده"

    return (
        f"🎉 *نتیجه تخمین رتبه*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🎓 رشته: *{field_name}*\n"
        f"📍 منطقه: *{region}*\n"
        f"📊 تراز: *{score}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🏆 تخمین رتبه:\n*{rank_text}*\n\n"
        f"📈 وضعیت: *{status}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💡 این تخمین تقریبی است و ممکن است با نتیجه نهایی اختلاف داشته باشد."
    )


def evaluate_exam_taraz(exam_type: str, taraz: float) -> str:
    data = EXAM_RANGES.get(exam_type)
    if not data:
        return "❌ نوع آزمون نامعتبر است."

    if taraz < data["min"] or taraz > data["max"]:
        return (
            f"⚠️ تراز وارد شده خارج از بازه معمول {data['name']} است.\n"
            f"بازه تقریبی: {data['min']} تا {data['max']}"
        )

    level_text = "نیاز به تلاش بیشتر"
    for low, high, desc in data["levels"]:
        if low <= taraz < high:
            level_text = desc
            break

    return (
        f"📝 *نتیجه تحلیل تراز {data['name']}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"📊 تراز شما: *{taraz}*\n\n"
        f"📈 سطح تقریبی:\n*{level_text}*\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"💡 این تحلیل تقریبی است و بستگی به جامعه آماری همان آزمون دارد."
    )
