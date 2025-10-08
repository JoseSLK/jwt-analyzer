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

### Análisis de JWT
- **GET** `/api/analyze/{jwt_token}`
- Analiza un token JWT y retorna sus componentes

**Ejemplo:**
```
GET http://localhost:5000/api/analyze/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ.XM-XSs2Lmp76IcTQ7tVdFcZzN4W_WcoKMNANp925Q9g
```

**Respuesta:**
```json
{
    "success": true,
    "result": {
        "valid": true,
        "tokens": ["header", "payload", "signature"],
        "header": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        "payload": "eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ",
        "signature": "XM-XSs2Lmp76IcTQ7tVdFcZzN4W_WcoKMNANp925Q9g"
    }
}
```