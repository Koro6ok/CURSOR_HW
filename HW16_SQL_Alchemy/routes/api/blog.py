from app import app, api, db, mail
from flask import render_template, request, Response
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User
from flask_mail import Message


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }

class Articles(Resource):
    def post(self):
        data = request.json
        article = Article(
            author_id=data.get('author_id'),
            title=data.get('title'),
            slug=data.get('slug'),
            description=data.get('description'),
            short_description=data.get('short_description'),
            location=data.get('location'),
            img=data.get('img')
        )
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def get(self):
        articles = Article.query
        if request.args.get('title'):
            articles = articles.filter_by(title=request.args.get('title'))

        # articles = articles.filter(Article.title.startwith('A'))

        if request.args.get("sort_by"):
            articles = articles.order_by(request.args.get("sort_by")).all()


        articles = articles.all()
        serialized_articles = []
        for article in articles:
            serialized_articles.append(article.serialize)

        return serialized_articles

class ArticlesEntity(Resource):
    def get(self, id):
        article = Article.query.get(id)
        if article == None:
            return Response(status=404)
        return article.serialize

    def delete(self, id):
        article = Article.query.filter_by(id=id)

        if article == None:
            return Response(status=404)

        article.delete()
        db.session.commit()

        return Response (status=204)




class Users(Resource):
    def get(self):
        user = User.query.get(1)
        serialized_articles = []
        for article in user.articles:
            print(article)
            serialized_articles.append(article.serialize)
        return serialized_articles


class UsersRead(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user == None:
            return Response(status=404)
        serialized_articles = []
        for article in user.articles:
            print(article)
            serialized_articles.append(article.serialize)
        serialized_user = [user.serialize, serialized_articles]
        return serialized_user



class UsersUpdate(Resource):
    def post(self, id):
        user = User.query.get(id)
        data = request.json
        user.username = data.get('username')
        user.password = data.get('password')
        user.email = data.get('email'),
        user.created = data.get('created'),
        user.bio = data.get('bio'),
        user.admin = data.get('admin'),
        user.location = data.get('location')


        db.session.add(user)
        db.session.commit()
        return user.serialize



class UsersCreate(Resource):
    def post(self):
        data = request.json
        user = User(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
            created=data.get('created'),
            bio=data.get('bio'),
            admin=data.get('admin'),
            location=data.get('location')
        )
        db.session.add(user)
        db.session.commit()
        return user.serialize


class Contact(Resource):
    def post(self):
        data = request.json
        msg = Message('Contact form alert', sender='curses.test@gmail.com', recipients=['korobchuk.aleksandr@gmail.com'])
        msg.html = "Contact Email: " + data['email'] + "<br>" + "Contact Title: " + data['title'] + "<br>" + "Contact Description: " + data['description'] + "<br>" + "This message from 'contact us' form"
        mail.send(msg)
        client_msg = Message('Dear Client!', sender='curses.test@gmail.com', recipients=[data['email']])
        client_msg.html = render_template("blog/emails/contact.html", email=data['email'])
        mail.send(client_msg)
        return Response(status=200)




class FooterItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.FOOTER_LINKS
        }


api.add_resource(MenuItem, '/api/menu-items')
api.add_resource(Articles, '/api/articles')
api.add_resource(ArticlesEntity, '/api/articles/<int:id>')
api.add_resource(Users, '/api/users')
api.add_resource(UsersRead, '/api/users/read/<int:id>')
api.add_resource(UsersUpdate, '/api/users/update/<int:id>')
api.add_resource(UsersCreate, '/api/users/create')
api.add_resource(Contact, '/api/contact')
api.add_resource(FooterItem, '/api/footer-items')