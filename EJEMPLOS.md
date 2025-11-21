# Ejemplos de Casos de Prueba

## Caso 1: JWT Básico

**JWT:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ.XM-XSs2Lmp76IcTQ7tVdFcZzN4W_WcoKMNANp925Q9g
```

**Respuesta Análisis Léxico:**
```json
{
    "success": true,
    "result": {
        "valid": true,
        "tokens": [
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            "eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ",
            "XM-XSs2Lmp76IcTQ7tVdFcZzN4W_WcoKMNANp925Q9g"
        ],
        "header": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        "payload": "eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ",
        "signature": "XM-XSs2Lmp76IcTQ7tVdFcZzN4W_WcoKMNANp925Q9g"
    }
}
```

**Respuesta Decoder:**
```json
{
    "success": true,
    "result": [
        "{\"alg\":\"HS256\",\"typ\":\"JWT\"}",
        "{\"sub\":\"foo\",\"name\":\"John Doe\"}"
    ]
}
```



**Respuesta Analyzador Syntactico:**
```json

{
  "success": true,
  "valid": true,
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "foo",
    "name": "John Doe"
  },
  "errors": []
}


```

**Respuesta Analyzador Semantico:**
```json
{
  "success": true,
  "result": {
    "header": {
      "alg": "HS256",
      "typ": "JWT"
    },
    "payload": {
      "sub": "foo",
      "name": "John Doe"
    },
    "valid": true
  }
}
```

## Caso 2: JWT con Usuario Admin

**JWT:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5taS1wcm95ZWN0by5jb20iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkwIiwiYXVkIjoiaHR0cHM6Ly9hcGkubWktcHJveWVjdG8uY29tL3YxIiwiaWF0IjoxNzYyOTU2MDAwLCJleHAiOjE3NjI5NTk2MDAsIm5iZiI6MTc2Mjk1NjAwMCwianRpIjoiYWJjLWRlZi0xMjMiLCJ1c2VybmFtZSI6Impvc2Uuc2FsYW1hbmNhIiwicm9sZSI6ImFkbWluIn0.Vq2-vG1A-PzX3Yy_G-m-9S-k4_x-D2k-c6y-T-M8_Vw
```

**Respuesta Análisis Léxico:**
```json
{
    "result": {
        "header": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        "payload": "eyJpc3MiOiJodHRwczovL2FwaS5taS1wcm95ZWN0by5jb20iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkwIiwiYXVkIjoiaHR0cHM6Ly9hcGkubWktcHJveWVjdG8uY29tL3YxIiwiaWF0IjoxNzYyOTU2MDAwLCJleHAiOjE3NjI5NTk2MDAsIm5iZiI6MTc2Mjk1NjAwMCwianRpIjoiYWJjLWRlZi0xMjMiLCJ1c2VybmFtZSI6Impvc2Uuc2FsYW1hbmNhIiwicm9sZSI6ImFkbWluIn0",
        "signature": "Vq2-vG1A-PzX3Yy_G-m-9S-k4_x-D2k-c6y-T-M8_Vw",
        "tokens": [
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            "eyJpc3MiOiJodHRwczovL2FwaS5taS1wcm95ZWN0by5jb20iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkwIiwiYXVkIjoiaHR0cHM6Ly9hcGkubWktcHJveWVjdG8uY29tL3YxIiwiaWF0IjoxNzYyOTU2MDAwLCJleHAiOjE3NjI5NTk2MDAsIm5iZiI6MTc2Mjk1NjAwMCwianRpIjoiYWJjLWRlZi0xMjMiLCJ1c2VybmFtZSI6Impvc2Uuc2FsYW1hbmNhIiwicm9sZSI6ImFkbWluIn0",
            "Vq2-vG1A-PzX3Yy_G-m-9S-k4_x-D2k-c6y-T-M8_Vw"
        ],
        "valid": true
    },
    "success": true
}
```

**Respuesta Decoder:**
```json
{
    "result": [
        "{\"alg\":\"HS256\",\"typ\":\"JWT\"}",
        "{\"iss\":\"https://api.mi-proyecto.com\",\"sub\":\"auth0|1234567890\",\"aud\":\"https://api.mi-proyecto.com/v1\",\"iat\":1762956000,\"exp\":1762959600,\"nbf\":1762956000,\"jti\":\"abc-def-123\",\"username\":\"jose.salamanca\",\"role\":\"admin\"}"
    ],
    "success": true
}
```


