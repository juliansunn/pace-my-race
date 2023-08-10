from rest_framework import permissions, serializers, viewsets, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.training_group import PacingGroup
from api.views.pagination import APIPaginator
from api.views.users import UserSerializer


class PacingGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacingGroup
        fields = "__all__"


class PacingGroupViewSet(viewsets.ModelViewSet):
    model = PacingGroup
    serializer_class = PacingGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = APIPaginator

    def get_queryset(self):
        qs = PacingGroup.objects.all()
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
    def members(self, request, pk=None):
        training_group = self.get_object()
        members = training_group.members.all()
        results = self.paginate_queryset(members)
        serializer = UserSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)
