import pytest
import uuid
from faker import Faker
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

fake = Faker()

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason='Database interaction test')
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trip_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'email': fake.email()
    }

    emails_to_invite_repository.registry_email(email_trip_info)


@pytest.mark.skip(reason='Database interaction test')
def test_find_emails_by_trip_id():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_by_trip_id(trip_id)
