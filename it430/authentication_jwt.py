from datetime import datetime, timedelta, timezone
import jwt
from it430.models import Customer as User
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, ParseError

jwt_key = 'it430_key'

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Extract the JWT from the Authorization header
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        # print(jwt_token)
        if jwt_token is None:
            return None

        jwt_token = JWTAuthentication.get_the_token_from_header(jwt_token)  # clean the token

        # Decode the JWT and verify its signature
        try:
            payload = jwt.decode(jwt_token, key=jwt_key, algorithms=['HS256'])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed('Invalid signature')
        except jwt.exceptions.ExpiredSignatureError:
            raise AuthenticationFailed('Expired signature')
        except Exception as err:
            print(err)
            raise ParseError()

        # Verify user information exists
        user_id = payload.get("user_id")
        if user_id is None:
            raise AuthenticationFailed('User identifier not found in JWT')
        user = User.objects.filter(user_id=user_id).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        # Return the token payload
        return payload

    def authenticate_header(self, request):
        return 'Bearer'

    @classmethod
    def create_jwt(cls, user):
        # Create the JWT payload
        payload = {
            'username': user.username,
            'customer_id': str(user.customer_id),
            'user_type': 'customer',
            'family_id': str(user.family_id),
            "first_name": user.first_name,
            "last_name": user.last_name,
            "exp": datetime.now(timezone.utc) + timedelta(hours=8),
            "iat": datetime.now(timezone.utc)
        }
        # Encode the JWT with your secret key
        jwt_token = jwt.encode(payload, key=jwt_key, algorithm='HS256')

        return jwt_token

    @classmethod
    def get_the_token_from_header(cls, token):
        token = token.replace('Bearer', '').replace(' ', '')  # clean the token
        return token