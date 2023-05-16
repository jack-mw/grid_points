from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from . import serializers, services


class GridPointsView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    def create(self, request, *args, **kwargs):
        serializer = serializers.GridPointsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        closest_points = services.find_closest()
        return Response(
            {
                "closest_points": closest_points,
            },
            status=status.HTTP_201_CREATED,
        )
