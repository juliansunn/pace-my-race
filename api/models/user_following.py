from django.db import models


class UserFollowing(models.Model):
    user = models.ForeignKey(
        "api.User", related_name="following", on_delete=models.CASCADE
    )
    following_user = models.ForeignKey(
        "api.User", related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id", "following_user_id"], name="unique_followers"
            )
        ]

        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.id} follows {self.following_user.id}"
