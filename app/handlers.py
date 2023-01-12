from fastapi import APIRouter, Body, Depends
from app.forms import UserLoginForm
from app.models import connect_db


router = APIRouter()


@router.post('/login', name='user:login')
def login(user_form: UserLoginForm = Body(..., embed=True), datebase=Depends(connect_db)):
    return {'status': 'OK'}