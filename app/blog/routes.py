from app.blog import blog

@blog.route('/entrada/<int:id>')
def entrada(id):
    return f"Titulo de la entrada {id}"