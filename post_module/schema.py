import graphene
from .types import *



#/////......Querying Data........ ////


class Query(graphene.ObjectType):
    all_user=graphene.List(ExtendUserType)
    single_user=graphene.Field(ExtendUserType,id=graphene.Int())
    single_post = graphene.Field(PostType,id=graphene.Int())
    all_post=graphene.List(PostType)
    all_author=graphene.List(AuthorType)
    author= graphene.Field(AuthorType, id=graphene.Int())
    author_by_username = graphene.Field(AuthorType, id=graphene.Int())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())
    

    def resolve_all_user(root,info,**kwargs):
        return ExtendUser.objects.all()

    def resolve_single_user(self,info,id):
        return ExtendUser.objects.get(pk=id)

    def resolve_single_post(self,info,id):
        return Post.objects.get(pk=id)

    def resolve_multiple_post(root,info,**kwargs):
        return Post.objects.all()

    def resolve_author(self,info,id):
        return Author.objects.get(pk=id)

    def resolve_all_author(root,info,**kwargs):
        return Author.objects.all()

    
    def resolve_all_post(root, info):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, id):
        return Author.objects.select_related("username").get(pk=id)

    def resolve_post_by_slug(root, info, slug):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(author__username__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )


schema = graphene.Schema(query=Query)
