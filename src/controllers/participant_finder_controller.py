class ParticipantFinderController:
    def __init__(self, participant_repository) -> None:
        self.__participant_repository = participant_repository

    def get_participants(self, trip_id) -> dict:
        try:
            participants = self.__participant_repository.find_participants_by_trip_id(trip_id)
            
            participants_info = []
            for participant in participants:
                participants_info.append({
                    'id': participant[0],
                    'name': participant[1],
                    'is_confirmed': participant[2],
                    'email': participant[3]
                })

            return {
                'body': {
                    'participants': participants_info
                },
                'status_code': 200
            }

        except Exception as e:
            return {
                'body': {'error': 'Bad request', 'message': str(e)},
                'status_code': 400
            }
