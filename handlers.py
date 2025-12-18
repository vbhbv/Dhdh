import os
from telegram import Update
from telegram.ext import ContextTypes
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_text
from config import SUMMARY_RATIO, MAX_MESSAGE_LENGTH, DOWNLOAD_FOLDER

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا! أرسل لي ملف PDF لألخصه لك.")

async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await context.bot.get_file(update.message.document.file_id)
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(DOWNLOAD_FOLDER, update.message.document.file_name)
    await file.download_to_drive(file_path)

    await update.message.reply_text("جارٍ استخراج النص من الملف...")

    text = extract_text_from_pdf(file_path)

    if not text.strip():
        await update.message.reply_text("عذراً، لم أتمكن من استخراج نص من الملف.")
        return

    await update.message.reply_text("جارٍ تلخيص الملف...")

    # تلخيص النص
    from utils import split_text
    summary = ""
    for chunk in split_text(text, chunk_size=1500):
        summary += summarize_text(chunk, ratio=SUMMARY_RATIO) + "\n\n"

    # إرسال الملخص
    if len(summary) > MAX_MESSAGE_LENGTH:
        # حفظه في ملف TXT إذا كان طويلاً جداً
        summary_file = file_path.replace(".pdf", "_summary.txt")
        with open(summary_file, "w", encoding="utf-8") as f:
            f.write(summary)
        await update.message.reply_document(open(summary_file, "rb"))
    else:
        await update.message.reply_text(summary)
