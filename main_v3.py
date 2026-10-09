from fastapi import FastAPI
import os

# استدعاء جميع شركات إمبراطورية F-92 في النسخة الجديدة الآمنة V3
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

try:
    from companies.company_delta import DeltaAIOrchestrator
except ImportError:
    DeltaAIOrchestrator = None

try:
    from companies.company_epsilon import EpsilonProcessingCore
except ImportError:
    EpsilonProcessingCore = None

try:
    from companies.company_zeta import ZetaCyberDefense
except ImportError:
    ZetaCyberDefense = None

app = FastAPI(title="F-92 Sovereign Empire - Main V3 Ultimate Application")

@app.get("/")
def home():
    return {
        "empire": "F-92 Sovereign Empire",
        "status": "Main V3 Ultimate Application Fully Operational",
        "commander": "العراب"
    }

@app.get("/api/v3/empire/all-sectors")
def get_all_sectors_v3():
    all_firms = []
    if AlphaCorporation:
        all_firms.append(AlphaCorporation().get_info())
    if BetaCorporation:
        all_firms.append(BetaCorporation().get_info())
    if GammaCorporation:
        all_firms.append(GammaCorporation().get_info())
    if DeltaAIOrchestrator:
        all_firms.append(DeltaAIOrchestrator().get_info())
    if EpsilonProcessingCore:
        all_firms.append(EpsilonProcessingCore().get_info())
    if ZetaCyberDefense:
        all_firms.append(ZetaCyberDefense().get_info())
        
    return {
        "empire_core": "Stable & Independent V3",
        "total_active_sectors": len(all_firms),
        "companies": all_firms
    }
