from django.db import models


class Direction(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    shortname = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class Service(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Role(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class Application(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Collaborator(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=10, null=True, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ApplicationMember(models.Model):

    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    rate = models.PositiveSmallIntegerField()
    collaborator = models.ForeignKey(Collaborator, related_name="member", on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "%s %s" % (self.application, self.role)


class TechnicalType(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class TechnicalSkill(models.Model):

    type = models.ForeignKey(TechnicalType, on_delete=models.CASCADE, null=True)
    rate = models.PositiveSmallIntegerField()
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.type.name


class Project(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)

    def __str__(self):
        return self.name


class ProjectRequest(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    request_date = models.DateField(blank=True, null=True)
    affected = models.BooleanField(default=False)
    affectation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectMember(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    collaborator = models.ForeignKey(Collaborator, on_delete=models.CASCADE, null=True)
    period_start = models.DateField(blank=True, null=True)
    period_end = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.project is not None:
            return self.project.name
        else:
            return self.application.name
