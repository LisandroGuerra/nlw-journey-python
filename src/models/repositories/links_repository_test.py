import pytest
import uuid
from faker import Faker
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

fake = Faker()

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason='Database interaction test')
def test_link_register():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    link_trip_info = {
        'id': str(uuid.uuid4()),
        'trip_id': trip_id,
        'link': fake.url(),
        'title': fake.sentence()
    }

    links_repository.link_register(link_trip_info)


@pytest.mark.skip(reason='Database interaction test')
def test_find_links_by_trip_id():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    trip_links = links_repository.find_links_by_trip_id(trip_id)

    assert isinstance(trip_links, list)
    assert isinstance(trip_links[0], tuple)
