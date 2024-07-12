from flask import Blueprint, jsonify, request

trips_routes_bp = Blueprint('trip_routes', __name__)

#Controllers import
from src.controllers.trip_creator_controller import TripCreatorController
from src.controllers.trip_finder_controller import TripFinderController
from src.controllers.trip_confirmer_controller import TripConfirmerController

from src.controllers.link_creator_controller import LinkCreatorController
from src.controllers.link_finder_controller import LinkFinderController

from src.controllers.participant_creator_controller import ParticipantCreatorController
from src.controllers.participant_finder_controller import ParticipantFinderController
from src.controllers.participant_confirmer_controller import ParticipantConfirmerController

from src.controllers.activity_creator_controller import ActivityCreatorController
from src.controllers.activity_finder_controller import ActivityFinderController

#Repositories import
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.activities_repository import ActivitiesRepository

#Connection manager import
from src.models.settings.db_connection_handler import db_connection_handler


@trips_routes_bp.route('/trips', methods=['POST'])
def create_trip():
    conn = db_connection_handler.get_connection()
    trip_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = TripCreatorController(trip_repository, emails_repository)

    response = controller.create(request.json)


    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>', methods=['GET'])
def get_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinderController(trips_repository)

    response = controller.find_trip_details(trip_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>/confirm', methods=['PATCH'])
def confirm_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmerController(trips_repository)

    response = controller.confirm_trip(trip_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>/links', methods=['POST'])
def create_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreatorController(links_repository)

    response = controller.create_link(request.json, trip_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>/links', methods=['GET'])
def get_trip_links(trip_id):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinderController(links_repository)

    response = controller.get_links(trip_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>/invites', methods=['POST'])
def invite_to_trip(trip_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreatorController(participants_repository, emails_repository)

    response = controller.create_participant(request.json, trip_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>/participants', methods=['GET'])
def get_trip_participants(trip_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinderController(participants_repository)

    response = controller.get_participants(trip_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/participants/<participant_id>/confirm', methods=['PATCH'])
def confirm_participant(participant_id):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmerController(participants_repository)

    response = controller.confirm_participant(participant_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['POST'])
def create_trip_activity(trip_id):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityCreatorController(activities_repository)

    response = controller.create_activity(request.json, trip_id)

    return jsonify(response['body']), response['status_code']


@trips_routes_bp.route('/trips/<trip_id>/activities', methods=['GET'])
def get_trip_activities(trip_id):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityFinderController(activities_repository)

    response = controller.get_activities(trip_id)

    return jsonify(response['body']), response['status_code']
