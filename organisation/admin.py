from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin
from .models import Direction,Service,Collaborator,Role,Application,TechnicalType,Project,TechnicalSkill,ProjectMember,ApplicationMember,ProjectRequest


class TechnicalSkillInline(admin.TabularInline):
    
    model = TechnicalSkill
    extra = 1


class ApplicationMemberInline(admin.TabularInline):
    
    model = ApplicationMember
    extra = 1


class ProjectMemberInline(admin.TabularInline):
    
    model = ProjectMember
    extra = 1
    

class ApplicationAdmin(admin.ModelAdmin):

    list_display = ('name',)


class CollaboratorResource(resources.ModelResource):
    
    service = fields.Field(
        column_name='service',
        attribute='service',
        widget=ForeignKeyWidget(Service, 'name')
    )

    class Meta:
        model = Collaborator
        fields = ('name','service','code')
        export_order = ('name','service','code',)
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('code',)


class CollaboratorAdmin(ImportExportModelAdmin): 
    
    list_display = ('name', 'service', 'code', 'active', 'applicationmember_display')
    resource_class = CollaboratorResource
    inlines = [
        ApplicationMemberInline,
        ProjectMemberInline,
        TechnicalSkillInline,
    ]

    def applicationmember_display(self, obj):
        return ", ".join([
            child.application.name for child in ApplicationMember.objects.filter(collaborator__id=obj.id)
        ])
    applicationmember_display.short_description = "Application"


admin.site.register(Direction)
admin.site.register(Service)
admin.site.register(Role)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(TechnicalType)
admin.site.register(Project)
admin.site.register(ProjectRequest)
