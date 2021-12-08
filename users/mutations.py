import graphene
import jwt
from django.contrib.auth import authenticate
from django.conf import settings

from rooms.models import Room
from users.models import User


class CreateAccountMutations(graphene.Mutation):

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    ok = graphene.Boolean()
    error = graphene.String()

    # mutate()는 필수, 위에서 정의한 인자도 필요함 -> *args, **kwargs 사용도 가능
    def mutate(self, info, email, password, first_name=None, last_name=None):
        try:
            User.objects.get(email=email)
            return CreateAccountMutations(ok=False, error="User already exists")
        except User.DoesNotExist:
            try:
                User.objects.create_user(email, email, password)
                return CreateAccountMutations(ok=True)
            except Exception:
                return CreateAccountMutations(ok=False, error="Can't create user.")


class LoginMutation(graphene.Mutation):

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    # 여기 들여쓰기 잘못되면 오류 발생!!
    token = graphene.String()
    pk = graphene.Int()
    error = graphene.String()

    def mutate(self, info, email, password):
        user = authenticate(username=email, password=password)
        if user:
            token = jwt.encode({'pk': user.pk}, settings.SECRET_KEY, algorithm='HS256')
            # 현 상태의 token은 byte 형태이므로 string으로 바꿔줘야 함 -> token.decode("utf-8)
            # 패치가 되었는지 그냥 token으로 동작하네 ...
            return LoginMutation(token=token, pk=user.pk)
        else:
            return LoginMutation(error="Wrong username/password")


class ToggleMutation(graphene.Mutation):
    class Arguments:
        room_id = graphene.Int(required=True)

    ok = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, room_id):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("You need to be logged in")

        try:
            room = Room.objects.get(pk=room_id)
            if room in user.favs.all():
                user.favs.remove(room)
            else:
                user.favs.add(room)
            return ToggleMutation(ok=True)

        except Room.DoesNotExist:
            return ToggleMutation(ok=False, error="Room not found")