import graphene
from post_module.types import TagType
from post_module.models.tags import Tag


class CreateTag(graphene.Mutation):

    create_tag = graphene.Field(TagType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(root,info, name):
        name=Tag.objects.create(name=name)

        return CreateTag(create_tag=name) 


class Mutation(graphene.ObjectType):
    create_tag = CreateTag.Field()

schema = graphene.Schema(mutation=Mutation)
