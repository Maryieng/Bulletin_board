from rest_framework.pagination import PageNumberPagination


class AnnouncementPaginator(PageNumberPagination):
    """ пагинация для вывода """
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 4