**Respuesta Analyzador Syntactico:**
```json

{
  "success": true,
  "valid": true,
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "iss": "https://api.mi-proyecto.com",
    "sub": "auth0|1234567890",
    "aud": "https://api.mi-proyecto.com/v1",
    "iat": 1762956000,
    "exp": 1762959600,
    "nbf": 1762956000,
    "jti": "abc-def-123",
    "username": "jose.salamanca",
    "role": "admin"
  },
  "errors": []
}



```

**Respuesta Analyzador Semantico:**
```json
{
  "success": true,
  "result": {
    "header": {
      "alg": "HS256",
      "typ": "JWT"
    },
    "payload": {
      "iss": "https://api.mi-proyecto.com",
      "sub": "auth0|1234567890",
      "aud": "https://api.mi-proyecto.com/v1",
      "iat": 1762956000,
      "exp": 1762959600,
      "nbf": 1762956000,
      "jti": "abc-def-123",
      "username": "jose.salamanca",
      "role": "admin"
    },
    "valid": true
  }
}
```



## Caso 3: JWT con Usuario Regular

**JWT:**
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5taS1wcm95ZWN0by5jb20iLCJzdWIiOiJhdXRoMHwwOTg3NjU0MzIxIiwiYXVkIjoiaHR0cHM6Ly9hcGkubWktcHJveWVjdG8uY29tL3YxIiwiaWF0IjoxNzYyOTQ4ODAwLCJleHAiOjE3NjI5NTI0MDAsIm5iZiI6MTc2Mjk0ODgwMCwianRpIjoiZ2hpLWprbC00NTYiLCJ1c2VybmFtZSI6InNhbXVlbC51c2VyIiwicm9sZSI6InVzZXIifQ.J-Z_y_T-B_J-d_v-E_c-g_g-V_l-f_j-M_v-r_y-B_Q
```

**Respuesta Análisis Léxico:**
```json
{
    "result": {
        "header": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
        "payload": "eyJpc3MiOiJodHRwczovL2FwaS5taS1wcm95ZWN0by5jb20iLCJzdWIiOiJhdXRoMHwwOTg3NjU0MzIxIiwiYXVkIjoiaHR0cHM6Ly9hcGkubWktcHJveWVjdG8uY29tL3YxIiwiaWF0IjoxNzYyOTQ4ODAwLCJleHAiOjE3NjI5NTI0MDAsIm5iZiI6MTc2Mjk0ODgwMCwianRpIjoiZ2hpLWprbC00NTYiLCJ1c2VybmFtZSI6InNhbXVlbC51c2VyIiwicm9sZSI6InVzZXIifQ",
        "signature": "J-Z_y_T-B_J-d_v-E_c-g_g-V_l-f_j-M_v-r_y-B_Q",
        "tokens": [
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
            "eyJpc3MiOiJodHRwczovL2FwaS5taS1wcm95ZWN0by5jb20iLCJzdWIiOiJhdXRoMHwwOTg3NjU0MzIxIiwiYXVkIjoiaHR0cHM6Ly9hcGkubWktcHJveWVjdG8uY29tL3YxIiwiaWF0IjoxNzYyOTQ4ODAwLCJleHAiOjE3NjI5NTI0MDAsIm5iZiI6MTc2Mjk0ODgwMCwianRpIjoiZ2hpLWprbC00NTYiLCJ1c2VybmFtZSI6InNhbXVlbC51c2VyIiwicm9sZSI6InVzZXIifQ",
            "J-Z_y_T-B_J-d_v-E_c-g_g-V_l-f_j-M_v-r_y-B_Q"
        ],
        "valid": true
    },
    "success": true
}
```

**Respuesta Decoder:**
```json
{
    "result": [
        "{\"alg\":\"HS256\",\"typ\":\"JWT\"}",
        "{\"iss\":\"https://api.mi-proyecto.com\",\"sub\":\"auth0|0987654321\",\"aud\":\"https://api.mi-proyecto.com/v1\",\"iat\":1762948800,\"exp\":1762952400,\"nbf\":1762948800,\"jti\":\"ghi-jkl-456\",\"username\":\"samuel.user\",\"role\":\"user\"}"
    ],
    "success": true
}
```


**Respuesta Analyzador Syntactico:**
```json

{
    "success": true,
    "valid": true,
    "header": {
        "alg": "HS256",
        "typ": "JWT"
    },
    "payload": {
        "iss": "https://api.mi-proyecto.com",
        "sub": "auth0|0987654321",
        "aud": "https://api.mi-proyecto.com/v1",
        "iat": 1762948800,
        "exp": 1762952400,
        "nbf": 1762948800,
        "jti": "ghi-jkl-456",
        "username": "samuel.user",
        "role": "user"
    },
    "errors": []
}


