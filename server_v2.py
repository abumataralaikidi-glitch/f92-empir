from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os

# استدعاء الشركات الداخلية بشكل آمن ومستقل
try:
    from companies.company_alpha import AlphaCorporation
except ImportError:
    AlphaCorporation = None

app = FastAPI(title="F-92 Sovereign Empire - Server V2")

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h3>إمبراطورية F-92 - السيرفر المطور (V2) يعمل بكفاءة وأمان تام</h3>"

@app.get("/api/v2/status")
def v2_status():
    alpha_status = AlphaCorporation().get_info() if AlphaCorporation else "Offline"
    return {
        "empire": "F-92 Sovereign Empire",
        "version": "V2 Independent",
        "commander": "العراب",
        "registered_companies": [alpha_status]
    }
