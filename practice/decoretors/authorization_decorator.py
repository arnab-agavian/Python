# Authorization decorator is a function that wraps 
# another function to add authorization checks before 
# executing the wrapped function. It is commonly used in web applications to ensure that users have the 
# necessary permissions to access certain resources or perform specific actions.

from functools import wraps

# def admin_required(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         user = kwargs.get('user')
#         if user is None or not user.is_admin:
#             raise PermissionError("User does not have admin privileges.")
#         return func(*args, **kwargs)
#     return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != 'admin':
            raise PermissionError("User does not have admin privileges.")
        else:
            print("Admin privileges confirmed.")
            return func(user_role)
    return wrapper

@admin_required
def access_admin_panel(user_role):
    return f"Access granted to {user_role} panel."

access_admin_panel('admin')  # This will succeed
# access_admin_panel('user')   # This will raise a PermissionError