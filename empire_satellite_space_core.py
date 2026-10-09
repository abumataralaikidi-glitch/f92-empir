from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="F-92 Sovereign Empire - Satellite & Deep Space Operations Core")

# سجل الأقمار الصناعية والمهام الفضائية النشطة
SATELLITE_REGISTRY: List[Dict[str, str]] = []

class SatelliteLaunchRequest(BaseModel):
    satellite_name: str
    orbit_type: str  # leo, geo, deep_space
    primary_mission: str  # telemetry, global_surveillance, quantum_communication

@app.get("/")
def home():
    return {
        "room": "Sovereign Satellite & Deep Space Operations Chamber",
        "commander": "صلاح الدين سامي (العراب)",
        "status": "Online, Orbiting & Monitoring Global Telemetry",
        "doctrine": "السيادة المطلقة في المدارات الفضائية وتأمين شبكة الاتصالات الكونية."
    }

@app.post("/api/space/launch-satellite")
def launch_sovereign_satellite(request: SatelliteLaunchRequest):
    sat_name = request.satellite_name
    orbit = request.orbit_type.lower()
    mission = request.primary_mission.lower()
    
    # محرك إدارة وإطلاق الأقمار الصناعية السيادية
    status_detail = f"تم إطلاق القمر الصناعي [{sat_name}] بنجاح واستقرار في مدار [{orbit.upper()}]."
    
    if "quantum" in mission or "communication" in mission:
        telemetry_result = "تفعيل رابط الاتصالات الكمومية المشفرة وتأمين نقل البيانات الفضائية."
    elif "surveillance" in mission or "global" in mission:
        telemetry_result = "تنشيط مسح الرادار الفضائي المتقدم ومراقبة الدرع السيادي للإمبراطورية من المدار."
    else:
        telemetry_result = "استقرار أنظمة التوجيه الذاتي وبدء بث البيانات إلى غرفة العمليات المركزية."

    record = {
        "satellite_name": sat_name,
        "orbit": orbit.upper(),
        "mission": mission,
        "telemetry_status": telemetry_result,
        "operator": "العراب"
    }
    SATELLITE_REGISTRY.append(record)

    return {
        "status": "Satellite Deployed & Operational",
        "commander": "العراب",
        "total_active_satellites": len(SATELLITE_REGISTRY),
        "deployment_details": record
    }

@app.get("/api/space/fleet-status")
def get_space_fleet_status():
    return {
        "commander": "العراب",
        "network_name": "شبكة الرصد الفضائي للإمبراطورية السيادية - F-92",
        "total_satellites": len(SATELLITE_REGISTRY),
        "fleet_registry": SATELLITE_REGISTRY,
        "security_lock": "Encrypted Sovereign Frequency - 100% Secured"
    }
