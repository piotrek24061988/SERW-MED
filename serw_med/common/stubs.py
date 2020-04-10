

class RequestStub:
    class USER:
        @staticmethod
        def validate_unique(exclude):
            pass

        @staticmethod
        def full_clean(exclude, validate_unique):
            pass

        def is_authenticated(self):
            return True

        class _meta:
            concrete_fields = ''
            private_fields = ''
            many_to_many = ''
            fields = ''

        class profile:
            @staticmethod
            def validate_unique(exclude):
                pass

            @staticmethod
            def full_clean(exclude, validate_unique):
                pass

            class _meta:
                concrete_fields = ''
                private_fields = ''
                many_to_many = ''
                fields = ''

    META = {'CSRF_COOKIE': []}
    user = USER
    method = 'POST'
    POST = {'POST': []}
    FILES = {'FILES': []}