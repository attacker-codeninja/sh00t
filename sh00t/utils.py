from django.apps import apps

def generate_secret_key(secret_file):
    try:
        # Ref: https://gist.github.com/ndarville/3452907#file-secret-key-gen-py
        import random
        secret_key = ''.join(
            [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in
             range(50)])
        secret = open(secret_file, 'w')
        secret.write(secret_key)
        secret.close()
        # First installation secret doesn't exists or upgraded so that the secret has changed. Reset user
        from scripts.createsuperuser import reset_user
        reset_user()
    except IOError:
        Exception('Looks like permission issue. Please create a %s file with random characters \
        to generate your secret key!' % secret_file)

    return securet_key


def get_secret_key(secret_file):
    try:
        if apps.get_models():
            try:
                secret_key = open(secret_file).read().strip()
            except IOError:
                secret_key = generate_secret_key(secret_file)
            return secret_key
    except Exception:
        # In case the app not loaded yet, migrate time, return a constant key for now
        return "&&c6x1*i7*0c5n9u6dv%-n(81200f15iuzmzbarlkr#p9)7#1s"


def db_table_exists(table_name):
    return table_name in connection.introspection.table_names()