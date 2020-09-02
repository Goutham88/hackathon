import validictory
from common_validation import VALIDATION_MAP


class GroupEntity:
    def __init__(self):
        self.__group_id = None
        self.__group_name = None
        self.__group_tag_line = None
        self.__max_score = None

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, value):
        validictory.validate(value, VALIDATION_MAP["group_id"])
        self.__group_id = value

    @property
    def group_name(self):
        return self.__group_name

    @group_name.setter
    def group_name(self, value):
        validictory.validate(value, VALIDATION_MAP["group_name"])
        self.__group_name = value

    @property
    def group_tag_line(self):
        return self.__group_tag_line

    @group_tag_line.setter
    def group_tag_line(self, value):
        validictory.validate(value, VALIDATION_MAP["group_tag_line"])
        self.__group_tag_line = value

    @property
    def max_score(self):
        return self.__max_score

    @max_score.setter
    def max_score(self, value):
        validictory.validate(value, VALIDATION_MAP["max_score"])
        self.__max_score = value
