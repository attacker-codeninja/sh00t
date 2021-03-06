import os
import django
import sys
from os.path import dirname, abspath

sh00t_path = dirname(dirname(abspath(__file__)))
sys.path.append(sh00t_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()


def reset_user():
    sh00t_password = "sh00t"

    from django.contrib.auth.models import User
    try:
        sh00t_user = User.objects.get(username="sh00t")
        sh00t_user.set_password(sh00t_password)
        sh00t_user.save()

    except User.DoesNotExist:
        User.objects.create_superuser('sh00t', 'sh00t@example.com', sh00t_password)


# Call the function if this file was run directly for backward compatibility.
if __name__ == "__main__":
    reset_user()
