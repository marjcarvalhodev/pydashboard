from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dashboard.models import (
    Profile,
    CaterpillarLog,
    CrabsLog,
    FrogLog,
    JellyfishLog,
    MonkeysLog,
    ParakeetsLog,
    TurtlesLog,
)

class Command(BaseCommand):
    help = "Populate Django auth users from all Kalulu game logs"

    def handle(self, *args, **kwargs):
        all_user_ids = set()

        log_models = [
            CaterpillarLog,
            CrabsLog,
            FrogLog,
            JellyfishLog,
            MonkeysLog,
            ParakeetsLog,
            TurtlesLog,
        ]

        for model in log_models:
            all_user_ids.update(model.objects.values_list("user", flat=True))

        self.stdout.write(self.style.SUCCESS(f"Found {len(all_user_ids)} users."))

        created = 0
        updated = 0

        for user_id in all_user_ids:
            user, _ = User.objects.get_or_create(username=user_id, defaults={'password': 'default123'})

            parts = str(user_id).split("_")
            if len(parts) == 3:
                school_id, class_id, student_number = parts
            else:
                school_id = class_id = student_number = None

            profile, created_profile = Profile.objects.get_or_create(user=user)

            # Always ensure it's marked as a student and has school/class/student info
            needs_update = False

            if profile.user_type != "student":
                profile.user_type = "student"
                needs_update = True
            if profile.external_user_id != user_id:
                profile.external_user_id = user_id
                needs_update = True
            if profile.school_id != school_id:
                profile.school_id = school_id
                needs_update = True
            if profile.class_id != class_id:
                profile.class_id = class_id
                needs_update = True
            if profile.student_number != student_number:
                profile.student_number = student_number
                needs_update = True

            if needs_update:
                profile.save()
                updated += 1

            if created_profile:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Created {created} new profiles."))
        self.stdout.write(self.style.SUCCESS(f"Updated {updated} existing profiles."))
        self.stdout.write(self.style.SUCCESS(f"Total users: {User.objects.count()}"))
