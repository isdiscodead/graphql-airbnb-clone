import graphene


class Query(graphene.ObjectType):
    hello = graphene.String()   # string return query

    # hello와 관련된 String resolver ( resolve_쿼리명() )
    # info 객체는 resolver의 모든 정보( 서버, 연결, 요청 )를 가짐
    def resolve_hello(self, info):
        return "Hello"



class Mutation():
    pass


schema = graphene.Schema(query=Query)
