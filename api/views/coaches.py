from rest_framework import permissions, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.training_group import PacingGroup
from api.views.pagination import APIPaginator
from api.views.users import UserSerializer
from api.models.pacer import Pacer
from api.models.race import Race


class PacerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Pacer
        fields = ("id", "bio", "expertise", "user")


class PacerViewSet(viewsets.ModelViewSet):
    model = PacingGroup
    serializer_class = PacerSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = APIPaginator

    def get_queryset(self):
        qs = Pacer.objects.all()
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
