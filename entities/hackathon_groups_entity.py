import validictory
from common_validation import VALIDATION_MAP


class HackathonGroupEntity:
    def __init__(self):
        self.__hackathon_group_id = None
        self.__hackathon_id = None
        self.__group_id = None
        self.__token = None

    @property
    def hackathon_group_id(self):
        return self.__hackathon_group_id

    @hackathon_group_id.setter
    def hackathon_group_id(self, value):
        validictory.validate(value, VALIDATION_MAP["hackathon_group_id"])
        self.__hackathon_group_id = value

    @property
    def hackathon_id(self):
        return self.__hackathon_id

    @hackathon_id.setter
    def hackathon_id(self, value):
        validictory.validate(value, VALIDATION_MAP["hackathon_id"])
        self.__hackathon_id = value

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, value):
        validictory.validate(value, VALIDATION_MAP["group_id"])
        self.__group_id = value

    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, value):
        validictory.validate(value, VALIDATION_MAP["token"])
        self.__token = value
