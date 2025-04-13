from models.ports.analysis_repository import AnalysisRepository
from mysql.connector import MySQLConnection
from models.analysis.analysis import Analysis


class AnalysisRepositoryInRDB(AnalysisRepository):
    def __init__(self, connection: MySQLConnection):
        self.connection = connection
        self.cursor = connection.cursor()

    def get_analysis_by_id(self, id: int) -> Analysis:
        self.cursor.execute("SELECT * FROM analysis WHERE id=%s", (id,))
        result = self.cursor.fetchone()
        return Analysis(result[1], result[2], result[3], result[0])

    def get_analysis_by_user_id(self, user_id: int) -> list:
        self.cursor.execute("SELECT * FROM analysis WHERE user_id=%s", (user_id,))
        result = self.cursor.fetchall()
        analysis = []

        for row in result:
            analysis.append(Analysis(row[1], row[2], row[3], row[0]))

        return analysis

    def register(self, analysis: Analysis) -> None:
        SQL = "INSERT INTO analysis (title, details, user_id) VALUES (%s, %s, %s)"
        self.cursor.execute(
            SQL,
            (
                analysis.get_title(),
                analysis.get_details(),
                analysis.get_user_id(),
            ),
        )
        self.connection.commit()
