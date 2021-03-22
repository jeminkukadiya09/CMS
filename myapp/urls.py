from django.urls import path
from . import views

urlpatterns = [
    path('person', views.person, name="person"),
    path('persondetail', views.persondetail, name="persondetail"),
    path('customer', views.customer, name="customer"),
    path('case', views.case, name="case"),
    path('state', views.state, name="state"),
    path('casedetailpage', views.case_detail_page, name="casedetailpage"),
    path('casedetailpageedit/<int:case_id>', views.case_detail_page_edit, name="casedetailpageedit"),
    path('case_update/<int:case_id>', views.case_update, name="case_update"),
    path('customer_list<str:data_object>', views.customer_list, name="customer_list"),
    path('lawyerform', views.lawyerform, name="lawyerform"),
    path('customerform', views.customerform, name="customerform"),
    path('case_full_detail<int:case_id>/', views.case_full_detail, name="case_full_detail"),
    path('customer_full_detail<int:case_id>/', views.customer_full_detail, name="customer_full_detail"),
    path('lawyer_full_detail<int:case_id>/', views.lawyer_full_detail, name="lawyer_full_detail"),
    path('all_customer/', views.all_customer, name="all_customer"),
    path('all_lawyer/', views.all_lawyer, name="all_lawyer"),
    path('lawyer_full_detail/', views.lawyer_full_detail, name="lawyer_full_detail"),
    path('same_color<str:state_name>/', views.same_color, name="same_color"),
    path('excel/', views.excel, name="excel"),
    path('Earning/', views.Earning, name="Earning"),
    path('people', views.people, name="people"),
    path('lawyer_update/<int:lawyer_id>', views.lawyer_update, name='lawyer_update'),
    path('customer_update/<int:customer_id>', views.customer_update, name='customer_update'),
    path('alluser/', views.alluser, name='alluser'),    
    
    path('lawyer_full_detail_all<int:lawyer_id>/', views.lawyer_full_detail_all, name='lawyer_full_detail_all'),
    path('customer_full_detail_all<int:customer_id>/', views.customer_full_detail_all, name='customer_full_detail_all'),
    
]
