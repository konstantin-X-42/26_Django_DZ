from django.urls import path
from catalog.views import (
    ProductListView,
    CategoriesListView,
    OrdersTemplateView,
    ContactsTemplateView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,  # -26 Импортируем контроллер обновления
    ProductDeleteView   # -26- Импортируем контроллер удаления
)

# исключаем одноименные конфликты
app_name = 'catalog'

urlpatterns = [
    # маршрут для домашней страницы 1
    path('', ProductListView.as_view(), name='21-2_home1'),

    # маршрут для Категорий страница 2
    path('categories/', CategoriesListView.as_view(), name='21-2_home2'),

    # маршрут для Заказов страница 3
    path('orders/', OrdersTemplateView.as_view(), name='21-2_home3'),

    # маршрут для страницы 4 контактов с закрывающим /
    path('contacts/', ContactsTemplateView.as_view(), name='21-2_home4'),

    # -24-Задание 1 Маршрут URL, отвечает за динамическое отображение страницы конкретного товара
    # (например, карточки товара с его подробным описанием, ценой и картинкой).
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Маршрут для создания товара
    path('products/create/', ProductCreateView.as_view(), name='create_product'),

    # -26- Маршрут для редактирования товара
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='update_product'),

    # -26- Маршрут для удаления товара
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
]


#  -----------25-------------


# from django.urls import path
# from catalog.views import (
#     ProductListView,
#     CategoriesListView,
#     OrdersTemplateView,
#     ContactsTemplateView,
#     ProductDetailView,
#     ProductCreateView
# )
#
# # исключаем одноименные конфликты
# app_name = 'catalog'
#
# urlpatterns = [
#     # маршрут для домашней страницы 1
#     path('', ProductListView.as_view(), name='21-2_home1'),
#
#     # маршрут для Категорий страница 2
#     path('categories/', CategoriesListView.as_view(), name='21-2_home2'),
#
#     # маршрут для Заказов страница 3
#     path('orders/', OrdersTemplateView.as_view(), name='21-2_home3'),
#
#     # маршрут для страницы 4 контактов с закрывающим /
#     path('contacts/', ContactsTemplateView.as_view(), name='21-2_home4'),
#
#     # -24-Задание 1
#     path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
#
#     # Маршрут для создания товара
#     path('products/create/', ProductCreateView.as_view(), name='create_product'),
# ]
