import uuid


class LinkCreatorController:
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository

    def create_link(self, body, trip_id) -> dict:
        try:
            link_id = str(uuid.uuid4())
            link_info = {
                'link': body['url'],
                'title': body['title'],
                'id': link_id,
                'trip_id': trip_id
            }
            self.__links_repository.link_register(link_info)
            return {
                'body': {
                    'linkId': link_id,
                    'link': body['url'],
                    'title': body['title']
                },
                'status_code': 201
            }
        except Exception as e:
            return {
                'body': { 'error': 'Bad request', 'message': str(e)},
                'status_code': 400
            }
