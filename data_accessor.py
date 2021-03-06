import pymysql

from custom_exception import DBException


class DataAccessor:
    def __init__(self):
        self.conn = pymysql.connect("sql12.freemysqlhosting.net", "sql12362999", "vDQ9nbAFIr", "sql12362999")
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def get_sorted_scores(self, hackathon_entity_object):
        """
        This is used by leaderboard API to get the all the scores of hackathon in sorted manner
        """
        try:
            query = "select group_name,max_score from groups join hackathon_groups using (group_id) where " \
                    "hackathon_id = %s order by 2 desc"
            self.cursor.execute(query % hackathon_entity_object.hackathon_id)
            return self.cursor.fetchall()
        except Exception as ex:
            raise DBException(str(ex))

    def get_test_cases_by_hackathon_id(self, hackathon_entity_object):
        """
        This is the data access function to get all testcases for a hackathon
        """
        try:
            query = "select * from testcases where hackathon_id = %s"
            self.cursor.execute(query % hackathon_entity_object.hackathon_id)
            return self.cursor.fetchall()
        except Exception as ex:
            raise DBException(str(ex))

    def insert_submission_details(self, group_entity_object, submission_entity_object):
        """
        For every new submission we insert the submitted data to submissions table here
        """
        try:
            query = "select hackathon_group_id from hackathon_groups where group_id = %s"
            self.cursor.execute(query % group_entity_object.group_id)
            submission_entity_object.hackathon_group_id = self.cursor.fetchall()[0]["hackathon_group_id"]

            query = "insert into submissions(hackathon_group_id, score) values (%s, %s)"
            self.cursor.execute(query % (submission_entity_object.hackathon_group_id, submission_entity_object.score))
            self.conn.commit()
            self.update_max_score(group_entity_object, submission_entity_object)
            return submission_entity_object
        except Exception as ex:
            raise DBException(str(ex))

    def update_max_score(self, group_entity_object, submission_entity_object):
        """
        updates the max_score value for respective group
        """
        try:
            query = "select max_score from groups where group_id = %s"
            self.cursor.execute(query % group_entity_object.group_id)
            max_score = self.cursor.fetchall()[0]["max_score"]
            if submission_entity_object.score > max_score:
                group_entity_object.max_score = submission_entity_object.score
                query = "update groups set score = %s where group_id = %s"
                self.cursor.execute(query % (submission_entity_object.score, group_entity_object.group_id))
                self.conn.commit()
        except Exception as ex:
            raise DBException(str(ex))
