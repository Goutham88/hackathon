from data_accessor import DataAccessor
from entities.hackathon_entity import HackathonEntity


class LeaderBoardHandler:
    def __init__(self):
        self.dao = DataAccessor()
        self.hackathon_entity_object = HackathonEntity()

    def get_leaderboard(self, hackathon_id):
        self.hackathon_entity_object.hackathon_id = hackathon_id
        return self.dao.get_sorted_scores(self.hackathon_entity_object)
