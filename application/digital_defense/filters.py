from rest_framework import filters


class PagesFilterByWebsite(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        website_id = request.query_params.get('website_id', None)
        queryset = queryset.filter(
            website_id=website_id
        )

        return queryset


class VulnerabilityFilterByWebsite(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        page_id = request.query_params.get('page_id', None)
        queryset = queryset.filter(
            page_id=page_id
        )

        return queryset.order_by('id')
