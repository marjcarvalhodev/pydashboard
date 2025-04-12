from django.db import models

class Escola(models.Model):
    name = models.CharField(max_length=100, unique=True)
    school_game_user = models.CharField(max_length=100, unique=True)  # used to match logs maybe?

    def __str__(self):
        return self.name


class Turma(models.Model):
    school = models.ForeignKey(Escola, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # remove unique constraint if name repeats across schools

    def __str__(self):
        return f'{self.school.name} - {self.name}'


class Aluno(models.Model):
    school_class = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='students')
    name = models.CharField(max_length=100)  # student "name" or user ID used in logs
    user_id = models.CharField(max_length=100, unique=True)  # This links to `user` in logs

    def __str__(self):
        return f'{self.user_id} ({self.name})'


class BaseLog(models.Model):
    user = models.CharField(max_length=100)
    unix_time = models.DateTimeField()
    minigame_id = models.CharField(max_length=50)
    lesson_id = models.IntegerField()
    elapsed_time = models.FloatField(null=True, blank=True)
    score = models.IntegerField()

    class Meta:
        abstract = True

class JellyfishLog(BaseLog):
    is_clicked = models.BooleanField()
    target_word = models.CharField(max_length=50)
    chapter_id = models.IntegerField()
    stimulus = models.CharField(max_length=50, blank=True)
    target = models.CharField(max_length=50, blank=True)

class MonkeysLog(BaseLog):
    game_level = models.IntegerField()
    stimulus = models.CharField(max_length=50, blank=True)
    target = models.CharField(max_length=50, blank=True)
    target_word = models.CharField(max_length=50)

class ParakeetsLog(BaseLog):
    game_level = models.IntegerField()
    response = models.CharField(max_length=100)  # store as JSON string
    stim_category = models.CharField(max_length=50, blank=True)
    target = models.CharField(max_length=50, blank=True)

class CaterpillarLog(BaseLog):
    game_level = models.IntegerField()
    stimulus = models.CharField(max_length=50, blank=True)
    target = models.CharField(max_length=50, blank=True)
    target_word = models.CharField(max_length=50)

class CrabsLog(BaseLog):
    target_word = models.CharField(max_length=50)
    is_clicked = models.BooleanField()
    chapter_id = models.IntegerField()
    stimulus = models.CharField(max_length=50, blank=True)
    target = models.CharField(max_length=50, blank=True)

class FrogLog(BaseLog):
    game_level = models.IntegerField()
    stimulus = models.CharField(max_length=50, blank=True)
    target = models.CharField(max_length=50, blank=True)
    target_word = models.CharField(max_length=50)

class TurtlesLog(BaseLog):
    game_level = models.IntegerField()
    stimulus = models.CharField(max_length=50, blank=True)
    target = models.CharField(max_length=50, blank=True)
    target_word = models.CharField(max_length=50)
