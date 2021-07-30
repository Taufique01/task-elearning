from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from elearning import settings
from .views import HomePageView, EducatorCourseView, LearnerEnrollmentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/educator/', EducatorCourseView.as_view(), name='educator_api'),
    path('api/learner/', LearnerEnrollmentView.as_view(), name='learner_api'),


] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
