from rest_framework import permissions, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.coach import Coach

from api.views.pagination import APIPaginator
from api.views.users import UserSerializer
from api.models.race import Race


class CoachSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Coach
        fields = ("id", "bio", "expertise", "user")


class CoachViewSet(viewsets.ModelViewSet):
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = APIPaginator

    def get_queryset(self):
        return Coach.objects.filter(coach_type=Coach.CoachType.PACE)

    def list(self, request, *args, **kwargs):
        coaching_groups = self.get_queryset()
        results = self.paginate_queryset(coaching_groups)
        serializer = self.get_serializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        race = self.get_object()
        serializer = self.get_serializer(race)
        return Response(serializer.data)

    @action(methods=["GET"], detail=True)
    def races(self, request, pk=None):
        races = Race.objects.filter(
            race_groups__in=self.get_object().coaching_groups.all(), is_active=True
        ).order_by("-race_start")
        results = self.paginate_queryset(races)
        serializer = Race(results, many=True)
        return self.get_paginated_response(serializer.data)
