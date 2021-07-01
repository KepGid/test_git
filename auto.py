def authenticate(login, password):
    if login == 'login' and password=='password':
        return "you were logged in"
    else:
        return "Login is incored"