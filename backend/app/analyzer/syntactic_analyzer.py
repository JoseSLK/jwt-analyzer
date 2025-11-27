# me llega un arreglo de 2 string, el primer string con el header y el seguindo array de string el payload (devuelto por el decoder)
# verficio un JSON valido y devuelvo un diccionario con los datos del payload.
# hago una validacion de estructuras 


# -*- coding: utf-8 -*-
"""
ANALIZADOR SINTÁCTICO (PROYECTO JWT)
-----------------------------------------------------------
Incluye:
- Parser JSON manual basado en la GLC (único método de parsing).
- Validaciones estructurales del header y payload.
- typ != "JWT" tratado como error fatal.
"""

class JSONParseError(Exception):
    pass

class JSONParser:
    def __init__(self, text):
        # Inicializa el parser con el texto JSON a analizar
        # self.i es el índice que marca la posición actual en el texto
        self.text = text
        self.i = 0

    def skip_ws(self):
        # Avanza el índice saltando todos los espacios en blanco (espacios, tabs, saltos de línea)
        # Esto permite que el parser ignore los espacios entre tokens
        while self.i < len(self.text) and self.text[self.i] in " \n\t\r":
            self.i += 1

    def peek(self):
        # Obtiene el siguiente carácter sin avanzar el índice
        # Primero salta espacios en blanco, luego retorna el carácter actual o None si llegó al final
        self.skip_ws()
        if self.i < len(self.text):
            return self.text[self.i]
        return None

    def parse(self):
        # Función principal que inicia el parsing del JSON
        # Parsea un valor JSON y verifica que no quede texto extra después
        value = self.parse_value()
        self.skip_ws()
        if self.i != len(self.text):
            raise JSONParseError("Texto extra después del JSON.")
        return value

    def parse_value(self):
        # Función central que determina qué tipo de valor JSON se está parseando
        # Analiza el primer carácter para decidir si es string, objeto, array, número, booleano o null
        # Luego delega el parsing específico a la función correspondiente
        self.skip_ws()
        c = self.peek()
        if c is None:
            raise JSONParseError("EOF inesperado.")
        if c == '"': return self.parse_string()  # Si empieza con comillas, es un string
        if c == '{': return self.parse_object()  # Si empieza con llave, es un objeto
        if c == '[': return self.parse_array()   # Si empieza con corchete, es un array
        if c.isdigit() or c == '-': return self.parse_number()  # Si es dígito o signo menos, es un número
        if self.text.startswith("true", self.i):  # Palabra reservada true
            self.i += 4
            return True
        if self.text.startswith("false", self.i):  # Palabra reservada false
            self.i += 5
            return False
        if self.text.startswith("null", self.i):  # Palabra reservada null
            self.i += 4
            return None
        raise JSONParseError("Token inesperado en value: " + c)

    def parse_string(self):
        # Parsea un string JSON: lee caracteres entre comillas dobles
        # Maneja secuencias de escape como \n, \t, \r, \uXXXX (Unicode), y caracteres especiales
        self.skip_ws()
        if self.peek() != '"':
            raise JSONParseError("Se esperaba inicio de string.")
        self.i += 1  # Avanza después de la comilla inicial
        out = ""
        while self.i < len(self.text):
            c = self.text[self.i]
            if c == '"':  # Comilla de cierre encontrada
                self.i += 1
                return out
            if c == '\\':  # Secuencia de escape encontrada
                if self.i + 1 >= len(self.text):
                    raise JSONParseError("Escape incompleto.")
                nxt = self.text[self.i+1]
                if nxt in ['"', '\\', '/']:  # Caracteres escapados simples
                    out += nxt
                    self.i += 2
                elif nxt == 'n':  # Nueva línea
                    out += '\n'; self.i += 2
                elif nxt == 't':  # Tab
                    out += '\t'; self.i += 2
                elif nxt == 'r':  # Retorno de carro
                    out += '\r'; self.i += 2
                elif nxt == 'u':  # Secuencia Unicode \uXXXX
                    hexv = self.text[self.i+2:self.i+6]
                    if len(hexv) < 4:
                        raise JSONParseError("Unicode incompleto.")
                    out += chr(int(hexv, 16))  # Convierte hexadecimal a carácter
                    self.i += 6
                else:
                    raise JSONParseError("Escape inválido.")
            else:
                out += c; self.i += 1  # Carácter normal, se agrega al resultado
        raise JSONParseError("String no cerrado.")

    def parse_number(self):
        # Parsea un número JSON: puede ser entero o decimal, positivo o negativo
        # Lee dígitos opcionales después del signo menos, luego punto decimal y más dígitos
        self.skip_ws()
        start = self.i  # Guarda la posición inicial para extraer el número completo
        if self.peek() == '-': self.i += 1  # Maneja signo negativo opcional
        if not self.peek() or not self.peek().isdigit():
            raise JSONParseError("Número inválido.")
        while self.peek() and self.peek().isdigit():  # Lee la parte entera
            self.i += 1
        if self.peek() == '.':  # Si hay punto, es un número decimal
            self.i += 1
            if not self.peek() or not self.peek().isdigit():
                raise JSONParseError("Decimal inválido.")
            while self.peek() and self.peek().isdigit():  # Lee la parte decimal
                self.i += 1
        num_str = self.text[start:self.i]  # Extrae el string del número
        try:
            if '.' in num_str:
                return float(num_str)  # Convierte a float si tiene punto decimal
            return int(num_str)  # Convierte a int si es entero
        except:
            raise JSONParseError("Número mal formado.")

    def parse_object(self):
        # Parsea un objeto JSON: conjunto de pares clave-valor entre llaves {}
        # Formato: {"clave1": valor1, "clave2": valor2, ...}
        # Maneja objetos vacíos {} y objetos con múltiples propiedades
        self.skip_ws()
        if self.peek() != '{': raise JSONParseError("Se esperaba '{'.")
        self.i += 1  # Avanza después de la llave de apertura
        obj = {}
        self.skip_ws()
        if self.peek() == '}':  # Objeto vacío
            self.i += 1
            return obj
        while True:  # Bucle para leer todas las propiedades
            key = self.parse_string()  # Parsea la clave (debe ser string)
            self.skip_ws()
            if self.peek() != ':': raise JSONParseError("Se esperaba ':'.")
            self.i += 1  # Avanza después de los dos puntos
            val = self.parse_value()  # Parsea el valor (puede ser cualquier tipo JSON)
            obj[key] = val  # Almacena el par clave-valor en el diccionario
            self.skip_ws()
            if self.peek() == '}':  # Si encuentra llave de cierre, termina
                self.i += 1
                break
            if self.peek() != ',': raise JSONParseError("Se esperaba ',' o '}'.")
            self.i += 1  # Avanza después de la coma para leer la siguiente propiedad
        return obj

    def parse_array(self):
        # Parsea un array JSON: lista de valores entre corchetes []
        # Formato: [valor1, valor2, valor3, ...]
        # Maneja arrays vacíos [] y arrays con múltiples elementos
        self.skip_ws()
        if self.peek() != '[': raise JSONParseError("Se esperaba '['.")
        self.i += 1  # Avanza después del corchete de apertura
        arr = []
        self.skip_ws()
        if self.peek() == ']':  # Array vacío
            self.i += 1
            return arr
        while True:  # Bucle para leer todos los elementos
            arr.append(self.parse_value())  # Parsea cada valor y lo agrega al array
            self.skip_ws()
            if self.peek() == ']':  # Si encuentra corchete de cierre, termina
                self.i += 1
                break
            if self.peek() != ',': raise JSONParseError("Se esperaba ',' o ']'.")
            self.i += 1  # Avanza después de la coma para leer el siguiente elemento
        return arr


