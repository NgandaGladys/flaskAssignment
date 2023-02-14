from flask import Flask,jsonify
#creating an instance
app=Flask(__name__)
#creating a route
@app.route('/')
def hello_world():
    return "<p>Here are the articles</p>"

@app.route("/articles", methods=['GET'])
#defining a function
def getArticles():
    articles={
        'article1':{
            'id':1,
            'title':'Who is a programmer',
            'body':'Simply a person who writes computer programmes',
            'author':'Pearl Jordans'
            },
        
        'article2':{
             'id':2,
             'title':'Programming languages',
             'body':'There are various languages such as C\tC++\tPython\tJavaScript etc',
             'author':'Ella Richards'
             },
        'article3':{
            'id':3,
            'title':'Starting with HTML and CSS',
            'body':'These are the best languages for starters',
            'author':'Emma Robbtison'
            },
        'article4':{
            'id':4,
            'title':'Advantages of Css',
            'body':'it\'s main function is to style your HTML for a good visual impression',
            'author':'Christina Adams'
            },
        'article5':{
            'id':5,
            'title':'Deep into programming',
            'body':'We shall be introduced to other languages such as JavaScript and React which are more dynamic',
            'author':'Sherry Partson'
            },
        'article6':{
            'id':6,
            'title':'what about JavaScript',
            'body':'Js is fun\t more interractive and can be used to change our HTML elements',
            'author':'Glad Amanda'
            }
    }
    return jsonify(articles)
if __name__=='main':
    app.run(debug=True)    


