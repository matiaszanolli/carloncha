from sqlalchemy import TypeDecorator, String


class ChoiceField(TypeDecorator):
    impl = String

    cache_ok = True

    def __init__(self, choices):
        self.choices = tuple(choices)
        self.internal_only = True
