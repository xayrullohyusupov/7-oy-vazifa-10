from django.urls import path
from .views import contact_list, contact_detail
from .views import (
    contact_list, contact_detail,
    chooseitem_list, chooseitem_detail,
    teammember_list, teammember_detail,
    partner_list, partner_detail,
    roadmapitem_list, roadmapitem_detail,
    contactmessage_list, contactmessage_detail
)

urlpatterns = [
    path('api/contacts/', contact_list, name='contact-list'),
    path('api/contacts/<int:pk>/', contact_detail, name='contact-detail'),
    
    path('api/chooseitems/', chooseitem_list, name='chooseitem-list'),
    path('api/chooseitems/<int:pk>/', chooseitem_detail, name='chooseitem-detail'),
    
    path('api/teammembers/', teammember_list, name='teammember-list'),
    path('api/teammembers/<int:pk>/', teammember_detail, name='teammember-detail'),
    
    path('api/partners/', partner_list, name='partner-list'),
    path('api/partners/<int:pk>/', partner_detail, name='partner-detail'),
    
    path('api/roadmapitems/', roadmapitem_list, name='roadmapitem-list'),
    path('api/roadmapitems/<int:pk>/', roadmapitem_detail, name='roadmapitem-detail'),

    path('api/contactmessage_list/', contactmessage_list, name='contactmessage_list'),
    path('api/contactmessage_list/<int:pk>/', contactmessage_detail, name='contactmessage_detail')
    
]
