from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dashboard.models import Profile

class Command(BaseCommand):
    help = 'Cria um usuário do tipo pesquisador (researcher)'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, required=True, help='Nome de usuário')
        parser.add_argument('--password', type=str, required=True, help='Senha do usuário')

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']

        user, created = User.objects.get_or_create(username=username)

        if created:
            user.set_password(password)
            user.is_staff = True  # permite acesso ao admin
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Usuário '{username}' criado."))
        else:
            self.stdout.write(f"Usuário '{username}' já existia.")

        profile, p_created = Profile.objects.get_or_create(user=user)
        profile.user_type = 'researcher'
        profile.external_user_id = username
        profile.save()

        if p_created:
            self.stdout.write(self.style.SUCCESS("Perfil de pesquisador criado com sucesso."))
        else:
            self.stdout.write("Perfil atualizado para pesquisador.")
