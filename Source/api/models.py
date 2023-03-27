from django.db import models

class Risk(models.Model):
    RISK_STATUS_CHOICES = [
        ('active', 'Active'),
        ('resolved', 'Resolved'),
        ('mitigated', 'Mitigated'),
    ]
    
    RISK_CATEGORY_CHOICES = [    
        ('financial', 'Financial'),    
        ('operational', 'Operational'),    
        ('strategic', 'Strategic'),    
        ('compliance', 'Compliance'),    
        ('cybersecurity', 'Cybersecurity'),    
        ('reputational', 'Reputational'),    
        ('legal', 'Legal'),    
        ('environmental', 'Environmental'),    
        ('health_safety', 'Health and Safety'),    
        ('technology', 'Technology'),    
        ('supply_chain', 'Supply Chain'),    
        ('market', 'Market'),    
        ('political', 'Political'),    
        ('social', 'Social'),    
        ('human_resource', 'Human Resource'),
    ]


    RISK_IMPACT_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    RISK_LIKELIHOOD_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(choices=RISK_CATEGORY_CHOICES, max_length=50)
    owner = models.CharField(max_length=255)
    likelihood = models.CharField(choices=RISK_LIKELIHOOD_CHOICES, max_length=50)
    impact = models.CharField(choices=RISK_IMPACT_CHOICES, max_length=50)
    overall_score = models.IntegerField(default=50)
    status = models.CharField(choices=RISK_STATUS_CHOICES, max_length=50)
    mitigation_plan = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    review_date = models.DateField()
    
    def __str__(self):
        return self.title