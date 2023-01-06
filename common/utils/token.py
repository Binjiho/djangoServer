from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken


class HESMKToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        """
        Returns an authorization token for the given user that will be provided
        after authenticating the user's credentials.
        """
        usr_key = getattr(user, api_settings.USER_ID_FIELD)
        if not isinstance(usr_key, int):
            usr_key = str(usr_key)

        token = cls()
        token[api_settings.USER_ID_CLAIM] = usr_key
        # token['user_type'] = user.user_type
        # token['is_admin'] = user.is_admin
        return token
