import uuid

class TripCreatorController:
    def __init__(self, trip_repository, emails_repository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository

    def create(self, body) -> dict:
        try:
            emails = body.get('emails_to_invite')

            trip_id = str(uuid.uuid4())
            trip_info = { **body, 'id': trip_id, 'status': 0 }

            self.__trip_repository.create_trip(trip_info)

            if emails:
                for email in emails:
                    self.__emails_repository.email_register({
                        'id': str(uuid.uuid4()),
                        'trip_id': trip_id,
                        'email': email
                    })

            return {
                'body': {'id': trip_id},
                'status_code': 201
            }
        except Exception as e:
            return {
                'body': {'error': 'Bad request', 'message': str(e)},
                'status_code': 400
            }
