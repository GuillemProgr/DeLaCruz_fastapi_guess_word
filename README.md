# Guess Word - API con FastAPI

Backend en **FastAPI** para un juego de adivinar palabras con soporte de varios idiomas. Guarda el historial de partidas de cada usuario en una base de datos **PostgreSQL**.

## Que hace

La API devuelve una palabra aleatoria segun el idioma, el abecedario de ese idioma y las instrucciones del juego. Ademas permite guardar una partida y consultar el historial de un usuario.

## Endpoints

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/llista/{idioma}` | Devuelve una palabra aleatoria del idioma indicado |
| GET | `/paraula/abecedari/{idioma}` | Devuelve las letras del abecedario del idioma |
| GET | `/instruccions/{idioma}` | Devuelve las instrucciones del juego |
| POST | `/historial` | Guarda los datos de una partida |
| GET | `/historial/{usuari}` | Devuelve el historial de partidas de un usuario |

## Tecnologias

Python, FastAPI, SQLModel, PostgreSQL, Uvicorn y Docker Compose (PostgreSQL y pgAdmin).

## Estructura

```
main.py            # App FastAPI y definicion de endpoints
models/            # Modelos de datos y esquemas de respuesta
services/          # Logica de negocio
crud/              # Acceso a la base de datos
docker-compose.yml # PostgreSQL y pgAdmin para desarrollo
requirements.txt   # Dependencias
```

## Como ejecutarlo

```bash
# 1. Levantar PostgreSQL y pgAdmin
docker compose up -d

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear un archivo .env (hay un ejemplo en .env.example)
DATABASE_URL=postgresql+psycopg2://admin:admin123@localhost:5432/guessdb

# 4. Arrancar la API
uvicorn main:app --reload
```

La documentacion interactiva queda en http://localhost:8000/docs

Las credenciales son de ejemplo y solo para desarrollo local.

## Video de la practica

[Conexion con el backend](https://drive.google.com/file/d/11NZ4XMJRSHSxPqlxEFffIMtwSEgid2_q/view?usp=drive_link)

## Autor

Guillem De La Cruz Paga - [LinkedIn](https://www.linkedin.com/in/guillem-de-la-cruz-b8289b382)
