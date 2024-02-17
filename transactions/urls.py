from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from transactions import views

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionViewSet,'transactions')
router.register(r'categories', views.CategoryViewSet,'categories')
router.register(r'users', views.UserViewSet,'users')
router.register(r'cards', views.CardViewSet,'cards')
router.register(r'installments', views.InstallmentsViewSet,'installments')
# router.register(r'getUserByName', views.getUserByName,'getUserByName')
# router.register(r'getTransactionsByUser', views.getTransactionsByUser,'getTransactionsByUser')

urlpatterns = [
    path("api/",include(router.urls)),
    path('docs/', include_docs_urls(title='Finanzas API')),
    # path('api/v1/transactions/', views.getTransactionsByUser.as_view({'get': 'list'}), name='get_transactions_by_user'),
]

