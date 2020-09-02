from data_accessor import DataAccessor
from entities.hackathon_entity import HackathonEntity


class LeaderBoardHandler:
    def __init__(self):
        self.dao = DataAccessor()
        self.hackathon_entity_object = HackathonEntity()

    def get_leaderboard(self, hackathon_id):
        """
        this is a utility method used by leaderboard api to access the DAOs and get the scores
        """
        self.hackathon_entity_object.hackathon_id = hackathon_id
        result = self.dao.get_sorted_scores(self.hackathon_entity_object)
        if len(result) == 0:
            return "No submissions yet"
        return self.dao.get_sorted_scores(self.hackathon_entity_object)
