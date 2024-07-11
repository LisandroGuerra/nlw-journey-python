import pytest
import uuid
from faker import Faker
from src.models.settings.db_connection_handler import db_connection_handler
from .activities_repository import ActivitiesRepository

fake = Faker()

db_connection_handler.connect()

trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason='Database interaction test')
def test_activity_register():
    conn = db_connection_handler.get_connection()  
    activities_repository = ActivitiesRepository(conn)

    activity_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'title': fake.sentence(),
        'occurs_at': fake.date_time_this_year()
    }

    activities_repository.activity_register(activity_info)


@pytest.mark.skip(reason='Database interaction test')
def test_find_activities_by_trip_id():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    
    activities = activities_repository.find_activities_by_trip_id(trip_id)

    assert isinstance(activities, list)
    assert isinstance(activities[0], tuple)
