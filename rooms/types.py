import graphene
from graphene_django import DjangoObjectType

from rooms.models import Room


class RoomType(DjangoObjectType):

    user = graphene.Field("users.schema.UserType")
    is_fav = graphene.Boolean()

    # resolve의 parent는 우리가 보고 있는 객체를 뜻함 -> room
    def resolve_is_fav(room, info):
        user = info.context.user
        if user.is_authenticated:
            return room in user.favsgi.all()

    class Meta:
        model = Room


class RoomListResponse(graphene.ObjectType):
    arr = graphene.List(RoomType)
    total = graphene.Int()