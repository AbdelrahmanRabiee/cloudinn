from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Cost(models.Model):
    Wood = models.IntegerField(_("Wood"), null=True, blank=True, help_text="How much wood it costs")
    Food = models.IntegerField(_("Food"), null=True, blank=True, help_text="How much Food it costs")
    Stone = models.IntegerField(_("Stone"), null=True, blank=True, help_text="How much Stone it costs")
    Gold = models.IntegerField(_("Gold"), null=True, blank=True, help_text="How much Gold it costs")

    class Meta:
        verbose_name = _("Cost")
        verbose_name_plural = _("Costs")

    def __str__(self):
        return "{} {} {} {}".format(str(self.Wood), str(self.Food), str(self.Stone), str(self.Gold))


class Structure(models.Model):
    """ Store structure Info """
    name = models.CharField(_("Name"), max_length=50, help_text="Name of the structure")
    description = models.TextField(
        _("Description"), null=True, blank=True,
        help_text="Short description of the structure"
        )
    expansion = models.CharField(
        _("Expansion"), max_length=50,
        help_text="Expansion in which the structure was introduced"
        )
    age = models.CharField(_("Age"), max_length=50, help_text="Age in which the structure can be built")
    cost = models.ForeignKey("empires.Cost", verbose_name=_("Cost"), on_delete=models.CASCADE)
    build_time = models.IntegerField(_("Build Time"), help_text="Build time in seconds")
    hit_points = models.IntegerField(_("Hit Points"), help_text="Hit points (health) of the structure")
    line_of_sight = models.IntegerField(_("Line of Sight"), help_text="Line of sight of the structure")
    armor = models.CharField(_("Armor"), max_length=50, help_text="Armor of the structure formated as ‘melee/pierce’")
    range = models.CharField(
        _("Range"), max_length=50, null=True, blank=True,
        help_text="Range of the structure. There can be a minimum and maximum range in the format (min-max)"
        )
    reload_time = models.DecimalField(
        _("Reload Time"), max_digits=5, decimal_places=2, null=True, blank=True, help_text="Reload time"
        )
    attack = models.IntegerField(_("Attack"), null=True, blank=True, help_text="Attack points of the structure")
    special = ArrayField(models.CharField(
        _("Special"), max_length=50, null=True, blank=True,
        help_text="Other information about the structure and the units it can garrison")
        )

    class Meta:
        verbose_name = _("Structure")
        verbose_name_plural = _("Structures")

    def __str__(self):
        return self.name


class Unit(models.Model):
    """store unit info"""
    name = models.CharField(_("Name"), max_length=50, help_text="Name of the unit")
    description = models.TextField(_("Description"), null=True, blank=True, help_text="Short description of the unit")
    expansion = models.CharField(
        _("Expansion"), max_length=255,
        help_text="Expansion in which the unit was introduced"
        )
    age = models.CharField(_("Age"), max_length=50, help_text="Age in which the unit can be produced")
    created_in = models.CharField(
        _("Created In"), max_length=120, default="", help_text="Structure the unit is created in"
        )
    cost = models.ForeignKey("empires.Cost", verbose_name=_("Cost"), on_delete=models.CASCADE, null=True, blank=True)
    build_time = models.IntegerField(_("Build Time"), null=True, blank=True, help_text="Build time in seconds")
    reload_time = models.DecimalField(
        _("Reload Time"), null=True, blank=True,
        max_digits=5, decimal_places=2, help_text="Reload time"
        )
    attack_delay = models.DecimalField(
        _("Attack Delay"), max_digits=5, decimal_places=2, null=True, blank=True,
        help_text="Attack delay when you give the order to attack"
        )
    movement_rate = models.DecimalField(
        _("Movement Rate"), max_digits=5, decimal_places=2,
        null=True, blank=True, help_text="Movement Rate"
        )
    line_of_sight = models.IntegerField(_("Line of Sight"), help_text="Line of sight of the unit")
    hit_points = models.IntegerField(_("Hit Points"), help_text="Hit points (health) of the unit")
    range = models.CharField(
        _("Range"), max_length=50, null=True, blank=True,
        help_text="Range of the unit. There can be a minimum and maximum range in the format (min-max)"
        )
    attack = models.IntegerField(_("Attack"), null=True, blank=True, help_text="Attack of the unit")
    armor = models.CharField(_("Armor"), max_length=50, help_text="Armor of the unit formated as ‘melee/pierce’")
    attack_bonus = ArrayField(models.CharField(
        _("Attack Bonus"), max_length=50, null=True, blank=True, help_text="Attack bonuses of the unit"),
        null=True, blank=True)
    armor_bonus = ArrayField(models.CharField(
        _("Armor Bonus"), max_length=50, null=True, blank=True, help_text="Armor bonuses of the unit"),
        null=True, blank=True)
    search_radius = models.IntegerField(
        _("search Radius"), null=True, blank=True, help_text="Search Radius of the unit"
        )
    accuracy = models.CharField(
        _("Accurcay"), max_length=255, null=True, blank=True, help_text="Attack accuracy (as %) of the unit"
        )
    blast_radius = models.DecimalField(
        _("Blast Radius"), max_digits=5, decimal_places=2, null=True, blank=True, help_text="Attack blast radius"
        )

    class Meta:
        verbose_name = _("Unit")
        verbose_name_plural = _("Units")

    def __str__(self):
        return self.name
