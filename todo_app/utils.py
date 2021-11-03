from django.contrib.auth import get_user_model

from todo_app.models import Todo

User = get_user_model()
# def get_user_by_email_and_check_psw(email, psw) -> User:
#     user = User.query.filter_by(email=email).first()
#     if user and check_password_hash(user.hash_password, psw):
#         return user
#     raise NoUserOrPSW

#
# def check_user_name_and_email(name, email) -> bool:
#     return bool(User.query.filter(or_(User.name == name, User.email == email)).first())


def get_todo_for_user(user_id, priority):
    if priority:
        data = Todo.objects.filter(user_id=user_id). \
            filter(priority=priority). \
            order_by('display_priority').all()
    else:
        data = Todo.objects.filter(user_id=user_id). \
            order_by('display_priority').all()
    return data


def find_next_display_priority_for_user() -> int:
    data = Todo.objects.last()
    display_priority = (data.id + 1) if data else 1
    return display_priority


# def get_link(display):
#     return TodoList.query.filter_by(display_priority=display).first()


# def get_up_link(link, priority, current_user):
#     if priority:
#         link_next = TodoList.query.filter(TodoList.user == current_user). \
#             filter_by(priority=priority). \
#             filter(TodoList.display_priority < link.display_priority). \
#             order_by(TodoList.display_priority.desc()).first()
#     else:
#         link_next = TodoList.query.filter(TodoList.user == current_user). \
#             filter(TodoList.display_priority < link.display_priority). \
#             order_by(TodoList.display_priority.desc()).first()
#     if link_next:
#         return link_next
#     raise NoLink


# def get_down_link(link, priority, current_user):
#     if priority:
#         link_next = TodoList.query.filter(TodoList.user == current_user). \
#             filter_by(priority=priority). \
#             filter(TodoList.display_priority > link.display_priority). \
#             order_by(TodoList.display_priority).first()
#     else:
#         link_next = TodoList.query.filter(TodoList.user == current_user). \
#             filter(TodoList.display_priority > link.display_priority). \
#             order_by(TodoList.display_priority).first()
#     if link_next:
#         return link_next
#     raise NoLink