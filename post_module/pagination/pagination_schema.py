# import graphene
# from django_filters import FilterSet, OrderingFilter
# from graphene import ObjectType, relay
# from graphene_django import DjangoObjectType
# from post_module.pagination.fields import PageConnection, PageConnectionField
# from post_module.models.post import Post


# class PostFilter(FilterSet):
#     class Meta:
#         model = Post
#         fields = "__all__"

#     order_by = OrderingFilter(fields=("slug"))


# class PostNode(DjangoObjectType):
#     class Meta:
#         model = Post
#         interfaces = (relay.Node,)
#         connection_class = PageConnection


# class Query(ObjectType):
#     post = relay.Node.Field(PostNode)
#     all_post = PageConnectionField(PostNode, filterset_class=PostFilter)

# schema= graphene.Schema(query=Query)
