from flask import Blueprint, jsonify

trips_routes_bp = Blueprint('trip_routes', __name__)

@trips_routes_bp.route('/trips', methods=['POST'])
def create_trip():
    return jsonify({'message': 'Trip created'}), 201
