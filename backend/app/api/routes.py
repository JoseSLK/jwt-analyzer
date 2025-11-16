"""
Módulo de rutas API para el análisis de JWT.

Define los endpoints REST para el análisis léxico, decodificación, sintactico, y semantico de JWT.
Se aplica como interfaz HTTP para el frontend y clientes externos.
"""

from flask import Blueprint, jsonify, request
from app.analyzer.lexical_analyzer import JWTLexer
from app.analyzer.decoder_json import get_decoded_strings
from app.analyzer.semantic_analyzer import (
    SemanticAnalyzer,
    SemanticError,
    MissingClaimError,
    InvalidDataTypeError,
    InvalidValueError,
    ExpirationDateError,
    NotActiveTokenError
)

api_bp = Blueprint('api', __name__)
jwt_lexer = JWTLexer()
semantic_analyzer = SemanticAnalyzer()

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

@api_bp.route('/analyze/semantic', methods=['POST'])
def analyze_jwt_semantic():
    """
    Endpoint para análisis semántico de JWT.
    
    Recibe header y payload como diccionarios y valida las reglas semánticas.
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No se recibió JSON en el cuerpo de la solicitud'
            }), 400
        
        if 'header' not in data or 'payload' not in data:
            return jsonify({
                'success': False,
                'error': 'El JSON debe contener "header" y "payload" como diccionarios'
            }), 400
        
        header_map = data['header']
        payload_map = data['payload']
        
        if not isinstance(header_map, dict) or not isinstance(payload_map, dict):
            return jsonify({
                'success': False,
                'error': 'Los campos "header" y "payload" deben ser diccionarios'
            }), 400
        
        # Realizar análisis semántico
        result = semantic_analyzer.analyze(header_map, payload_map)
        
        return jsonify({
            'success': True,
            'result': {
                'header': result[0],
                'payload': result[1],
                'valid': True
            }
        })
    except MissingClaimError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': 'MissingClaimError'
        }), 400
    except InvalidDataTypeError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': 'InvalidDataTypeError'
        }), 400
    except InvalidValueError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': 'InvalidValueError'
        }), 400
    except ExpirationDateError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': 'ExpirationDateError'
        }), 400
    except NotActiveTokenError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': 'NotActiveTokenError'
        }), 400
    except SemanticError as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'error_type': 'SemanticError'
        }), 400
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
