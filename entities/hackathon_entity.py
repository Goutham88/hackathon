import validictory
from common_validation import VALIDATION_MAP


class HackathonEntity:
    def __init__(self):
        self.__hackathon_id = None
        self.__start_datetime = None
        self.__end_datetime = None

    @property
    def hackathon_id(self):
        return self.__hackathon_id

    @hackathon_id.setter
    def hackathon_id(self, value):
        validictory.validate(value, VALIDATION_MAP["hackathon_id"])
        self.__hackathon_id = value

    @property
    def start_datetime(self):
        return self.__start_datetime

    @start_datetime.setter
    def start_datetime(self, value):
        validictory.validate(value, VALIDATION_MAP["start_datetime"])
        self.__start_datetime = value

    @property
    def end_datetime(self):
        return self.__end_datetime

    @end_datetime.setter
    def end_datetime(self, value):
        validictory.validate(value, VALIDATION_MAP["end_datetime"])
        self.__end_datetime = value
