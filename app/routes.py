from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Doron'}
    html_page = f'''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, {user['username']} !</h1>
        </body>
    </html>
'''
    return html_page
