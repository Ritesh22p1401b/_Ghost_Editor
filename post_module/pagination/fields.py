from graphene import Boolean, Field, Int, List, ObjectType, String
from graphene.relay import Connection
from graphene_django.filter import DjangoFilterConnectionField
from .pages_functionality import convert_connection_args_to_page_options
from .pagination import create_page_cursors


class PageCursor(ObjectType):
    cursor = String()
    is_current = Boolean()
    page = Int()


class PageCursors(ObjectType):
    around = List(PageCursor)
    first = Field(PageCursor)
    last = Field(PageCursor)
    next = Field(PageCursor)
    previous = Field(PageCursor)


class PageConnection(Connection):
    class Meta:
        abstract = True

    page_cursors = Field(PageCursors)


class PageConnectionField(DjangoFilterConnectionField):

    @classmethod
    def resolve_connection(cls, _connection, args, iterable, max_limit=None):
        connection = super(PageConnectionField, cls).resolve_connection(
            _connection, args, iterable, max_limit
        )

        page_options = convert_connection_args_to_page_options(args)
        page_cursors = create_page_cursors(page_options, connection.length)
        connection.page_cursors = page_cursors

        return connection
