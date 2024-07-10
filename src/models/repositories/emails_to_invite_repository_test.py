import pytest
import uuid
from faker import Faker
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

fake = Faker()

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason='Database interaction test')
def test_email_register():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trip_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'email': fake.email()
    }

    emails_to_invite_repository.email_register(email_trip_info)


@pytest.mark.skip(reason='Database interaction test')
def test_find_emails_by_trip_id():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_by_trip_id(trip_id)

    assert isinstance(emails, list)
    assert isinstance(emails[0], tuple)
