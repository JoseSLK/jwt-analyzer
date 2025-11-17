# JWT Analyzer - Backend

Backend API para análisis de tokens JWT desarrollado con Flask.

## Requisitos

- Python 3.7+
- pip

## Instalación y Ejecución

### 1. Crear entorno virtual
```bash
cd backend
python -m venv venv
```

### 2. Activar entorno virtual

**Windows:**
```bash
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python run.py
```

La aplicación estará disponible en: `http://localhost:5000`

## Endpoints Disponibles

### Health Check
- **GET** `/api/health`
- Verifica que la API esté funcionando

**Respuesta:**
```json
{
    "status": "healthy",
    "message": "API is running"
}
```

### Análisis Léxico de JWT
- **GET** `/api/analyze/lexical/<jwt_token>`
- Analiza un token JWT y valida su formato léxico (Fase 1)
- Retorna los componentes separados del JWT (header, payload, signature)

### Decodificación de JWT
- **POST** `/api/analyze/decoder`
- Decodifica los tokens Base64URL del header y payload a strings JSON (Fase 4)
- Recibe el resultado del análisis léxico en el cuerpo de la solicitud

**Nota:** El resultado es un array con dos elementos:
- `result[0]`: Header decodificado en formato JSON string
- `result[1]`: Payload decodificado en formato JSON string

Para ver ejemplos de uso y casos de prueba, consulta [EJEMPLOS.md](EJEMPLOS.md).

### Análisis Sintáctico de JWT
- **POST** `/api/analyze/syntactic`
- Analiza la estructura interna del *header* y *payload* decodificados (Fase 5).
- Verifica que ambos componentes correspondan a objetos JSON válidos y que cumplan con la estructura mínima requerida por el estándar JWT.

El analizador realiza las siguientes validaciones:

- Que el **header** sea un diccionario JSON válido.
- Que exista el campo **`typ`** y que su valor sea **exactamente `"JWT"`**.  
  - Si no coincide, se genera un **error fatal** y el análisis se marca como inválido.
- Que exista el campo **`alg`** y que su valor sea un string válido.
- Que el **payload** sea un diccionario JSON válido.
- Que no existan errores de sintaxis en ninguno de los dos segmentos.

**Salida del Analizador Sintáctico**

El analizador retorna un objeto con:

```json
{
  "valid": true | false,
  "errors": ["lista de errores si existen"],
  "header": { "diccionario con el contenido del header" },
  "payload": { "diccionario con el contenido del payload" }
}


## Flujo de Uso

1. **Paso 1:** Realizar análisis léxico del JWT usando `/api/analyze/lexical/<jwt_token>`
2. **Paso 2:** Tomar el `result` de la respuesta y enviarlo al endpoint `/api/analyze/decoder` como body
3. **Paso 3:** Obtener los strings JSON decodificados para análisis posterior