from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="F-92 Sovereign Empire - Archive, Logging & Live Chat Core")

# قاعدة بيانات مؤقتة داخل الذاكرة للأرشيف والرسائل (للحفاظ على استقلالية وسلامة النظام)
ARCHIVE_STORAGE: List[Dict[str, str]] = []
CHAT_MESSAGES: List[Dict[str, str]] = []

class ArchiveRecord(BaseModel):
    category: str
    content: str
    author: str = "العراب"

class ChatMessage(BaseModel):
    sender: str
    message: str
    target_channel: str = "General-Empire-Grid"

@app.get("/")
def home():
    return {
        "engine": "Empire Archive & Sovereign Chat Grid",
        "commander": "صلاح الدين سامي (العراب)",
        "status": "Online, Recording & Synchronizing Live Chat",
        "doctrine": "حفظ موثق لكافة البيانات وربط حي وآمن بين كافة الأطراف والشركات."
    }

@app.post("/api/archive/save")
def save_to_archive(record: ArchiveRecord):
    entry = {
        "category": record.category,
        "content": record.content,
        "author": record.author,
        "status": "Saved and Secured in Sovereign Archive"
    }
    ARCHIVE_STORAGE.append(entry)
    return {
        "status": "Success",
        "message": "تم حفظ وتوثيق البيان في مكتبة الإمبراطورية بنجاح.",
        "total_archived_items": len(ARCHIVE_STORAGE),
        "record": entry
    }

@app.get("/api/archive/list")
def get_archive():
    return {
        "commander": "العراب",
        "total_records": len(ARCHIVE_STORAGE),
        "archive_entries": ARCHIVE_STORAGE
    }

@app.post("/api/chat/send")
def send_chat_message(chat: ChatMessage):
    msg_entry = {
        "sender": chat.sender,
        "message": chat.message,
        "channel": chat.target_channel
    }
    CHAT_MESSAGES.append(msg_entry)
    return {
        "status": "Message Broadcasted",
        "chat_grid": "Active",
        "broadcast_to": chat.target_channel,
        "total_messages": len(CHAT_MESSAGES),
        "latest_transmission": msg_entry
    }

@app.get("/api/chat/history")
def get_chat_history():
    return {
        "commander": "العراب",
        "channel": "General-Empire-Grid",
        "messages": CHAT_MESSAGES
    }
