import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kladr_api import kladr_api_router
from kladr_site import kladr_site_router

app = FastAPI()
app.include_router(kladr_api_router)
app.include_router(kladr_site_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# uvicorn kladr:app --reload
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("kladr:app", reload=True)
