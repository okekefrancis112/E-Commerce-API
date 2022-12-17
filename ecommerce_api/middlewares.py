


class CustomAuthMiddleware(object):
    def resolve(self, next, root, info, **kwargs):
        info.context.user = self.authorize_user(info)
        return next(root, info, **kwargs)

    @staticmethod
    def authorize_user(info):