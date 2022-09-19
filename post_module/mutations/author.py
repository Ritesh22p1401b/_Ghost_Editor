import graphene
from post_module.types import AuthorType
from users.models import ExtendUser
from post_module.models.author import Author
from django.utils import timezone


class CreateAuthor(graphene.Mutation):
    
    create_author = graphene.Field(AuthorType)
    
    class Arguments:
        id=graphene.Int()
        first_name = graphene.String()
        last_name = graphene.String()
        created_at = graphene.DateTime()
        bio=graphene.String()


    def mutate(self,info,id,first_name ,last_name,bio,**kwargs):
        
        user = ExtendUser.objects.get(pk=id)

        author_create = Author.objects.create(username=user,
            first_name=first_name,
            last_name=last_name,
            created_at=timezone.now(),
            bio=bio
        )
      
        return CreateAuthor(create_author=author_create)

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()

schema = graphene.Schema(mutation=Mutation)