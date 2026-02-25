from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routes import upload, analysis, patients, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MedInsight AI API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api/upload")
app.include_router(analysis.router, prefix="/api/analysis")
app.include_router(patients.router, prefix="/api/patients")
app.include_router(reports.router, prefix="/api/reports")

@app.get("/")
def root():
    return {"message": "MedInsight AI Backend Running"}