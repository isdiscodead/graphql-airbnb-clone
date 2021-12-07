import jwt
from django.conf import settings


# django-graphql-jwt라는 라이브러리가 존재하지만 직접 만들자!
from users.models import User


class JWTMiddleware(object):
    def resolve(self, next, root, info, **args):
        request = info.context

        # 사용자가 token을 보내면 암호화를 다시 풀어야 함
        token = request.META.get("HTTP_AUTHORIZATION")
        if token:
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, 'HS256')
                pk = decoded.get("pk")
                user = User.objects.get(pk=pk)
                # info에 user 정보를 담아서 다음 쿼리(next)로 넘겨줌
                info.context.user = user
            except Exception:
                pass

        return next(root, info, **args)
