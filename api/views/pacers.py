from rest_framework import permissions, serializers, viewsets, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.coach import Coach
from api.views.coaches import CoachSerializer
from api.views.pagination import APIPaginator
from api.models.race import Race
from api.models.race_type import RaceType


class RaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceType
        fields = ("distance", "surface", "description", "distance_unit")


class PacerViewSet(viewsets.ModelViewSet):
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = APIPaginator
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_queryset(self):
        qs = Coach.objects.filter(coach_type=Coach.CoachType.PACE)
        return qs

    def list(self, request, *args, **kwargs):
        pacing_groups = self.get_queryset()
        print(pacing_groups)
        results = self.paginate_queryset(pacing_groups)
        print("results", results)
        serializer = self.get_serializer(results, many=True)
        print(serializer.data)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        race = self.get_object()
        serializer = self.get_serializer(race)
        return Response(serializer.data)

    @action(methods=["GET"], detail=True)
    def races(self, request, pk=None):
        races = Race.objects.filter(
            race_groups__in=self.get_object().pacing_groups.all(), is_active=True
        ).order_by("-race_start")
        results = self.paginate_queryset(races)
        serializer = Race(results, many=True)
        return self.get_paginated_response(serializer.data)
