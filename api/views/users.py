from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models.user import User
from api.models.race import Race
from api.models.coach import Coach


class UserSerializer(serializers.ModelSerializer):
    following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "clerk_id",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "date_joined",
            "last_login",
            "following",
            "followers",
        )

    def get_following(self, obj):
        return list(obj.following.values("following_user_id", "created_at"))

    def get_followers(self, obj):
        return list(obj.followers.values("user_id", "created_at"))


class Profile(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request.user
        return User.objects.all_visible_users_for_user(user)

    @action(detail=True, methods=["GET"])
    def races(self, request, pk=None):
        from api.views.races import RaceSerializer

        user = self.get_object()
        print(user)
        races = Race.objects.filter(participants=user)
        serializer = RaceSerializer(races, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @action(detail=True, methods=['get'])
    # def coaches(self, request, pk=None):
    #     user = self.get_object()
    #     coaches = Coach.objects.filter(user=user)
    #     serializer = CoachSerializer(coaches, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
