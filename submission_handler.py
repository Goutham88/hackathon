from data_accessor import DataAccessor
from entities.hackathon_entity import HackathonEntity
from entities.group_entity import GroupEntity


class SubmissionHandler:
    def __init__(self):
        self.dao = DataAccessor()
        self.hackathon_entity_object = HackathonEntity()
        self.group_entity_object = GroupEntity()

    def run_testcases(self, code, hackathon_id, group_id):
        self.hackathon_entity_object.hackathon_id = hackathon_id
        self.group_entity_object.group_id = group_id
        testcases = self.dao.get_test_cases_by_hackathon_id(self.hackathon_entity_object)
        score = 0
        solved_testcases = []
        for testcase in testcases:
            if code(testcase["input"]) == testcase["output"]:
                score += testcase["weightage"]
                solved_testcases.append(testcase["testcase_id"])
        self.dao.insert_submission_details(self.group_entity_object, score)
        return {"score": score, "solved_testcases": solved_testcases}
