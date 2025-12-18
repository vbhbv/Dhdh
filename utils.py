import re

def clean_text(text: str) -> str:
    """تنظيف النصوص من رموز غير مرغوبة وفراغات زائدة."""
    text = re.sub(r'\s+', ' ', text)  # إزالة فراغات زائدة
    text = re.sub(r'[^\w\sء-ي]', '', text)  # إزالة الرموز غير الحروف والأرقام
    return text.strip()

def split_text(text: str, chunk_size: int = 1000):
    """تقسيم النص الطويل إلى قطع صغيرة لتجنب مشاكل التلخيص."""
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])
