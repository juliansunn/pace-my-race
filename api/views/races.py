from rest_framework import permissions, serializers, viewsets, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.race import Race
from api.models.race_registration import RaceRegistration
from api.views.pagination import APIPaginator
from api.views.users import UserSerializer


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = "__all__"


class RaceRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceRegistration
        fields = ("race", "user", "registration_time")

    user = UserSerializer(read_only=True)
    race = RaceSerializer(read_only=True)


class RaceViewSet(viewsets.ModelViewSet):
    model = Race
    serializer_class = RaceSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = APIPaginator

    def get_queryset(self):
        qs = Race.objects.all()
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

    @action(detail=True, methods=["POST"])
    def signup(self, request, pk=None):
        race = self.get_object()
        user = request.user

        if race.participants.filter(raceregistration__user=user).exists():
            return Response(
                {"detail": "You are already signed up for this race."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        rr = RaceRegistration(race=race, user=user)
        rr.save()

        serializer = RaceRegistrationSerializer(rr)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
