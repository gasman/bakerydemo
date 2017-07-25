from django.contrib.auth.models import User, Group


def init_user(user_dict):
    user = User.objects.get(username=user_dict['username'][0])
    if 'wagtail-admins' in user_dict['groups']:
        user.is_staff = True
        user.is_superuser = True
        user.save()

    groups = []
    if 'wagtail-editors' in user_dict['groups']:
        groups.append(Group.objects.get(name='Editors'))
    if 'wagtail-moderators' in user_dict['groups']:
        groups.append(Group.objects.get(name='Moderators'))
    if 'wagtail-blog-readers' in user_dict['groups']:
        groups.append(Group.objects.get(name='Blog readers'))

    user.groups = groups
