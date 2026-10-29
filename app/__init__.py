from flask import Flask

def create_app():
    app = Flask(__name__)
    # Registro de los blueprints (Modulos)
    from app.usuarios.routes import usuarios_bp
    from app.productos.routes import productos_bp
    from app.auth.routes import auth_bp
    from app.admin import admin
    from app.blog import blog
    
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin)
    app.register_blueprint(blog)
    
    return app