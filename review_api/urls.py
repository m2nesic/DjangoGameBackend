from django.urls import path,include
from .views import CreateReview, DeleteReview, EditReview, ReviewList, ReviewDetail, ReviewListDetailfilter , AdminReviewDetail

app_name = 'review_api'
urlpatterns = [
    path('reviews/<str:pk>/', ReviewDetail.as_view(), name='detailreview'),
    path('search/', ReviewListDetailfilter.as_view(), name='searchreview'),
    path('',ReviewList.as_view(), name = 'listcreate'), #homepage 
    path('game/', include('game_api.urls', namespace='game_api')),
    path('admin/create/', CreateReview.as_view(), name='createreview'),
    path('admin/edit/reviewdetail/<int:pk>/', AdminReviewDetail.as_view(), name='admindetailreview'),
    path('admin/edit/<int:pk>/', EditReview.as_view(), name='editreview'),
    path('admin/delete/<int:pk>/', DeleteReview.as_view(), name='deletereview')
]
