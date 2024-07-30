from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Cost, CostApproval
from django.core.mail import send_mail
from django.conf import settings



@receiver(post_save, sender=Cost)
def create_cost_approval(sender, instance, created, **kwargs):
    if created:
        # Set the status to "Requested"
        instance.status = 'Requested'
        instance.save()

        # Create the CostApproval record
        CostApproval.objects.create(
            name=f"Cost Approval for {instance.name}",
            cost=instance,
            status='Draft',
            task=instance.task,
            created_date=timezone.now(),
            created_by=instance.created_by,
            last_modified_date=timezone.now(),
            last_modified_by=instance.created_by
        )


def send_cost_approval_email(cost_approval):
    subject = 'New Cost Approval Request'
    message = f'Please review the cost approval at the following link: 120.1.2.1/charges/{cost_approval.id}'
    recipient_list = ['joanakrraba6@gmail.com']

    send_mail(
        subject,
        message,
        recipient_list,
        fail_silently=False,
    )

@receiver(post_save, sender=CostApproval)
def update_cost_status(sender, instance, **kwargs):
    if instance.status in ['Approved', 'Rejected']:
        cost = instance.cost
        cost.status = instance.status
        cost.save()


