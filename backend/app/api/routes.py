"""
Módulo de rutas API para el análisis de JWT.

Define los endpoints REST para el análisis léxico, decodificación, sintactico, y semantico de JWT.
Se aplica como interfaz HTTP para el frontend y clientes externos.
"""

from flask import Blueprint, jsonify, request
from app.analyzer.lexical_analyzer import JWTLexer
from app.analyzer.decoder_json import get_decoded_strings

api_bp = Blueprint('api', __name__)
jwt_lexer = JWTLexer()

@api_bp.route('/analyze/lexical/<string:jwt>', methods=['GET'])
def analyze_jwt(jwt):
    """
    Endpoint para análisis léxico de JWT.
    
    Recibe un JWT en la URL y retorna el resultado del análisis léxico (Fase 1).
    Se aplica como primer paso en el proceso de análisis de JWT.
    """
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

@api_bp.route('/analyze/decoder', methods=['POST'])
def analyze_jwt_decoder():
    """
    Endpoint para decodificación de JWT.
    
    Recibe el resultado del análisis léxico en el cuerpo (JSON) y retorna
    los strings JSON decodificados del header y payload. Se aplica después
    del análisis léxico (Fase 1) para obtener los JSON decodificados (Fase 4).
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No se recibió JSON en el cuerpo de la solicitud'
            }), 400
        
        if not isinstance(data, dict) or 'header' not in data or 'payload' not in data:
            return jsonify({
                'success': False,
                'error': 'El JSON debe contener el resultado del análisis léxico con "header" y "payload"'
            }), 400
        
        result = get_decoded_strings(data)
        
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
    """
    Endpoint de verificación de salud de la API.
    
    Retorna el estado de la API. Se aplica para monitoreo y verificación
    de que el servicio está en funcionamiento.
    """
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
    })
