from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from django.shortcuts import render
from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render
from .models import Profile
from dashboard.models import (
    JellyfishLog, MonkeysLog, ParakeetsLog,
    CaterpillarLog, CrabsLog, FrogLog, TurtlesLog
)

import json

@api_view(['GET'])
def health_check(request):
    return Response('Ok')

def public_home(request):
    return render(request, "dashboard/public_home.html")

@never_cache
@login_required
def dashboard_view(request):
    return render(request, 'dashboard/index.html')

@never_cache
@login_required
def dashboard_root(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect("admin:index")  # or login, or render an error template

    if profile.user_type in ("researcher", "admin"):
        return redirect("user_list")
    elif profile.user_type == "student":
        return redirect("user_summary", user_id=profile.external_user_id)
    else:
        return redirect("user_list")

@never_cache
@login_required
def user_list(request):
    if request.user.profile.user_type not in ("researcher", "admin"):
        return redirect("dashboard_root")  # or 403

    students = Profile.objects.filter(user_type="student").order_by("school_id", "class_id", "student_number")
    # render with grouping logic in template

    grouped = {}
    for s in students:
        grouped.setdefault(s.school_id, {}).setdefault(s.class_id, []).append(s)

    return render(request, "dashboard/user_list.html", {"grouped": grouped})

# def user_list(request):
#     models = [
#         JellyfishLog, MonkeysLog, ParakeetsLog,
#         CaterpillarLog, CrabsLog, FrogLog, TurtlesLog
#     ]

#     # Collect all distinct users from all tables
#     user_ids = set()
#     for model in models:
#         user_ids.update(model.objects.values_list('user', flat=True).distinct())

#     return render(request, 'dashboard/user_list.html', {
#         'users': sorted(user_ids)
#     })

@never_cache
@login_required
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
