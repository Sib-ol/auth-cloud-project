import environ

env = environ.Env()
environ.Env.read_env()

print("SECRET_KEY TEST:", env('SECRET_KEY'))
