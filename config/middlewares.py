import jwt


# django-graphql-jwt라는 라이브러리가 존재하지만 직접 만들자!
class JWTMiddleware(object):
    def resolve(self, next, root, info, **args):
        request = info.context
        print(request)
        return next(root, info, **args)
