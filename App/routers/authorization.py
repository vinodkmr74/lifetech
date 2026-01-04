from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from App.utils.config import SECRET_KEY, ALGORITHM

router = APIRouter(prefix="/api")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token_generate")

@router.get("/authorization")
def authorization(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "Authorized", "user": payload}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
