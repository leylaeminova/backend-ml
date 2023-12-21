from fastapi import APIRouter

from api.user.v1.user import user_router as user_v1_router
from api.disease.v1.disease import disease_router as disease_v1_router
from api.auth.auth import auth_router

router = APIRouter()
router.include_router(user_v1_router, prefix="/api/v1/users", tags=["User"])
router.include_router(
    disease_v1_router, prefix="/api/v1/diseases", tags=["Disease"])
router.include_router(auth_router, prefix="/auth", tags=["Auth"])


__all__ = ["router"]
