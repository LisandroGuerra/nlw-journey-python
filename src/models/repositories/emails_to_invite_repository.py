from sqlite3 import Connection

class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn


    def email_register(self, email_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO emails_to_invite 
                (id, trip_id, email)
            VALUES (?, ?, ?)
            ''', (
                email_info['id'],
                email_info['trip_id'],
                email_info['email']
            )
        )
        self.__conn.commit()
        cursor.close()


    def find_emails_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT * FROM emails_to_invite WHERE trip_id = ?
            ''', (trip_id,)
        )
        trip_emails = cursor.fetchall()
        cursor.close()
        return trip_emails
