from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

# from project_name.dependencies.service import get_service
# from {cookiecutter.app_name}}.schmeas import UserCreate, User
# from {cookiecutter.app_name}}.services import UserService

{{cookiecutter.app_name}}_router = APIRouter()



# You can define your View as the following


@cbv({{cookiecutter.app_name}}_router)
# class CustomerView:
#     {{cookiecutter.app_name}}_service = Depends(get_service(UserService))
#
#     @users_router.post("/", response_model=UserCreate)
#     def create_user(self, user: UserCreate):
#         return self.customer_service.add_user(user)