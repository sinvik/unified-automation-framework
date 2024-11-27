"""
This module is specifically written for handling API-Endpoints of open API Json PlaceHolder
"""


class EndPoints:
    """
    This class contain methods to retrieve information through api endpoints using requests library
    """

    @staticmethod
    def get_user_endpoint(user_id=''):
        """
        Get a user by ID.

        :param user_id: ID of the user to retrieve.
        :return: endpoint
        """
        if not user_id:
            return "users"
        return f"users/{user_id}"

    @staticmethod
    def get_post_endpoint(post_id=''):
        """
        Get a post by ID.

        :param post_id: ID of the post to retrieve.
        :return: end.
        """
        if not post_id:
            return "posts"
        return f"posts/{post_id}"

    # def create_post(self, title, body, user_id):
    #     """
    #     Create a new post.
    #
    #     :param title: Title of the post.
    #     :param body: Body of the post.
    #     :param user_id: ID of the user creating the post.
    #     :return: Response object from the POST request.
    #     """
    #     url = f"{self.BASE_URL}/posts"
    #     payload = {
    #         "title": title,
    #         "body": body,
    #         "userId": user_id
    #     }
    #     response = self.session.post(url, json=payload)
    #     return response
    #
    # def update_post(self, post_id, title=None, body=None, user_id=None):
    #     """
    #     Update an existing post.
    #
    #     :param post_id: ID of the post to update.
    #     :param title: New title of the post (optional).
    #     :param body: New body of the post (optional).
    #     :param user_id: New user ID of the post (optional).
    #     :return: Response object from the PUT request.
    #     """
    #     url = f"{self.BASE_URL}/posts/{post_id}"
    #     payload = {
    #         "title": title,
    #         "body": body,
    #         "userId": user_id
    #     }
    #     response = self.session.put(url, json={k: v for k, v in payload.items() if v is not None})
    #     return response
    #
    # def delete_post(self, post_id):
    #     """
    #     Delete a post by ID.
    #
    #     :param post_id: ID of the post to delete.
    #     :return: Response object from the DELETE request.
    #     """
    #     url = f"{self.BASE_URL}/posts/{post_id}"
    #     response = self.session.delete(url)
    #     return response
