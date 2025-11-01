# churchmembers/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from authentication.models import ChurchUser
from .models import ChurchMember

@receiver(post_save, sender=ChurchUser)
def sync_user_to_member(sender, instance, created, **kwargs):
    if instance.role == 'member':
        member, _ = ChurchMember.objects.get_or_create(user=instance)
        # Only update member fields — DO NOT save instance.user
        member.first_name = instance.first_name
        member.last_name = instance.last_name
        member.email_address = instance.email_address
        member.phone_number = instance.phone_number
        member.whatsapp_number = instance.whatsapp_number
        member.gender = instance.gender
        member.age_group = instance.age_group
        member.branch_name = instance.branch_name
        member.resident = instance.resident
        member.marital_status = instance.marital_status
        member.is_baptized = instance.is_baptized
        member.save()  # Only save ChurchMember
    else:
        ChurchMember.objects.filter(user=instance).delete()

@receiver(post_save, sender=ChurchMember)
def sync_member_to_user(sender, instance, **kwargs):
    # Only update ChurchUser fields — DO NOT call save() on user
    ChurchUser.objects.filter(pk=instance.user.pk).update(
        first_name=instance.first_name,
        last_name=instance.last_name,
        email_address=instance.email_address,
        phone_number=instance.phone_number,
        whatsapp_number=instance.whatsapp_number,
        gender=instance.gender,
        age_group=instance.age_group,
        branch_name=instance.branch_name,
        resident=instance.resident,
        marital_status=instance.marital_status,
        is_baptized=instance.is_baptized,
    )

@receiver(post_delete, sender=ChurchMember)
def delete_user_on_member_delete(sender, instance, **kwargs):
    pass