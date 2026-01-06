# from fastapi import FastAPI
# from App.database import Base, engine
# from App.routers import singin
# from App.routers import login
# from fastapi.middleware.cors import CORSMiddleware
# from App.routers import  authorization
# from App.routers import token


# Base.metadata.create_all(bind=engine)

# app = FastAPI()


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         "http://localhost:5173",  
#         "http://127.0.0.1:5173"
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )



# app.include_router(authorization.router)
# app.include_router(token.router)
# app.include_router(singin.router,tags=["singin"])
# app.include_router(login.router,tags=["login"])

# @app.get("/")
# def home():
#     return {"message": "FastAPI running successfully"}



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from App.database import Base, engine
from App.routers import singin, login, token, authorization
from App.utils.config import ALLOWED_ORIGINS

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(singin.router)
app.include_router(login.router)
app.include_router(token.router)
app.include_router(authorization.router)

@app.get("/")
def home():
    return {"message": "FastAPI running successfully"}
