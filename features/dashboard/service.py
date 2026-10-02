from .repository import DashboardRepository


class DashboardService:

    def __init__(self, repository):
        self.repository = repository

    def getStats(self):
        return self.repository.getStats()