import unittest

import pytest
from _pytest.monkeypatch import MonkeyPatch

from custom_exception import DBException
from data_accessor import DataAccessor
from entities.group_entity import GroupEntity
from entities.hackathon_entity import HackathonEntity
from entities.submission_entity import SubmissionEntity
from leaderboard_handler import LeaderBoardHandler
from submission_handler import SubmissionHandler

mp = MonkeyPatch()


class TestCases(unittest.TestCase):

    def test_get_leaderboard(self):
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

    def test_get_leaderboard_empty(self):
        lbh_obj = LeaderBoardHandler()

        def mock_get_sorted_scores(self, hid):
            return_data = []
            return return_data

        mp.setattr(DataAccessor, "get_sorted_scores", mock_get_sorted_scores)
        assert lbh_obj.get_leaderboard(1) == "No submissions yet"

    def test_get_leaderboard_exception(self):
        lbh_obj = LeaderBoardHandler()

        def mock_get_sorted_scores(self, hid):
            raise DBException

        mp.setattr(DataAccessor, "get_sorted_scores", mock_get_sorted_scores)
        with pytest.raises(DBException):
            lbh_obj.get_leaderboard(1)
        mp.undo()

    def test_run_testcases(self):
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

    def test_run_testcases_exception(self):
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
            sh_obj.run_testcases("", 2, 2)

    def test_get_sorted_scores(self):
        dao = DataAccessor()

        def mock_execute(query):
            pass

        mp.setattr(dao.cursor, "execute", mock_execute)

        def mock_fetch_all():
            return [
                {
                    "group_name": "goutham team",
                    "max_score": 1000
                }
            ]

        mp.setattr(dao.cursor, "fetchall", mock_fetch_all)
        assert dao.get_sorted_scores(HackathonEntity())[0]["group_name"] == "goutham team"

    def test_get_sorted_scores_exception(self):
        dao = DataAccessor()

        def mock_execute(query):
            raise

        mp.setattr(dao.cursor, "execute", mock_execute)
        with pytest.raises(DBException):
            dao.get_sorted_scores("")

    def test_get_test_cases_by_hackathon_id(self):
        dao = DataAccessor()

        def mock_execute(query):
            pass

        mp.setattr(dao.cursor, "execute", mock_execute)

        def mock_fetch_all():
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

        mp.setattr(dao.cursor, "fetchall", mock_fetch_all)
        assert dao.get_test_cases_by_hackathon_id(HackathonEntity())[0]["input"] == "sample"

    def test_get_test_cases_by_hackathon_id_exception(self):
        dao = DataAccessor()

        def mock_execute(query):
            raise

        mp.setattr(dao.cursor, "execute", mock_execute)
        with pytest.raises(DBException):
            dao.get_test_cases_by_hackathon_id("")

    def test_update_max_score(self):
        dao = DataAccessor()

        def mock_execute(query):
            assert query == "select max_score from groups where group_id = 2123"

        mp.setattr(dao.cursor, "execute", mock_execute)

        def mock_fetch_all():
            return [
                {
                    "max_score": 5
                }
            ]

        mp.setattr(dao.cursor, "fetchall", mock_fetch_all)
        ge = GroupEntity()
        ge.group_id = 2123
        se = SubmissionEntity()
        se.score = 1
        dao.update_max_score(ge, se)

    def test_update_max_score_exception(self):
        dao = DataAccessor()

        def mock_execute(query):
            raise

        mp.setattr(dao.cursor, "execute", mock_execute)
        with pytest.raises(DBException):
            dao.update_max_score("", "")
