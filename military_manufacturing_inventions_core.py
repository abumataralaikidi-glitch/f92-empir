from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="F-92 Sovereign Empire - Military Manufacturing & Advanced Inventions Core")

# سجل أبحاث واختراعات الإمبراطورية الحربية داخل الذاكرة
INVENTIONS_REGISTRY: List[Dict[str, str]] = []

class MilitaryUpgradeRequest(BaseModel):
    domain: str  # fighter_jets, naval_ships, armored_vehicles, general_defense
    upgrade_objective: str

class NewInventionRecord(BaseModel):
    invention_name: str
    category: str
    specification: str
    inventor: str = "العراب - صلاح الدين سامي"

@app.get("/")
def home():
    return {
        "room": "Military Manufacturing & Advanced Inventions Chamber",
        "commander": "صلاح الدين سامي (العراب)",
        "status": "Active, Manufacturing & Innovating Sovereign Defense Tech",
        "doctrine": "التطوير الحربي الشامل للسفن، الطائرات، والمدرعات، مع توثيق الابتكارات في السجل المركزي."
    }

@app.post("/api/military/upgrade")
def upgrade_military_asset(request: MilitaryUpgradeRequest):
    domain = request.domain.lower()
    objective = request.upgrade_objective.lower()
    
    # محرك تطوير الأصول والمجالات الحربية
    if "jet" in domain or "air" in domain or "طائرة" in objective:
        result = "تطوير أنظمة الدفع النفاث، طلاء التخفي الراداري، وتجهيز أسراب الطائرات القتالية بتقنيات الجيل السادس."
    elif "ship" in domain or "naval" in domain or "سفن" in objective:
        result = "تعزيز دروع الهيكل البحري، دمج أنظمة التوجيه الذاتي، وتطوير البوارج الحربية لتعمل بالطاقة المتقدمة."
    elif "armor" in domain or "tank" in domain or "مدرعات" in objective:
        result = "ترقية التدريع التفاعلي المركب، تحسين نظم الحركة في التضاريس الوعرة، وربطها بغرفة القيادة المركزية."
    else:
        result = "تنفيذ ترقية عسكرية شاملة لكافة المنشآت والعتاد الحربي بأحدث معايير الردع السيادي."

    return {
        "status": "Military Asset Upgraded Successfully",
        "commander": "العراب",
        "target_domain": request.domain.upper(),
        "objective": request.upgrade_objective,
        "engineering_result": result,
        "classification": "Top Secret - Sovereign Military Grade"
    }

@app.post("/api/inventions/register")
def register_advanced_invention(invention: NewInventionRecord):
    record = {
        "invention_name": invention.invention_name,
        "category": invention.category,
        "specification": invention.specification,
        "inventor": invention.inventor,
        "status": "Secured and Logged in Sovereign Invention Library"
    }
    INVENTIONS_REGISTRY.append(record)
    return {
        "status": "Invention Registered Successfully",
        "commander": "العراب",
        "total_inventions_in_library": len(INVENTIONS_REGISTRY),
        "invention_details": record
    }

@app.get("/api/inventions/library")
def get_inventions_library():
    return {
        "commander": "العراب",
        "library_name": "مكتبة سجل الاختراعات الحربية والمتقدمة",
        "total_records": len(INVENTIONS_REGISTRY),
        "registered_inventions": INVENTIONS_REGISTRY
    }
