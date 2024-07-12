class ActivityFinderController:
    def __init__(self, activities_repository) -> None:
        self.__activities_repository = activities_repository

    def get_activities(self, trip_id) -> dict:
        try:
            activities = self.__activities_repository.find_activities_by_trip_id(trip_id)
            
            activities_info = []
            for activity in activities:
                activities_info.append({
                    'id': activity[0],
                    'title': activity[2],
                    'occurs_at': activity[3],
                })

            return {
                'body': {
                    'activities': activities_info
                },
                'status_code': 200
            }

        except Exception as e:
            return {
                'body': {'error': 'Bad request', 'message': str(e)},
                'status_code': 400
            }
