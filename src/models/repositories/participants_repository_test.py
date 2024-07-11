import pytest
import uuid
from faker import Faker
from src.models.settings.db_connection_handler import db_connection_handler
from .participants_repository import ParticipantsRepository

fake = Faker()

db_connection_handler.connect()

# @pytest.mark.skip(reason='Database interaction test')
def get_emails_to_invite_id():
    conn = db_connection_handler.get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM emails_to_invite')
    emails_to_invite_id = cursor.fetchone()[0]
    cursor.close()
    return emails_to_invite_id

trip_id = str(uuid.uuid4())
emails_to_invite_id = get_emails_to_invite_id()


# @pytest.mark.skip(reason='Database interaction test')
def test_participant_register():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'name': fake.name(),
        'emails_to_invite_id': emails_to_invite_id
    }

    participants_repository.participant_register(participant_info)


# @pytest.mark.skip(reason='Database interaction test')
def test_find_participants_by_trip_id():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participants = participants_repository.find_participants_by_trip_id(trip_id)

    assert isinstance(participants, list)
    assert isinstance(participants[0], tuple)


# @pytest.mark.skip(reason='Database interaction test')
def test_update_participant_status():
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    
    participants = participants_repository.find_participants_by_trip_id(trip_id)
    participant_id = participants[0][0]

    participants_repository.update_participant_status(participant_id)
