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

