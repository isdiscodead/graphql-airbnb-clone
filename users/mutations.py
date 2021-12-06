import graphene

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