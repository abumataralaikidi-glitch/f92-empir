# شركة Beta التابعة لإمبراطورية F-92
class BetaCorporation:
    def __init__(self):
        self.name = "Beta Logistics"
        self.sector = "Supply Chain & Operations"
        self.status = "Active & Secured"

    def get_info(self):
        return {
            "company": self.name,
            "sector": self.sector,
            "status": self.status
        }
