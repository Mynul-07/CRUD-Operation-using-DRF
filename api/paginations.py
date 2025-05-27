# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response


# class CustomPagination(PageNumberPagination):
#     page_size_query_param = 'page_size'
#     page_query_param = 'page-num'
#     max_page_size = 2
    
#     def get_paginated_response(self, data):
#         return Response({
#             'next': self.get_next_link(),
#             'previous' : self.get_previous_link(),
#             'count': self.page.paginator.count,
#             'page_size': self.page_size,
#             'results': data
            
#         })

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    # Set the default number of items per page to 2
    page_size = 2

    # Allows client to override page_size, e.g., ?page_size=1
    page_size_query_param = 'page_size'

    # The query parameter for specifying the page number
    page_query_param = 'page-num'

    # Ensures that the client cannot request more than 2 items per page
    # This was already correctly set in your provided code.
    max_page_size = 2

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous' : self.get_previous_link(),
            'count': self.page.paginator.count,
            # self.page_size here will reflect the actual page size used for the request
            # (either the default 2, or what the client requested if <= max_page_size)
            'page_size': self.page_size,
            'results': data
        })