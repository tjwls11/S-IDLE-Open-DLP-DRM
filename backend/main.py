from fastapi import FastAPI
from routers import files, policy, access, encrypt, logs
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DLP/DRM API")

app.include_router(files.router, prefix="/files", tags=["Files"])
app.include_router(policy.router, prefix="/policy", tags=["Policy"])
app.include_router(access.router, prefix="/access", tags=["Access Control"])
app.include_router(encrypt.router, prefix="/encrypt", tags=["Encryption"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://34.41.82.222:3000"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")
def root():
    return {"message": "Open DRM/DLP"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return {}
