from sqlite3 import Connection


class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def activity_register(self, activity_info: dict) -> None:
        cursor = self.__conn.cursor()   
        cursor.execute(
            """
            INSERT INTO activities (id, trip_id, title, occurs_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                activity_info["id"],
                activity_info["trip_id"],
                activity_info["title"],
                activity_info["occurs_at"],
            ),
        )
        self.__conn.commit()
        cursor.close()


    def find_activities_by_trip_id(self, trip_id: str) -> list:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
            SELECT * FROM activities
            WHERE trip_id = ?
            """,
            (trip_id,),
        )
        activities = cursor.fetchall()
        cursor.close()
        
        return activities
