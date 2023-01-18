import uuid
from fastapi import APIRouter, Body, Depends
from app.forms import UserLoginForm
from app.models import connect_db, User, AuthToken
from app.utils import get_password_hash


router = APIRouter()


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), datebase=Depends(connect_db)):
    user = datebase.query(User).filter(User.email == user_form.email).one_or_none() # проверка юзера есть ли он в базе данных
    if not user or get_password_hash(user_form.password) != user.password:
        return {"error": "Email/password invalid"}

    auth_token = AuthToken(token=str(uuid.uuid4()), user_id=user.id)
    datebase.add(auth_token)
    datebase.commit()

    return {'status': 'OK'}

