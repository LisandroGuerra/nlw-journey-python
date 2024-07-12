import uuid


class ActivityCreatorController:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def create_activity(self, body, trip_id) -> dict:
        try:
            activity_id = str(uuid.uuid4())

            activity_info = {
                'id': activity_id,
                'trip_id': trip_id,
                'title': body['title'],
                'occurs_at': body['occurs_at']
            }

            self.__activities_repository.activity_register(activity_info)

            return {
                'body': {
                    'activity_id': activity_id,
                    },
                'status_code': 201
            }
        
        except Exception as e:
            return { 
                'body': { 'error': 'Bad request', 'message': str(e)},
                'status_code': 400 }
