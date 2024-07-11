class TripConfirmerController:
    def __init__(self, trips_repository) -> None:
        self.__trips_repository = trips_repository

    def confirm_trip(self, trip_id) -> dict:
        try:
            self.__trips_repository.update_trip_status(trip_id)
            return { 'body': None, 'status_code': 204 }
        except Exception as e:
            return { 
                'body': { 'error': 'Bad request', 'message': str(e)},
                'status_code': 400 }
