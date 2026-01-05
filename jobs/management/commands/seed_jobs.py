from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random

from companies.models import Company
from jobs.models import Job


class Command(BaseCommand):
    help = 'Gera dados falsos de empresas e vagas de emprego'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            default=3,
            help='Número de usuários a criar'
        )
        parser.add_argument(
            '--companies',
            type=int,
            default=5,
            help='Número de empresas a criar'
        )
        parser.add_argument(
            '--jobs',
            type=int,
            default=20,
            help='Número de vagas a criar'
        )
        parser.add_argument(
            '--seed',
            type=int,
            default=42,
            help='Seed para garantir dados reproduzíveis'
        )

    def handle(self, *args, **options):
        # Configura seed para reproduzibilidade
        seed = options['seed']
        Faker.seed(seed)
        random.seed(seed)

        fake = Faker('pt_BR')

        num_users = options['users']
        num_companies = options['companies']
        num_jobs = options['jobs']

        self.stdout.write(self.style.SUCCESS(f'🌱 Iniciando seed com seed={seed}'))

        # Criar usuários
        self.stdout.write('👤 Criando usuários...')
        users = []
        for i in range(num_users):
            username = f'user_{i+1}'
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': f'user{i+1}@example.com',
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                }
            )
            users.append(user)
            if created:
                self.stdout.write(f'  ✓ Usuário criado: {username}')
            else:
                self.stdout.write(f'  ℹ Usuário já existia: {username}')

        # Criar empresas
        self.stdout.write('\n🏢 Criando empresas...')
        companies = []
        for i in range(num_companies):
            company_name = fake.company()
            company, created = Company.objects.get_or_create(
                name=company_name,
                owner=random.choice(users),
                defaults={
                    'description': fake.text(max_nb_chars=200),
                    'website': fake.url(),
                }
            )
            companies.append(company)
            if created:
                self.stdout.write(f'  ✓ Empresa criada: {company_name}')
            else:
                self.stdout.write(f'  ℹ Empresa já existia: {company_name}')

        # Criar vagas
        self.stdout.write('\n💼 Criando vagas de emprego...')
        job_titles = [
            'Desenvolvedor Python',
            'Desenvolvedor Django',
            'Desenvolvedor Full Stack',
            'Desenvolvedor Frontend',
            'Desenvolvedor Backend',
            'Desenvolvedor React',
            'Desenvolvedor Vue.js',
            'Desenvolvedor Node.js',
            'Desenvolvedor Java',
            'Desenvolvedor C#',
            'Data Scientist',
            'DevOps Engineer',
            'QA Engineer',
            'Líder Técnico',
            'Arquiteto de Software',
            'Mobile Developer',
            'Desenvolvedor iOS',
            'Desenvolvedor Android',
            'Security Engineer',
            'Machine Learning Engineer',
        ]

        levels = ['JR', 'PL', 'SR']

        for i in range(num_jobs):
            job_title = random.choice(job_titles)
            company = random.choice(companies)
            level = random.choice(levels)

            salary_ranges = {
                'JR': f'R$ 3.000 - R$ 5.000',
                'PL': f'R$ 5.000 - R$ 10.000',
                'SR': f'R$ 10.000 - R$ 20.000'
            }

            job, created = Job.objects.get_or_create(
                title=job_title,
                company=company,
                level=level,
                defaults={
                    'description': fake.text(max_nb_chars=500),
                    'salary_range': salary_ranges[level],
                    'is_active': random.choice([True, True, True, False]),  # 75% ativo
                }
            )
            if created:
                self.stdout.write(f'  ✓ Vaga criada: {job_title} ({level}) - {company.name}')
            else:
                self.stdout.write(f'  ℹ Vaga já existia: {job_title}')

        self.stdout.write(
            self.style.SUCCESS(
                f'\n✅ Seed concluído com sucesso!\n'
                f'   Usuários: {len(users)}\n'
                f'   Empresas: {len(companies)}\n'
                f'   Vagas: {num_jobs}'
            )
        )
