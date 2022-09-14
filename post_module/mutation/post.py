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

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()


schema = graphene.Schema(mutation=Mutation)
