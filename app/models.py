from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    is_active = models.BooleanField(default=False)
    is_trash = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Truck(TimeStampedModel):
    name = models.CharField(primary_key=True, max_length=255)
    location = models.CharField(max_length=255, null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    speed = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Driver(TimeStampedModel):
    OFF_DUTY = "OFF"
    SLEEPER_BERTH = "SB"
    ON_DUTY_NOT_DRIVING = "ON"
    DRIVING = "D"
    YARD_MOVES = "YM"
    PERSONAL_USE = "PC"

    STATUS_TYPE = (
        (OFF_DUTY, "Off duty"),
        (SLEEPER_BERTH, "Sleeper berth"),
        (ON_DUTY_NOT_DRIVING, "On duty not driving"),
        (DRIVING, "Driving"),
        (YARD_MOVES, "Yard moves"),
        (PERSONAL_USE, "Authorized personal use of CMV"),
    )

    driver_id = models.CharField(unique=True, max_length=255)
    truck = models.ForeignKey(
        Truck, on_delete=models.CASCADE, related_name="drivers", verbose_name="Truck"
    )
    duty_status = models.CharField(max_length=3, choices=STATUS_TYPE, null=True)
    duty_status_start_time = models.DateTimeField(null=True)
    shift_work_minutes = models.BigIntegerField()
    shift_drive_minutes = models.BigIntegerField()
    cycle_work_minutes = models.BigIntegerField()
    max_shift_work_minutes = models.BigIntegerField()
    max_shift_drive_minutes = models.BigIntegerField()
    max_cycle_work_minutes = models.BigIntegerField()
    home_terminal_time_zone_windows = models.CharField(max_length=255)
    home_terminal_time_zone_iana = models.CharField(max_length=255)

    class Meta:
        db_table = "drivers"

    def __str__(self):
        return self.driver_id