```

**Respuesta Analyzador Semantico:**
```json
{
  "success": true,
  "result": {
    "header": {
      "alg": "HS256",
      "typ": "JWT"
    },
    "payload": {
      "iss": "https://api.mi-proyecto.com",
      "sub": "auth0|0987654321",
      "aud": "https://api.mi-proyecto.com/v1",
      "iat": 1762948800,
      "exp": 1762952400,
      "nbf": 1762948800,
      "jti": "ghi-jkl-456",
      "username": "samuel.user",
      "role": "user"
    },
    "valid": true
  }
}
```



## Caso 4: JWT con HS384 y Permisos

**JWT:**
```
eyJhbGciOiJIU380IiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2F1dGgubWktcHJveWVjdG8uY29tIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyMzM0NDU1IiwiYXVkIjpbImh0dHBzOi8vYXBpLm1pLXByb3llY3RvLmNvbS92MSIsImh0dHBzOi8vYWRtaW4ubWktcHJveWVjdG8uY29tIl0sImlhdCI6MTc2Mjk1NjAwMCwiZXhwIjoxNzYyOTU5NjAwLCJqdGkiOiJtbm8tcHFyLTc4OSIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20iLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmRhdGEiLCJ3cml0ZTpkYXRhIl19.K-i-h_j-J_y-k_w-s_v-q_v-H_P-C_T-S_V-W_Y-v_P-H_w-y_k-L_o-X_m
```

**Respuesta Análisis Léxico:**
```json
{
    "result": {
        "header": "eyJhbGciOiJIU380IiwidHlwIjoiSldUIn0",
        "payload": "eyJpc3MiOiJodHRwczovL2F1dGgubWktcHJveWVjdG8uY29tIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyMzM0NDU1IiwiYXVkIjpbImh0dHBzOi8vYXBpLm1pLXByb3llY3RvLmNvbS92MSIsImh0dHBzOi8vYWRtaW4ubWktcHJveWVjdG8uY29tIl0sImlhdCI6MTc2Mjk1NjAwMCwiZXhwIjoxNzYyOTU5NjAwLCJqdGkiOiJtbm8tcHFyLTc4OSIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20iLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmRhdGEiLCJ3cml0ZTpkYXRhIl19",
        "signature": "K-i-h_j-J_y-k_w-s_v-q_v-H_P-C_T-S_V-W_Y-v_P-H_w-y_k-L_o-X_m",
        "tokens": [
            "eyJhbGciOiJIU380IiwidHlwIjoiSldUIn0",
            "eyJpc3MiOiJodHRwczovL2F1dGgubWktcHJveWVjdG8uY29tIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyMzM0NDU1IiwiYXVkIjpbImh0dHBzOi8vYXBpLm1pLXByb3llY3RvLmNvbS92MSIsImh0dHBzOi8vYWRtaW4ubWktcHJveWVjdG8uY29tIl0sImlhdCI6MTc2Mjk1NjAwMCwiZXhwIjoxNzYyOTU5NjAwLCJqdGkiOiJtbm8tcHFyLTc4OSIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20iLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmRhdGEiLCJ3cml0ZTpkYXRhIl19",
            "K-i-h_j-J_y-k_w-s_v-q_v-H_P-C_T-S_V-W_Y-v_P-H_w-y_k-L_o-X_m"
        ],
        "valid": true
    },
    "success": true
}
```

**Respuesta Decoder:**
```json
{
    "result": [
        "{\"alg\":\"HS384\",\"typ\":\"JWT\"}",
        "{\"iss\":\"https://auth.mi-proyecto.com\",\"sub\":\"google-oauth2|1122334455\",\"aud\":[\"https://api.mi-proyecto.com/v1\",\"https://admin.mi-proyecto.com\"],\"iat\":1762956000,\"exp\":1762959600,\"jti\":\"mno-pqr-789\",\"email\":\"test@gmail.com\",\"permissions\":[\"read:data\",\"write:data\"]}"
    ],
    "success": true
}
```


**Respuesta Analyzador Syntactico:**
```json
{
  "success": true,
  "valid": true,
  "header": {
    "alg": "HS384",
    "typ": "JWT"
  },
  "payload": {
    "iss": "https://auth.mi-proyecto.com",
    "sub": "google-oauth2|1122334455",
    "aud": [
      "https://api.mi-proyecto.com/v1",
      "https://admin.mi-proyecto.com"
    ],
    "iat": 1762956000,
    "exp": 1762959600,
    "jti": "mno-pqr-789",
    "email": "test@gmail.com",
    "permissions": [
      "read:data",
      "write:data"
    ]
  },
  "errors": []
}


