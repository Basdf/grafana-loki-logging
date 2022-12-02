from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.schemas.root import HealtCheck
from app.core.logging import get_logger

router = APIRouter()
logger = get_logger(__name__)


@router.get(
    "/debug",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def debug_log():
    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    logger.debug(f"status={status.HTTP_200_OK} message=OK")
    return health_data


@router.get(
    "/info",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def info_log():
    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    logger.info(f"status={status.HTTP_201_CREATED} message=CREATED")
    return health_data


@router.get(
    "/warning",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def warning_log():
    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    logger.warning(
        f"status={status.HTTP_422_UNPROCESSABLE_ENTITY} message=UNPROCESSABLE_ENTITY"
    )
    return health_data


@router.get(
    "/error",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def error_log():
    logger.error(f"status={status.HTTP_400_BAD_REQUEST} message=BAD_REQUEST")
    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    return health_data


@router.get(
    "/critical",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def critical_log():
    logger.critical(
        f"status={status.HTTP_500_INTERNAL_SERVER_ERROR} message=INTERNAL_SERVER_ERROR"
    )
    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    return health_data


@router.post(
    "",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def post():

    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    return health_data


@router.put(
    "",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def put():

    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    return health_data


@router.patch(
    "",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def patch():

    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    return health_data


@router.delete(
    "",
    response_class=JSONResponse,
    response_model=HealtCheck,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Health check found"},
    },
)
def delete():

    health_data = {
        "title": settings.TITLE,
        "version": settings.VERSION,
        "description": settings.DESCRIPTION,
        "environment": settings.ENVIRONMENT,
    }
    return health_data
