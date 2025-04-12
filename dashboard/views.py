from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from dashboard.models import (
    JellyfishLog, MonkeysLog, ParakeetsLog,
    CaterpillarLog, CrabsLog, FrogLog, TurtlesLog
)

import json

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')

@api_view(['GET'])
def health_check(request):
    return Response('Ok')

def user_list(request):
    models = [
        JellyfishLog, MonkeysLog, ParakeetsLog,
        CaterpillarLog, CrabsLog, FrogLog, TurtlesLog
    ]

    # Collect all distinct users from all tables
    user_ids = set()
    for model in models:
        user_ids.update(model.objects.values_list('user', flat=True).distinct())

    return render(request, 'dashboard/user_list.html', {
        'users': sorted(user_ids)
    })

def user_summary(request, user_id):
    game_models = {
        'jellyfish': JellyfishLog,
        'monkeys': MonkeysLog,
        'parakeets': ParakeetsLog,
        'caterpillar': CaterpillarLog,
        'crabs': CrabsLog,
        'frog': FrogLog,
        'turtles': TurtlesLog,
    }

    data = []

    for game, model in game_models.items():
        logs = model.objects.filter(user=user_id)
        total_score = sum(log.score for log in logs)
        data.append({
            'game': game,
            'attempts': logs.count(),
            'score': total_score,
        })

    return render(request, 'dashboard/user_summary.html', {
        'user_id': user_id,
        'summary': data,
        'chart_data': json.dumps({
            'labels': [entry['game'] for entry in data],
            'scores': [entry['score'] for entry in data],
        }),
    })