def parse_json_manual(text):
    # Función pública que inicia el parsing de un string JSON
    # Crea una instancia del parser y ejecuta el método parse() para obtener el resultado
    return JSONParser(text).parse()


def analyze_syntax(header_str, payload_str):
    # Función principal del analizador sintáctico para JWT
    # Realiza dos fases: parsing JSON y validación estructural
    result = {"success": True, "valid": False, "header": None, "payload": None, "errors": []}

    # FASE 1: PARSE HEADER
    # Usa el parser manual para convertir el string JSON del header en un diccionario Python
    try:
        header = parse_json_manual(header_str)
    except JSONParseError as e:
        result["errors"].append("Header inválido (error de parsing): " + str(e))
        return result
    except Exception as e:
        result["errors"].append("Header inválido: " + str(e))
        return result

    # FASE 2: PARSE PAYLOAD
    # Usa el parser manual para convertir el string JSON del payload en un diccionario Python
    try:
        payload = parse_json_manual(payload_str)
    except JSONParseError as e:
        result["errors"].append("Payload inválido (error de parsing): " + str(e))
        return result
    except Exception as e:
        result["errors"].append("Payload inválido: " + str(e))
        return result

    result["header"] = header
    result["payload"] = payload

    # FASE 3: VALIDACIONES ESTRUCTURALES
    # Verifica que header y payload sean objetos JSON (diccionarios)
    if not isinstance(header, dict):
        result["errors"].append("Header debe ser objeto JSON.")
    if not isinstance(payload, dict):
        result["errors"].append("Payload debe ser objeto JSON.")

    # Valida que el header contenga los claims obligatorios 'alg' y 'typ'
    if "alg" not in header:
        result["errors"].append("Header faltante 'alg'.")
    if "typ" not in header:
        result["errors"].append("Header faltante 'typ'.")
    else:
        # Valida que 'typ' sea exactamente "JWT" (error fatal si no coincide)
        if header["typ"] != "JWT":
            result["errors"].append("Header 'typ' debe ser exactamente 'JWT' (FATAL).")

    # Valida que los claims de tiempo (iat, exp, nbf) sean enteros si están presentes
    for t in ("iat", "exp", "nbf"):
        if t in payload and not isinstance(payload[t], int):
            result["errors"].append(f"Claim '{t}' debe ser entero.")

    # Valida que 'aud' (audience) sea string o lista de strings
    if "aud" in payload:
        aud = payload["aud"]
        if isinstance(aud, list):
            if not all(isinstance(x, str) for x in aud):
                result["errors"].append("Claim 'aud' debe ser lista de strings.")
        elif not isinstance(aud, str):
            result["errors"].append("Claim 'aud' debe ser string o lista.")

    # Valida que 'permissions' sea una lista de strings
    if "permissions" in payload:
        perms = payload["permissions"]
        if not (isinstance(perms, list) and all(isinstance(p, str) for p in perms)):
            result["errors"].append("Claim 'permissions' debe ser lista de strings.")

    # Si no hay errores, marca el resultado como válido
    if not result["errors"]:
        result["valid"] = True

    return result
