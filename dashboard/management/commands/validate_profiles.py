from django.core.management.base import BaseCommand
from dashboard.models import Profile

class Command(BaseCommand):
    help = "Populate Django auth users from all Kalulu game logs"

    def handle(self, *args, **kwargs):
        from dashboard.models import Profile

        # Step 1: Check total student profiles
        student_qs = Profile.objects.filter(user_type="student")
        print("Total student profiles:", student_qs.count())

        # Step 2: Inspect first student
        sample = student_qs.first()
        if sample:
            print("\nSample student:")
            print("  Username:", sample.user.username)
            print("  School:", sample.school_id)
            print("  Class:", sample.class_id)
            print("  Student #:", sample.student_number)
        else:
            print("⚠️ No student profiles found")

        # Step 3: Build same 'grouped' structure as the view
        grouped = {}
        for s in student_qs:
            grouped.setdefault(s.school_id, {}).setdefault(s.class_id, []).append(s)

        # Step 4: Inspect structure
        print("\nGrouped students by school and class:\n")
        for school, classes in grouped.items():
            print(f"🏫 {school}")
            for class_id, student_list in classes.items():
                print(f"  📚 Class {class_id}")
                for student in student_list:
                    print(f"    👤 {student.student_number} — {student.user.username}")
