import csv
import json
import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timezone as dt_timezone
from dashboard.models import (
    JellyfishLog, MonkeysLog, ParakeetsLog, 
    CaterpillarLog, CrabsLog, FrogLog, TurtlesLog
)
from datetime import datetime

class Command(BaseCommand):
    help = 'Load logs from CSV or JSON'

    def add_arguments(self, parser):
        parser.add_argument('--source', type=str, choices=['csv', 'json'], required=True)

    def handle(self, *args, **options):
        source = options['source']
        base_path = os.path.join('data', source)

        loaders = {
            'jellyfish': self.load_jellyfish,
            'monkeys': self.load_monkeys,
            'parakeets': self.load_parakeets,
            'caterpillar': self.load_caterpillar,
            'crabs': self.load_crabs,
            'frog': self.load_frog,
            'turtles': self.load_turtles
        }

        for name, loader in loaders.items():
            file_path = os.path.join(base_path, f'{name}.{source}')
            if os.path.exists(file_path):
                print(f"Loading {name} logs from {file_path}")
                loader(file_path, source)
            else:
                print(f"File {file_path} not found, skipping...")

        self.stdout.write(self.style.SUCCESS('✅ All logs loaded successfully.'))

    def to_datetime(self, timestamp):
        return datetime.fromtimestamp(int(timestamp), tz=dt_timezone.utc)
    
    def safe_int(self, val, default=-1):
        try:
            val = str(val).strip().lower()
            return int(val) if val not in ('', 'none', 'null') else default
        except (ValueError, TypeError):
            return default

    def safe_float(self, val, default=None):
        try:
            val = str(val).strip().lower()
            return float(val) if val not in ('', 'none', 'null') else default
        except (ValueError, TypeError):
            return default


    def load_file(self, filepath, source):
        if source == 'csv':
            with open(filepath, newline='', encoding='utf-8') as f:
                return list(csv.DictReader(f))
        else:  # json
            with open(filepath, encoding='utf-8') as f:
                return json.load(f)

    def load_jellyfish(self, filepath, source):
        rows = self.load_file(filepath, source)
        objs = [
            JellyfishLog(
                user=row['user'],
                unix_time=self.to_datetime(row['unixTime']),
                minigame_id=row['minigameId'],
                lesson_id=self.safe_int(row['lessonId']),
                elapsed_time=self.safe_float(row['elapsedTime']),
                score=self.safe_int(row['score']),
                is_clicked=row['isClicked'].lower() == 'true',
                target_word=row['targetWord'],
                chapter_id=self.safe_int(row['chapterId']),
                stimulus=row.get('stimulus', ''),
                target=row.get('target', '')
            ) for row in rows
        ]
        JellyfishLog.objects.bulk_create(objs)
        print(f"Loaded {len(objs)} Jellyfish logs.")

    def load_monkeys(self, filepath, source):
        rows = self.load_file(filepath, source)
        objs = [
            MonkeysLog(
                user=row['user'],
                unix_time=self.to_datetime(row['unixTime']),
                minigame_id=row['minigameId'],
                lesson_id=self.safe_int(row['lessonId']),
                elapsed_time=self.safe_float(row['elapsedTime']),
                score=self.safe_int(row['score']),
                game_level=self.safe_int(row['game_level']),
                stimulus=row.get('stimulus', ''),
                target=row.get('target', ''),
                target_word=row['targetWord']
            ) for row in rows
        ]
        MonkeysLog.objects.bulk_create(objs)
        print(f"Loaded {len(objs)} Monkeys logs.")

    def load_parakeets(self, filepath, source):
        rows = self.load_file(filepath, source)
        objs = [
            ParakeetsLog(
                user=row['user'],
                unix_time=self.to_datetime(row['unixTime']),
                minigame_id=row['minigameId'],
                lesson_id=self.safe_int(row['lessonId']),
                elapsed_time=self.safe_float(row['elapsedTime']),
                score=self.safe_int(row['score']),
                game_level=self.safe_int(row['game_level']),
                response=json.dumps(row['response']) if isinstance(row['response'], (list, dict)) else row['response'],
                stim_category=row.get('stim_category', ''),
                target=row.get('target', '')
            ) for row in rows
        ]
        ParakeetsLog.objects.bulk_create(objs)
        print(f"Loaded {len(objs)} Parakeets logs.")

    def load_caterpillar(self, filepath, source):
        rows = self.load_file(filepath, source)
        objs = [
            CaterpillarLog(
                user=row['user'],
                unix_time=self.to_datetime(row['unixTime']),
                minigame_id=row['minigameId'],
                lesson_id=self.safe_int(row['lessonId']),
                elapsed_time=self.safe_float(row['elapsedTime']),
                score=self.safe_int(row['score']),
                game_level=self.safe_int(row['game_level']),
                stimulus=row.get('stimulus', ''),
                target=row.get('target', ''),
                target_word=row['targetWord']
            ) for row in rows
        ]
        CaterpillarLog.objects.bulk_create(objs)
        print(f"Loaded {len(objs)} Caterpillar logs.")

    def load_crabs(self, filepath, source):
        rows = self.load_file(filepath, source)
        objs = [
            CrabsLog(
                user=row['user'],
                unix_time=self.to_datetime(row['unixTime']),
                minigame_id=row['minigameId'],
                lesson_id=self.safe_int(row['lessonId']),
                elapsed_time=self.safe_float(row['elapsedTime']),
                score=self.safe_int(row['score']),
                is_clicked=row['isClicked'].lower() == 'true',
                target_word=row['targetWord'],
                chapter_id=self.safe_int(row['chapterId']),
                stimulus=row.get('stimulus', ''),
                target=row.get('target', '')
            ) for row in rows
        ]
        CrabsLog.objects.bulk_create(objs)
        print(f"Loaded {len(objs)} Crabs logs.")

    def load_frog(self, filepath, source):
        rows = self.load_file(filepath, source)
        objs = [
            FrogLog(
                user=row['user'],
                unix_time=self.to_datetime(row['unixTime']),
                minigame_id=row['minigameId'],
                lesson_id=self.safe_int(row['lessonId']),
                elapsed_time=self.safe_float(row['elapsedTime']),
                score=self.safe_int(row['score']),
                game_level=self.safe_int(row['game_level']),
                stimulus=row.get('stimulus', ''),
                target=row.get('target', ''),
                target_word=row['targetWord']
            ) for row in rows
        ]
        FrogLog.objects.bulk_create(objs)
        print(f"Loaded {len(objs)} Frog logs.")

    def load_turtles(self, filepath, source):
        rows = self.load_file(filepath, source)
        objs = [
            TurtlesLog(
                user=row['user'],
                unix_time=self.to_datetime(row['unixTime']),
                minigame_id=row['minigameId'],
                lesson_id=self.safe_int(row['lessonId']),
                elapsed_time=self.safe_float(row['elapsedTime']),
                score=self.safe_int(row['score']),
                game_level=self.safe_int(row['game_level']),
                stimulus=row.get('stimulus', ''),
                target=row.get('target', ''),
                target_word=row['targetWord']
            ) for row in rows
        ]
        TurtlesLog.objects.bulk_create(objs)
        print(f"Loaded {len(objs)} Turtles logs.")
