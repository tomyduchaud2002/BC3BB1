from django.contrib.auth import get_user_model
User = get_user_model()
try:
    u = User.objects.get(username='admin')
    u.set_password('GarageAdmin!234')
    u.save()
    print('Password set for admin.')
except User.DoesNotExist:
    print('Admin user not found.')