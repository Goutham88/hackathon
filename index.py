import validictory
from flask import request, Flask, json
from flask_restful import Api

from base_controller import BaseController
from common_validation import SCHEMA
from leaderboard_handler import LeaderBoardHandler
from submission_handler import SubmissionHandler

app = Flask(__name__)
app.secret_key = "secret key"
if __name__ == "__main__":
    app.run(debug=True)

api = Api(app)


class LeaderBoardController(BaseController):
    """
    LeaderBoard API
    """
    def get(self):
        """
        GET of leaderboard API - takes hackathon id and returns all the scores for that hackathon
        """
        try:
            hackathon_id = request.args.get("hackathon_id")
            leaderboard_data = LeaderBoardHandler().get_leaderboard(hackathon_id)
            response = app.response_class(
                response=json.dumps({"leaderboard_data": leaderboard_data}),
                status=200,
                mimetype='application/json'
            )
            return response

        except Exception as ex:
            raise ex


api.add_resource(LeaderBoardController, '/leaderboard/', endpoint="leaderboard")


class SubmissionController(BaseController):
    """
    Submission API
    """
    def post(self):
        """
        POST of submission API - takes code, hackathon_id, group_id and returns score and passed testcases
        """
        try:
            request_data = request.get_json()
            validictory.validate(request_data, SCHEMA["submission_post_schema"])
            files = request_data.get("files")
            hackathon_id = request_data.get("hackathon_id")
            group_id = request_data.get("group_id")
            testcase_result = SubmissionHandler().run_testcases(files, hackathon_id, group_id)
            return testcase_result
        except Exception as ex:
            raise ex


api.add_resource(SubmissionController, '/submission/', endpoint="submission")
