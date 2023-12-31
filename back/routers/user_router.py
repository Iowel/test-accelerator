

from datetime import datetime

from fastapi import APIRouter, HTTPException, Path, Response

from routers.schemas import User, UserList, UpdateUserSchema




users = [
    User(id=1, username='andryc2', first_name='Andry', last_name='Johns', age=23, created_at=datetime.now()),
    User(id=2, username='mart3', first_name='Marty', last_name='Flatcher', age=32, created_at=datetime.now()),
    User(id=3, username='johny32', first_name='John', last_name='Does', age=14, created_at=datetime.now()),
]



user_router = APIRouter(prefix='/users', tags=['Пользователи'])


@user_router.get('/', name='Все пользователи', response_model=UserList)
def get_all_users():

    return UserList(count=len(users), users=users)



@user_router.post('/', name='Добавить пользователя', response_model=User)
def create_user(user: User):
    users.append(user)
    return user



@user_router.get('/{user_id}', name='Получить пользователя', response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail='User not found')
        

@user_router.delete('/{user_id}', name='Удалить пользователя', response_class=Response)
def delete_user(user_id:int):
    for i, user in enumerate(tuple(users)):
        if user.id == user_id:
            del users[i]
            break
    return Response(status_code=204)


@user_router.put('/{user_id}', name='Обновить данные пользователя', response_model=User)
def update_user(user_id: int, new_user_data: UpdateUserSchema):
    for i in range(len(users)):
        if users[i].id == user_id:
            data = new_user_data.model_dump()
            for key in data:
                if data[key] is not None:
                    setattr(users[i], key, data[key])
            break
    return users[i]

@user_router.put('/{user_id}', name='Обновить данные пользователя', response_model=User)
def update_user(user_id: int, new_user_data: UpdateUserSchema):
    for i in range(len(users)):
        if users[i].id == user_id:
            data = new_user_data.dict()
            for key in data:
                if data[key] is not None:
                    setattr(users[i], key, data[key])
            break
    raise HTTPException(status_code=404, detail='User not found')














