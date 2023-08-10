from rest_framework import permissions, serializers, viewsets, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.training_group import TrainingGroup
from api.views.pagination import APIPaginator
from api.views.users import UserSerializer


class TrainingGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingGroup
        fields = "__all__"


class TrainingGroupViewSet(viewsets.ModelViewSet):
    model = TrainingGroup
    serializer_class = TrainingGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = APIPaginator

    def get_queryset(self):
        qs = TrainingGroup.objects.all()
        return qs

    def list(self, request, *args, **kwargs):
        races = self.get_queryset()
        results = self.paginate_queryset(races)
        serializer = self.get_serializer(results, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):
        race = self.get_object()
        serializer = self.get_serializer(race)
        return Response(serializer.data)

    @action(methods=["GET"], detail=True)
    def races(self, request, pk=None):
        training_group = self.get_object()
        Race.objects.filter(pacing_group)
        members = training_group.members.all()
        results = self.paginate_queryset(members)
        serializer = UserSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
