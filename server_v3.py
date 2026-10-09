from fastapi import FastAPI
import os

# استدعاء الشركات الداخلية بأمان تام
try:
    from companies.company_alpha import AlphaCorporation
except ImportError:
    AlphaCorporation = None

try:
    from companies.company_beta import BetaCorporation
except ImportError:
    BetaCorporation = None

try:
    from companies.company_gamma import GammaCorporation
except ImportError:
    GammaCorporation = None

app = FastAPI(title="F-92 Sovereign Empire - Server V3")

@app.get("/")
def home():
    return {"message": "إمبراطورية F-92 - السيرفر المطور V3 يعمل بكفاءة وأمان تام"}

@app.get("/api/v3/empire/status")
def empire_status():
    companies = []
    if AlphaCorporation:
        companies.append(AlphaCorporation().get_info())
    if BetaCorporation:
        companies.append(BetaCorporation().get_info())
    if GammaCorporation:
        companies.append(GammaCorporation().get_info())

    return {
        "empire": "F-92 Sovereign Empire",
        "version": "V3 Consolidated",
        "commander": "العراب",
        "status": "All Systems Secured",
        "active_companies": companies
    }
