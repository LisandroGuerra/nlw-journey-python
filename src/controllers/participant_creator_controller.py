import uuid


class ParticipantCreatorController:
    def __init__(self, participants_repository, emails_to_invite_repository) -> None:
        self.__participants_repository = participants_repository
        self.__emails_to_invite_repository = emails_to_invite_repository

    def create_participant(self, body, trip_id) -> dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            email_info = {
                'id': email_id,
                'trip_id': trip_id,
                'email': body['email']            
            }

            participant_info = {
                'id': participant_id,
                'trip_id': trip_id,
                'name': body['name'],
                'emails_to_invite_id': email_id            
            }

            self.__participants_repository.participant_register(participant_info)
            self.__emails_to_invite_repository.email_register(email_info)

            return {
                'body': {
                    'participant_id': participant_id,
                    },
                'status_code': 201
            }

        except Exception as e:
            return { 
                'body': { 'error': 'Bad request', 'message': str(e)},
                'status_code': 400 }
