from rest_framework import permissions, serializers, viewsets, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.city import City
from api.models.race import Race
from api.models.race_registration import RaceRegistration
from api.views.pagination import APIPaginator
from api.views.users import UserSerializer


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ("id", "name", "state", "latitude", "longitude")


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = (
            "id",
            "name",
            "link",
            "image",
            "description",
            "registration_open",
            "registration_deadline",
            "race_start",
            "type",
            "city",
            "participant_count",
            "favorite_count",
            "is_favorite",
        )

    participant_count = serializers.IntegerField(read_only=True)
    favorite_count = serializers.IntegerField(read_only=True)
    is_favorite = serializers.BooleanField(read_only=True)

    city = CitySerializer(read_only=True)


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
        qs = Race.objects.annotate_is_favorite(self.request.user)
        qs = qs.annotate_favorite_count()
        qs = qs.annotate_participant_count()

        if self.request.query_params.get("is_favorite") is not None:
            f = self.request.query_params.get("is_favorite").lower().capitalize()
            if f == "True":
                f = True
            elif f == "False":
                f = False
            qs = qs.filter(is_favorite=f)
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

    @action(detail=True, methods=["POST"], url_path="favorite")
    def favorite(self, request, pk=None):
        race = self.get_object()
        user = request.user
        race.favorites.add(user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["POST"], url_path="unfavorite")
    def unfavorite(self, request, pk=None):
        race = self.get_object()
        user = request.user
        race.favorites.remove(user)
        return Response(status=status.HTTP_200_OK)
