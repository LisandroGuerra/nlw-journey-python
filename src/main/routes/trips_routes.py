from flask import Blueprint, jsonify, request

trips_routes_bp = Blueprint('trip_routes', __name__)

#Controllers import
from src.controllers.trip_creator_controller import TripCreatorController
from src.controllers.trip_finder_controller import TripFinderController

#Repositories import
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository

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
