from fastapi import FastAPI
from app.routes.measures_routes import router as measures_routes
# from app.routes.product_routes import router as product_routes
# from app.routes.user_routes import router as user_routes
# from app.routes.poc import router as poc_routes
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from app.exception_handlers import request_validation_exception_handler, http_exception_handler, unhandled_exception_handler
from app.middleware import log_request_middleware

app = FastAPI()

app.middleware("http")(log_request_middleware)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

@app.get('/health-check')
def health_check():
    return True

app.include_router(measures_routes)
# app.include_router(product_routes)
# app.include_router(user_routes)
# app.include_router(poc_routes)