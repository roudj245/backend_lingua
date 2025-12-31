from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.quiz.router import router as quiz_router
from app.civilization.router import router as civilization_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Quiz API")

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz_router)
app.include_router(civilization_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Quiz API"}

