# Dummy auth function
def user_authenticated(email: str, password: str) -> bool:
    return True if password == "test" else False
