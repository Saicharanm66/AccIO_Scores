from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import Team, TeamMember, scoreupdate, Schedule
from .forms import CustomFooForm
# Register your models here.

class TeamAdminInline(TabularInline):
        model = Team

# @admin.register(TeamMember)
# class TeamMembersModelAdmin(admin.ModelAdmin):
#     #inlines = [TeamAdminInline,]
#     fields = ('teamname','player_img', 'player_name',  'Player_type', 'Player_side')
#     search_fields = ['teamname', 'player_name', 'Player_type','Player_side', ]
@admin.register(Team)
class TeamModelAdmin(admin.ModelAdmin):
    fields = ('team_name','img','desc','Winnings','team')
    search_fields = ('team_name',)
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    search_fields = ['firstteam', 'secondteam','date','time','Status']
admin.site.register(scoreupdate)
from django.contrib import admin
from app.forms import CustomFooForm

@admin.register(TeamMember)
class FooAdmin(admin.ModelAdmin):
    form = CustomFooForm
    add_form = CustomFooForm # It is not a native django field. I created this field and use it in get_form method.
    search_fields = ('team_name',)
    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during foo creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)