from django.conf.urls import url
from . import views


app_name='sudoku'

urlpatterns= [
    url(r'^$',views.SudokuSolve.as_view(),name='sudoku'),
    url(r'fill/$',views.FillBoard.as_view(),name='FillBoard'),
    # url(r'^search/',views.solution.as_view(),name='solution')
]
