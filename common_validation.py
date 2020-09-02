GROUP_ID = {"type": ["integer", "string"], "pattern": "^[0-9]+$"}
GROUP_NAME = {"type": "string", "minLength": 1, "maxLength": 100}
GROUP_TAG_LINE = {"type": "string", "minLength": 1, "maxLength": 100}
MAX_SCORE = {"type": ["integer", "string"], "pattern": "^[0-9]+$"}
HACKATHON_ID = {"type": ["integer", "string"], "pattern": "^[0-9]+$"}
DATE = {"format": "date"}
TOKEN = {"type": "string", "minLength": 1, "maxLength": 100}
HACKATHON_GROUP_ID = {"type": ["integer", "string"], "pattern": "^[0-9]+$"}
TESTCASE_ID = {"type": ["integer", "string"], "pattern": "^[0-9]+$"}
INPUT = {"type": "string", "minLength": 1, "maxLength": 100}
OUTPUT = {"type": "string", "minLength": 1, "maxLength": 100}
WEIGHTAGE = {"type": ["integer", "string"], "pattern": "^[0-9]+$"}
IS_PUBLIC = {"type": "boolean"}

VALIDATION_MAP = {
    "group_id": GROUP_ID,
    "group_name": GROUP_NAME,
    "group_tag_line": GROUP_TAG_LINE,
    "max_score": MAX_SCORE,
    "hackathon_id": HACKATHON_ID,
    "start_datetime": DATE,
    "end_datetime": DATE,
    "hackathon_group_id": HACKATHON_GROUP_ID,
    "token": TOKEN,
    "testcase_id": TESTCASE_ID,
    "input": INPUT,
    "output": OUTPUT,
    "weightage": WEIGHTAGE,
    "is_public": IS_PUBLIC
}