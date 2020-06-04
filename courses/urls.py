from django.urls import path
from .views import *

urlpatterns = [
    path('mine/', ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('<pk>/', CourseUpdateView.as_view(), name='course_edit'),
    path('<pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
]