class LinkFinderController:
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository

    def get_links(self, trip_id):
        try:
            links = self.__links_repository.find_links_by_trip_id(trip_id)
            
            formated_links = []
            for link in links:
                formated_links.append({
                    'id': link[0],
                    'url': link[2],
                    'title': link[3]
                })

            return {
                'body': {
                    'links': formated_links
                },
                'status_code': 200
            }

        except Exception as e:
            return {
                'body': {'error': 'Bad request', 'message': str(e)},
                'status_code': 400
            }
