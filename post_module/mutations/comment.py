import graphene
from post_module.types import CommentType
from post_module.models.comment import Comment
from post_module.models.post import Post


class CreateComment(graphene.Mutation):
    
    create_comment = graphene.Field(CommentType)
    
    class Arguments:
        post_id = graphene.Int(required=True)
        comment = graphene.String()
        
    
    def mutate(self,info, post_id, comment,**kwargs):
        post = Post.objects.get(id=post_id)
        create_comment = Comment.objects.create(post=post,comment=comment)

        return CreateComment(create_comment=create_comment)

class DeleteComment(graphene.Mutation):
    
    comment_id = graphene.Int()
    
    class Arguments:
        comment_id = graphene.Int(required=True)
        
    def mutate(self,info,comment_id):
        
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return DeleteComment(comment_id=comment_id)


class Mutation(graphene.ObjectType):
    create_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()

schema = graphene.Schema(mutation=Mutation)