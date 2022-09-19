import graphene
from django.utils import timezone
from post_module.types import PostType
from post_module.models.tags import Tag
from post_module.models.author import Author
from post_module.models.post import Post


class CreatePost(graphene.Mutation):
    
    create_post = graphene.Field(PostType)
    
    class Arguments:
        author_id=graphene.Int()
        tags_id=graphene.Int()
        title=graphene.String()
        subtitle=graphene.String()
        slug=graphene.String()
        body=graphene.String()
        description=graphene.String()
        published_date = graphene.DateTime()
        published=graphene.Boolean()
        date_modified=graphene.DateTime()


    def mutate(self,info,author_id,tags_id,title,subtitle,slug,body,description,published,**kwargs):
        
        author = Author.objects.get(pk=author_id)

        t1=Tag.objects.get(id=tags_id)

        post_create = Post.objects.create(author=author,
            title=title,
            subtitle=subtitle,
            slug=slug,
            body=body,
            description=description,
            published_date=timezone.now(),
            published=published,
            date_modified=timezone.now()
        )

        post_create.tags.add(t1)
        

        return CreatePost(create_post=post_create)


class PostUpdate(graphene.Mutation):
    
    post_update = graphene.Field(PostType)
    
    class Arguments:
        author_id=graphene.Int()
        post_pk=graphene.Int()
        title=graphene.String()
        subtitle=graphene.String()
        slug=graphene.String()
        body=graphene.String()
        description=graphene.String()
        published=graphene.Boolean()
       
    def mutate(self,info,author_id,post_pk,title,subtitle,slug,body,description,published,**kwargs):

        author = Author.objects.get(pk=author_id)

        updated_post=Post.objects.get(id=post_pk)

        updated_post.author=author
        updated_post.title=title
        updated_post.subtitle=subtitle
        updated_post.slug=slug
        updated_post.body=body
        updated_post.description=description
        updated_post.published=published
        updated_post.save()

        return PostUpdate(post_update=updated_post)


class PostDelete(graphene.Mutation):

    post_delete=graphene.Field(PostType)


    class Arguments:
        post_id=graphene.Int(required=True)

    def mutate(self,info,post_id):
        deleteed_post=Post.objects.get(id=post_id)
        deleteed_post.delete()

        return PostDelete(post_delete=deleteed_post)



   
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    post_update = PostUpdate.Field()
    post_delete = PostDelete.Field()

schema = graphene.Schema(mutation=Mutation)
