
from fastapi import FastAPI
from routes.alumno import alumno
from routes.profesor import profesor
from fastapi.responses import RedirectResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI()
app.include_router(alumno)
app.include_router(profesor)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=400)

@app.get('/')
def read_root():
    return RedirectResponse(url='/docs')
