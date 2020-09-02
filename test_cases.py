import pytest
from _pytest.monkeypatch import MonkeyPatch

from custom_exception import DBException
from data_accessor import DataAccessor
from entities.submission_entity import SubmissionEntity
from leaderboard_handler import LeaderBoardHandler
from submission_handler import SubmissionHandler

mp = MonkeyPatch()

def test_get_leaderboard():
    lbh_obj = LeaderBoardHandler()

    def mock_get_sorted_scores(self, hid):
        return_data = [
            {
                "group_name": "goutham team",
                "max_score": 1000
            }
        ]
        return return_data

    mp.setattr(DataAccessor, "get_sorted_scores", mock_get_sorted_scores)
    assert lbh_obj.get_leaderboard(1)[0]["group_name"] == "goutham team"


def test_get_leaderboard_empty():
    lbh_obj = LeaderBoardHandler()

    def mock_get_sorted_scores(self, hid):
        return_data = []
        return return_data

    mp.setattr(DataAccessor, "get_sorted_scores", mock_get_sorted_scores)
    assert lbh_obj.get_leaderboard(1) == "No submissions yet"

def test_get_leaderboard_exception():
    lbh_obj = LeaderBoardHandler()

    def mock_get_sorted_scores(self, hid):
        raise DBException

    mp.setattr(DataAccessor, "get_sorted_scores", mock_get_sorted_scores)
    with pytest.raises(DBException):
        lbh_obj.get_leaderboard(1)


def test_run_testcases():
    sh_obj = SubmissionHandler()


    def mock_get_test_cases_by_hackathon_id(self, hid):
        test_cases = [
            {
                "testcase_id": 1,
                "weightage": 5,
                "hackathon_id": 2,
                "input": "sample",
                "output": "sample"
            },
            {
                "testcase_id": 2,
                "weightage": 15,
                "hackathon_id": 2,
                "input": "sample",
                "output": "sample"
            }
        ]
        return test_cases

    def mock_insert_submission_details(self, hgid, score):
        a = SubmissionEntity()
        a.score = 20
        return a

    mp.setattr(DataAccessor, "get_test_cases_by_hackathon_id", mock_get_test_cases_by_hackathon_id)
    mp.setattr(DataAccessor, "insert_submission_details", mock_insert_submission_details)
    assert sh_obj.run_testcases("", 2, 2)["score"] == 20


def test_run_testcases_exception():
    sh_obj = SubmissionHandler()


    def mock_get_test_cases_by_hackathon_id(self, hid):
        raise DBException

    def mock_insert_submission_details(self, hgid, score):
        a = SubmissionEntity()
        a.score = 20
        return a

    mp.setattr(DataAccessor, "get_test_cases_by_hackathon_id", mock_get_test_cases_by_hackathon_id)
    mp.setattr(DataAccessor, "insert_submission_details", mock_insert_submission_details)
    with pytest.raises(DBException):
        sh_obj.run_testcases("", 2, 2)["score"]
