
import pytest
import uuid
import datetime
from faker import Faker
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

fake = Faker()

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
start_date = fake.date_time_this_year()


@pytest.mark.skip(reason='Database interaction test')
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip_info = {
        'id': trip_id,
        'destination': fake.city(),
        'start_date': start_date,
        'end_date': start_date + datetime.timedelta(days=5),
        'owner_name': fake.name(),
        'owner_email': fake.email(),
        'status': fake.random_element(elements=(0, 1))
    }

    trips_repository.create_trip(trip_info)


@pytest.mark.skip(reason='Database interaction test')
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trip = trips_repository.find_trip_by_id(trip_id)


@pytest.mark.skip(reason='Database interaction test')
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_repository.update_trip_status(trip_id)

