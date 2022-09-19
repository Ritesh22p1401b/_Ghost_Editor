import graphene
from post_module.types import CommentType
from post_module.models.comment import Comment
from post_module.models.post import Post


class CreateComment(graphene.Mutation):
    
    create_comment = graphene.Field(CommentType)
    
    class Arguments:
        post_id = graphene.Int(required=True)
        comment = graphene.String()
        
    @staticmethod
    def mutate(root,info, post_id, comment,**kwargs):
        post = Post.objects.get(id=post_id)
        create_comment = Comment.objects.create(post=post,comment=comment)

        return CreateComment(create_comment=create_comment)

class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()

schema = graphene.Schema(mutation=Mutation)
