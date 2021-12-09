import graphene

from .types import UserType
from .queries import *
from .mutations import *


class Query(object):
    user = graphene.Field(
        UserType, id=graphene.Int(required=True), resolver=resolve_user
    )
    me = graphene.Field(UserType, resolver=resolve_me)


class Mutation(object):
    # mutation을 받아서 필드 형태로  변환
    create_account = CreateAccountMutations.Field()
    login = LoginMutation.Field()
    toggle_favs = ToggleMutation.Field()
    edit_profile = EditProfileMutation.Field()

