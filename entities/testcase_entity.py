import validictory
from common_validation import VALIDATION_MAP


class TestCaseEntity:
    def __init__(self):
        self.__testcase_id = None
        self.__input = None
        self.__output = None
        self.__weightage = None
        self.__is_public = None
        self.__hackathon_id = None

    @property
    def testcase_id(self):
        return self.__testcase_id

    @testcase_id.setter
    def testcase_id(self, value):
        validictory.validate(value, VALIDATION_MAP["testcase_id"])
        self.__testcase_id = value

    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, value):
        validictory.validate(value, VALIDATION_MAP["input"])
        self.__input = value

    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, value):
        validictory.validate(value, VALIDATION_MAP["output"])
        self.__output = value

    @property
    def weightage(self):
        return self.__weightage

    @weightage.setter
    def weightage(self, value):
        validictory.validate(value, VALIDATION_MAP["weightage"])
        self.__weightage = value

    @property
    def is_public(self):
        return self.__is_public

    @is_public.setter
    def is_public(self, value):
        validictory.validate(value, VALIDATION_MAP["is_public"])
        self.__is_public = value

    @property
    def hackathon_id(self):
        return self.__hackathon_id

    @hackathon_id.setter
    def hackathon_id(self, value):
        validictory.validate(value, VALIDATION_MAP["hackathon_id"])
        self.__hackathon_id = value