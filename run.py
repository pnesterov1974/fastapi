from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
#from starlette.staticfiles import StaticFiles

from kladr_api import kladr_api_router
from kladr_site import kladr_site_router

app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.include_router(kladr_api_router)
app.include_router(kladr_site_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("root.html", {"request": request})
    # return {'value': 'Корневая страница'}


#     return '''
# <!DOCTYPE html>
# <html lang="ru">

# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Корень</title>
# </head>

# <body>
#     Корневая страница
# </body>

# </html>
# '''

# uvicorn kladr:app --reload
# ---------------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("run:app", port=8000, reload=True, reload_delay=0.5)
    # uvicorn.run(app, port=8000, host='127.0.0.1', reload=True, reload_delay=0.5)
