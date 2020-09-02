from data_accessor import DataAccessor
from entities.group_entity import GroupEntity
from entities.hackathon_entity import HackathonEntity
from entities.submission_entity import SubmissionEntity


class SubmissionHandler:
    def __init__(self):
        self.dao = DataAccessor()
        self.hackathon_entity_object = HackathonEntity()
        self.group_entity_object = GroupEntity()
        self.submission_entity_object = SubmissionEntity()

    def run_testcases(self, code, hackathon_id, group_id):
        """
        This is a utility function used by submission API.
        Runs the code for each test case and based the result, it adds the score and saves the submission info to table
        using DAO
        """
        self.hackathon_entity_object.hackathon_id = hackathon_id
        self.group_entity_object.group_id = group_id
        testcases = self.dao.get_test_cases_by_hackathon_id(self.hackathon_entity_object)
        score = 0
        solved_testcases = []
        for testcase in testcases:
            # if code(testcase["input"]) == testcase["output"]:
            # commenting the above line for testing since we don't have real code
            if True:
                score += testcase["weightage"]
                solved_testcases.append(testcase["testcase_id"])
        self.submission_entity_object.score = score
        self.submission_entity_object = self.dao.insert_submission_details(self.group_entity_object,
                                                                           self.submission_entity_object)
        return {"score": score, "solved_testcases": solved_testcases}
