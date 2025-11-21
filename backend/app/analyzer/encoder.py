"""
Módulo de codificación y firma para JWT.

Codifica objetos JSON a Base64URL y aplica algoritmos de firma (HS256 o HS384).
Se aplica para generar tokens JWT completos y firmados.
"""

import json
import base64
import hmac
import hashlib
from typing import Dict, Any, Optional


def encode_base64url(data: str) -> str:
    """
    Codifica un string UTF-8 a Base64URL.
    
    Se aplica para convertir strings JSON a formato Base64URL usado en JWT.
    """
    encoded_bytes = data.encode('utf-8')
    base64_bytes = base64.urlsafe_b64encode(encoded_bytes)
    base64_string = base64_bytes.decode('utf-8')
    # Remover padding '=' según especificación Base64URL
    return base64_string.rstrip('=')


def sign_token(header_b64: str, payload_b64: str, algorithm: str, secret: str) -> str:
    """
    Firma un token JWT usando HMAC con el algoritmo especificado.
    
    Recibe header y payload codificados en Base64URL, el algoritmo (HS256 o HS384)
    y la clave secreta. Retorna la firma codificada en Base64URL.
    """
    message = f"{header_b64}.{payload_b64}"
    
    if algorithm == "HS256":
        hash_algorithm = hashlib.sha256
    elif algorithm == "HS384":
        hash_algorithm = hashlib.sha384
    else:
        raise ValueError(f"Algoritmo no soportado: {algorithm}. Solo se soportan HS256 y HS384.")
    
    signature_bytes = hmac.new(
        secret.encode('utf-8'),
        message.encode('utf-8'),
        hash_algorithm
    ).digest()
    
    signature_b64 = base64.urlsafe_b64encode(signature_bytes).decode('utf-8')
    return signature_b64.rstrip('=')


def encode_jwt(header: Dict[str, Any], payload: Dict[str, Any], secret: str = "secret") -> str:
    """
    Codifica y firma un JWT completo.
    
    Recibe header y payload como diccionarios, y una clave secreta.
    Retorna el JWT completo en formato: header.payload.signature
    
    Args:
        header: Diccionario con los claims del header (debe incluir 'alg' y 'typ')
        payload: Diccionario con los claims del payload
        secret: Clave secreta para la firma (por defecto "secret")
    
    Returns:
        String con el JWT completo codificado y firmado
    """
    # Validar que el header tenga 'alg'
    if 'alg' not in header:
        raise ValueError("El header debe contener el claim 'alg'")
    
    algorithm = header['alg']
    
    if algorithm not in ["HS256", "HS384"]:
        raise ValueError(f"Algoritmo no soportado: {algorithm}. Solo se soportan HS256 y HS384.")
    
    # Serializar a JSON compacto (sin espacios)
    header_json = json.dumps(header, separators=(',', ':'))
    payload_json = json.dumps(payload, separators=(',', ':'))
    
    # Codificar a Base64URL
    header_b64 = encode_base64url(header_json)
    payload_b64 = encode_base64url(payload_json)
    
    # Firmar el token
    signature_b64 = sign_token(header_b64, payload_b64, algorithm, secret)
    
    # Construir el JWT completo
    jwt_token = f"{header_b64}.{payload_b64}.{signature_b64}"
    
    return jwt_token

