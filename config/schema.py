import graphene

from rooms.models import Room


class RoomType(graphene.ObjectType):
    # models.py에 있는 내용 graphene으로 변경
    name = graphene.String()
    address = graphene.String()
    price = graphene.Int()
    beds = graphene.Int()


class Query(graphene.ObjectType):
    hello = graphene.String()   # string return query
    # Field -> 객체 등 복잡한 정보 / List -> 객체 등의 리스트
    rooms = graphene.List(RoomType)

    # hello와 관련된 String resolver ( resolve_쿼리명() )
    # info 객체는 resolver의 모든 정보( 서버, 연결, 요청 )를 가짐
    def resolve_hello(self, info):
        return "Hello"

    def resolve_rooms(self, info):
        return Room.Objects.all()

class Mutation():
    pass


schema = graphene.Schema(query=Query)
