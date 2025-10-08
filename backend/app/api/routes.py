from flask import Blueprint, jsonify, request
from app.analyzer.lexical_analyzer import JWTLexer

# Create blueprint
api_bp = Blueprint('api', __name__)

# Initialize service
jwt_lexer = JWTLexer()

@api_bp.route('/analyze/<string:jwt>', methods=['GET'])
def analyze_jwt(jwt):
    try:
        result = jwt_lexer.analyze(jwt)
        return jsonify({
            'success': True,
            'result': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
    })
