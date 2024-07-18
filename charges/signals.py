from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Cost, CostApproval



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