```

**Respuesta Analyzador Semantico:**
```json
{
  "success": true,
  "result": {
    "header": {
      "alg": "HS384",
      "typ": "JWT"
    },
    "payload": {
      "iss": "https://auth.mi-proyecto.com",
      "sub": "google-oauth2|1122334455",
      "aud": [
        "https://api.mi-proyecto.com/v1",
        "https://admin.mi-proyecto.com"
      ],
      "iat": 1762956000,
      "exp": 1762959600,
      "jti": "mno-pqr-789",
      "email": "test@gmail.com",
      "permissions": [
        "read:data",
        "write:data"
      ]
    },
    "valid": true
  }
}
```

---

## Ejemplos de Verificación Criptográfica

### Caso 1: Verificación Exitosa (HS256)

**Request:**
```json
POST /api/analyze/crypto-verification
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ.ka6DdIKip4EhcQ6vmyywTlebCmE9ZmgCyOFct9Pxgk8",
  "secret": "secret"
}
```

**Respuesta:**
```json
{
  "success": true,
  "valid": true,
  "algorithm": "HS256",
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "foo",
    "name": "John Doe"
  }
}
```

### Caso 2: Verificación Exitosa (HS384)

**Request:**
```json
POST /api/analyze/crypto-verification
{
  "jwt": "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGgubWktcHJveWVjdG8uY29tIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyMzM0NDU1IiwiYXVkIjpbImh0dHBzOi8vYXBpLm1pLXByb3llY3RvLmNvbS92MSIsImh0dHBzOi8vYWRtaW4ubWktcHJveWVjdG8uY29tIl0sImlhdCI6MTc2Mjk1NjAwMCwiZXhwIjoxNzYyOTU5NjAwLCJqdGkiOiJtbm8tcHFyLTc4OSIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20iLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmRhdGEiLCJ3cml0ZTpkYXRhIl19.4-9i05RdPrJGV9WT8cK7czn-g--wt5w4nQYXomJkW3U5UTekXPNrkY0ftH8vjJ9w",
  "secret": "another-secret-key"
}
```

**Respuesta:**
```json
{
  "success": true,
  "valid": true,
  "algorithm": "HS384",
  "header": {
    "alg": "HS384",
    "typ": "JWT"
  },
  "payload": {
    "iss": "https://auth.mi-proyecto.com",
    "sub": "google-oauth2|1122334455",
    "aud": [
      "https://api.mi-proyecto.com/v1",
      "https://admin.mi-proyecto.com"
    ],
    "iat": 1762956000,
    "exp": 1762959600,
    "jti": "mno-pqr-789",
    "email": "test@gmail.com",
    "permissions": [
      "read:data",
      "write:data"
    ]
  }
}
```

### Caso 3: Verificación Fallida - Clave Secreta Incorrecta

**Request:**
```json
POST /api/analyze/crypto-verification
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ.ka6DdIKip4EhcQ6vmyywTlebCmE9ZmgCyOFct9Pxgk8",
  "secret": "wrong-secret"
}
```

**Respuesta:**
```json
{
  "success": true,
  "valid": false,
  "error": "La firma no coincide. El token puede haber sido alterado o la clave secreta es incorrecta.",
  "algorithm": "HS256",
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  }
}
```

### Caso 4: Verificación Fallida - Token Alterado

**Request:**
```json
POST /api/analyze/crypto-verification
{
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ.XXXXXXXXXX",
  "secret": "secret"
}
```

**Respuesta:**
```json
{
  "success": true,
  "valid": false,
  "error": "La firma no coincide. El token puede haber sido alterado o la clave secreta es incorrecta.",
  "algorithm": "HS256",
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  }
}
```

### Caso 5: Verificación Fallida - Formato Inválido

**Request:**
```json
POST /api/analyze/crypto-verification
{
  "jwt": "not.a.valid.jwt.format",
  "secret": "secret"
}
```

**Respuesta:**
```json
{
  "success": true,
  "valid": false,
  "error": "Formato de JWT inválido: debe tener 3 partes separadas por puntos"
}
```

---

## Ejemplos de Codificación (Encoder)

### Caso 1: Codificación Básica con HS256

**Request:**
```json
POST /api/analyze/encoder
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "foo",
    "name": "John Doe"
  },
  "secret": "secret"
}
```

**Respuesta:**
```json
{
  "success": true,
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmb28iLCJuYW1lIjoiSm9obiBEb2UifQ.ka6DdIKip4EhcQ6vmyywTlebCmE9ZmgCyOFct9Pxgk8"
}
```

### Caso 2: Codificación Completa con Claims Estándar (HS256)

**Request:**
```json
POST /api/analyze/encoder
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "iss": "https://api.mi-proyecto.com",
    "sub": "auth0|1234567890",
    "aud": "https://api.mi-proyecto.com/v1",
    "iat": 1762956000,
    "exp": 1762959600,
    "nbf": 1762956000,
    "jti": "abc-def-123",
    "username": "jose.salamanca",
    "role": "admin"
  },
  "secret": "my-secret-key"
}
```

**Respuesta:**
```json
{
  "success": true,
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2FwaS5taS1wcm95ZWN0by5jb20iLCJzdWIiOiJhdXRoMHwxMjM0NTY3ODkwIiwiYXVkIjoiaHR0cHM6Ly9hcGkubWktcHJveWVjdG8uY29tL3YxIiwiaWF0IjoxNzYyOTU2MDAwLCJleHAiOjE3NjI5NTk2MDAsIm5iZiI6MTc2Mjk1NjAwMCwianRpIjoiYWJjLWRlZi0xMjMiLCJ1c2VybmFtZSI6Impvc2Uuc2FsYW1hbmNhIiwicm9sZSI6ImFkbWluIn0.hUyn-nFDX2xhtGcEtOSjvQobzZsWZc-putvn43AZphw"
}
```

### Caso 3: Codificación con HS384 y Array en Payload

**Request:**
```json
POST /api/analyze/encoder
{
  "header": {
    "alg": "HS384",
    "typ": "JWT"
  },
  "payload": {
    "iss": "https://auth.mi-proyecto.com",
    "sub": "google-oauth2|1122334455",
    "aud": [
      "https://api.mi-proyecto.com/v1",
      "https://admin.mi-proyecto.com"
    ],
    "iat": 1762956000,
    "exp": 1762959600,
    "jti": "mno-pqr-789",
    "email": "test@gmail.com",
    "permissions": [
      "read:data",
      "write:data"
    ]
  },
  "secret": "another-secret-key"
}
```

**Respuesta:**
```json
{
  "success": true,
  "jwt": "eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGgubWktcHJveWVjdG8uY29tIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyMzM0NDU1IiwiYXVkIjpbImh0dHBzOi8vYXBpLm1pLXByb3llY3RvLmNvbS92MSIsImh0dHBzOi8vYWRtaW4ubWktcHJveWVjdG8uY29tIl0sImlhdCI6MTc2Mjk1NjAwMCwiZXhwIjoxNzYyOTU5NjAwLCJqdGkiOiJtbm8tcHFyLTc4OSIsImVtYWlsIjoidGVzdEBnbWFpbC5jb20iLCJwZXJtaXNzaW9ucyI6WyJyZWFkOmRhdGEiLCJ3cml0ZTpkYXRhIl19.4-9i05RdPrJGV9WT8cK7czn-g--wt5w4nQYXomJkW3U5UTekXPNrkY0ftH8vjJ9w"
}
```

### Caso 4: Codificación con Clave Secreta por Defecto

**Request:**
```json
POST /api/analyze/encoder
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "user123",
    "name": "Test User"
  }
}
```

**Nota:** Si no se proporciona el campo `secret`, se usa `"secret"` por defecto.

**Respuesta:**
```json
{
  "success": true,
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzLCJuYW1lIjoiVGVzdCBVc2VyIn0.signature..."
}
```

### Caso 5: Error - Algoritmo No Soportado

**Request:**
```json
POST /api/analyze/encoder
{
  "header": {
    "alg": "RS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "foo"
  },
  "secret": "secret"
}
```

**Respuesta:**
```json
{
  "success": false,
  "error": "Algoritmo no soportado: RS256. Solo se soportan HS256 y HS384."
}
```

### Caso 6: Error - Falta Campo 'alg' en Header

**Request:**
```json
POST /api/analyze/encoder
{
  "header": {
    "typ": "JWT"
  },
  "payload": {
    "sub": "foo"
  },
  "secret": "secret"
}
```

**Respuesta:**
```json
{
  "success": false,
  "error": "El header debe contener el claim 'alg'"
}
```

### Caso 7: Error - Header o Payload No Son Objetos

**Request:**
```json
POST /api/analyze/encoder
{
  "header": "invalid",
  "payload": {
    "sub": "foo"
  },
  "secret": "secret"
}
```

**Respuesta:**
```json
{
  "success": false,
  "error": "Los campos \"header\" y \"payload\" deben ser objetos JSON (diccionarios)"
}
```
