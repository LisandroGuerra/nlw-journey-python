from sqlite3 import Connection


class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def participant_register(self, participant_info: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO participants 
                (id, trip_id, name, emails_to_invite_id)
            VALUES (?, ?, ?, ?)
            ''', 
            (
                participant_info['id'],
                participant_info['trip_id'],
                participant_info['name'],
                participant_info['emails_to_invite_id']
            )
        )
        self.__conn.commit()
        cursor.close()

    def find_participants_by_trip_id(self, trip_id: str) -> list[tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            SELECT p.id, p.name, p.is_confirmed, e.email
            FROM participants p
            JOIN emails_to_invite e
            ON e.id = p.emails_to_invite_id
            WHERE p.trip_id = ?
            ''', (trip_id,)
        )
        participants = cursor.fetchall()
        cursor.close()
        return participants

    def update_participant_status(self, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            UPDATE participants
            SET is_confirmed = 1
            WHERE id = ?
            ''', (participant_id,)
        )
        self.__conn.commit()
        cursor.close()