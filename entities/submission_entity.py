import validictory

from common_validation import VALIDATION_MAP


class SubmissionEntity:
    def __init__(self):
        self.__submission_id = None
        self.__hackathon_group_id = None
        self.__score = None

    @property
    def submission_id(self):
        return self.__submission_id

    @submission_id.setter
    def submission_id(self, value):
        validictory.validate(value, VALIDATION_MAP["submission_id"])
        self.__submission_id = value

    @property
    def hackathon_group_id(self):
        return self.__hackathon_group_id

    @hackathon_group_id.setter
    def hackathon_group_id(self, value):
        validictory.validate(value, VALIDATION_MAP["hackathon_group_id"])
        self.__hackathon_group_id = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        validictory.validate(value, VALIDATION_MAP["score"])
        self.__score = value
