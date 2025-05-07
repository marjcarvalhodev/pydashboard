from django.core.management.base import BaseCommand
from dashboard.models import (
    CaterpillarLog, CrabsLog, FrogLog, JellyfishLog,
    MonkeysLog, ParakeetsLog, TurtlesLog
)
from collections import defaultdict

class Command(BaseCommand):
    help = "Populate Django auth users from all Kalulu game logs"

    def handle(self, *args, **kwargs):
        log_models = {
            "Caterpillar": CaterpillarLog,
            "Crabs": CrabsLog,
            "Frog": FrogLog,
            "Jellyfish": JellyfishLog,
            "Monkeys": MonkeysLog,
            "Parakeets": ParakeetsLog,
            "Turtles": TurtlesLog,
        }

        user_game_activity = defaultdict(lambda: defaultdict(int))

        for game_name, model in log_models.items():
            for row in model.objects.values("user"):
                user_id = row["user"]
                user_game_activity[user_id][game_name] += 1

        # Build summary table
        summary = []
        for user_id, games in user_game_activity.items():
            summary.append({
                "user": user_id,
                "game_count": len(games),
                "log_count": sum(games.values())
            })

        # Sort and print top 10
        summary.sort(key=lambda x: (x["game_count"], x["log_count"]), reverse=True)

        print("Top 10 most active users:")
        for user in summary[:10]:
            print(f"{user['user']}: {user['game_count']} games, {user['log_count']} logs")
