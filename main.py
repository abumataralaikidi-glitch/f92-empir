from fastapi import FastAPI
import os

# استدعاء الشركات الثلاثة بأمان تام
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

app = FastAPI(title="F-92 Sovereign Empire - Final Application")

@app.get("/")
def home():
    return {
        "empire": "F-92 Sovereign Empire",
        "status": "Online & Fully Operational",
        "commander": "العراب"
    }

@app.get("/api/empire/all-companies")
def get_all_companies():
    active_firms = []
    if AlphaCorporation:
        active_firms.append(AlphaCorporation().get_info())
    if BetaCorporation:
        active_firms.append(BetaCorporation().get_info())
    if GammaCorporation:
        active_firms.append(GammaCorporation().get_info())

    return {
        "empire_core": "Stable",
        "total_companies": len(active_firms),
        "companies": active_firms
    }
