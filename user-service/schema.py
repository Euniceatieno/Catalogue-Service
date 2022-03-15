from models import UserData
from resolvers import login 
from resolvers import signup 
import graphene

class Login(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    response = graphene.String()

    def mutate(root, email, password):
        return Login(response=login(email, password))


class Signup(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    response = graphene.String()

    def mutate(root,email, password):
        return Signup(response=signup(email, password))


class User(graphene.ObjectType):
    email = graphene.String()
    password = graphene.String()


class MyMutations(graphene.ObjectType):
    login = Login.Field()
    signup = Signup.Field()


class MyQueries(graphene.ObjectType):
    user = graphene.Field(User)


schema = graphene.Schema(query=MyQueries, mutation=MyMutations, types=[User])