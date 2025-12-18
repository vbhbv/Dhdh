from gensim.summarization import summarize

def summarize_text(text: str, ratio: float = 0.05) -> str:
    """تلخيص النص باستخدام gensim."""
    try:
        summary = summarize(text, ratio=ratio)
        if not summary:
            return "النص قصير جداً، لا حاجة للتلخيص."
        return summary
    except Exception:
        return "حدث خطأ أثناء التلخيص. النص قد يكون قصير جداً."
