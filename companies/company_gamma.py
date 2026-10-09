# شركة Gamma التابعة لإمبراطورية F-92
class GammaCorporation:
    def __init__(self):
        self.name = "Gamma Security"
        self.sector = "Cybersecurity & Defense"
        self.status = "Active & Secured"

    def get_info(self):
        return {
            "company": self.name,
            "sector": self.sector,
            "status": self.status
        }
