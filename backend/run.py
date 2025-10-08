from flask import Flask
from app.api.routes import api_bp

def create_app():
    """Factory function to create Flask app instance"""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'amarillo-platano'
    app.config['DEBUG'] = True
    
    # Register blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
