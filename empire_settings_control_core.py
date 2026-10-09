from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="F-92 Sovereign Empire - Central Settings & Configuration Core")

# حالة إعدادات الإمبراطورية الافتراضية السيادية
EMPIRE_SETTINGS_STATE: Dict[str, Any] = {
    "commander": "صلاح الدين سامي (العراب)",
    "security_level": "Maximum Sovereign Lock",
    "voice_module_active": True,
    "cyber_retaliation_grid": "Armed & Automated",
    "exclusive_local_mode": True,
    "global_corporate_nexus": "Standby",
    "satellite_link": "Encrypted & Orbiting",
    "theme": "Sovereign Dark Obsidian"
}

class SettingUpdateRequest(BaseModel):
    master_key: str
    setting_name: str
    new_value: Any

@app.get("/")
def home():
    return {
        "room": "Central Settings & Configuration Chamber",
        "commander": EMPIRE_SETTINGS_STATE["commander"],
        "status": "Online, Fully Operational",
        "doctrine": "التحكم المطلق في كافة إعدادات ومعايير الإمبراطورية السيادية."
    }

@app.get("/api/settings/get-all")
def get_all_empire_settings():
    return {
        "status": "Success",
        "commander": EMPIRE_SETTINGS_STATE["commander"],
        "current_settings": EMPIRE_SETTINGS_STATE
    }

@app.post("/api/settings/update")
def update_empire_setting(request: SettingUpdateRequest):
    # التحقق من مفتاح العراب لتغيير الإعدادات السيادية
    if request.master_key != "F92-EXCLUSIVE-LOCAL-2026":
        raise HTTPException(
            status_code=403,
            detail="Access Denied: تعديل إعدادات الإمبراطورية مخصص حصرياً للعراب (صلاح الدين سامي)."
        )
    
    setting = request.setting_name
    if setting in EMPIRE_SETTINGS_STATE:
        EMPIRE_SETTINGS_STATE[setting] = request.new_value
        return {
            "status": "Setting Updated Successfully",
            "commander": EMPIRE_SETTINGS_STATE["commander"],
            "updated_setting": setting,
            "new_value": request.new_value,
            "current_state": EMPIRE_SETTINGS_STATE
        }
    else:
        raise HTTPException(
            status_code=404,
            detail=f"الإعداد [{setting}] غير موجود في سجلات الإمبراطورية."
        )
