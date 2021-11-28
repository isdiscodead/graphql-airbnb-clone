import graphene
from graphene_django import DjangoObjectType

from rooms.models import Room


class RoomType(DjangoObjectType):
    class Meta:
        model = Room


class Query(object):
    rooms = graphene.List(RoomType)

    def resolve_rooms(self, info):
        pass
