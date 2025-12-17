# churchmembers/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import ChurchMember


@receiver(post_save, sender=ChurchMember)
def sync_member_to_user(sender, instance, **kwargs):
    """
    **DO NOT** sync from ChurchMember → ChurchUser.
    All personal data (first_name, email, etc.) is already set on ChurchUser
    during creation via ChurchMemberSerializer.

    ChurchMember model only has:
        - user (OneToOne to ChurchUser)
        - branch_name

    → It has NO first_name, last_name, email_address, etc.
    → Accessing them causes AttributeError.
    """
    # No action needed. Data is already on ChurchUser.
    pass


@receiver(post_delete, sender=ChurchMember)
def delete_user_on_member_delete(sender, instance, **kwargs):
    """
    Delete the linked ChurchUser when ChurchMember is deleted.
    """
    if instance.user:
        instance.user.delete()