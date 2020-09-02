from flask import request, Flask, json
from flask_restful import Api
from base_controller import BaseController

from leaderboard_handler import LeaderBoardHandler
from submission_handler import SubmissionHandler
from data_accessor import DataAccessor

app = Flask(__name__)
app.secret_key = "secret key"
if __name__ == "__main__":
    app.run(debug=True)

api = Api(app)


class LeaderBoardController(BaseController):

    def get(self):
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

    def post(self):
        try:
            request_data = request.get_json()
            files = request_data.get("files")
            hackathon_id = request_data.get("hackathon_id")
            group_id = request_data.get("group_id")
            testcase_result = SubmissionHandler().run_testcases(files, hackathon_id, group_id)
            return testcase_result
        except Exception as ex:
            raise ex


api.add_resource(SubmissionController, '/submission/', endpoint="submission")
