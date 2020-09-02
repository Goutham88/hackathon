from mock import MagicMock
from leaderboard_handler import LeaderBoardHandler
from data_accessor import DataAccessor


def test_get_leaderboard():
    lbh_obj = LeaderBoardHandler()
    return_data = {
        "leaderboard_data": [
            {
                "group_name": "goutham team",
                "max_score": 1000
            }
        ]
    }
    DataAccessor().get_sorted_scores = MagicMock(return_value = return_data)
    assert lbh_obj.get_leaderboard(1) == return_data