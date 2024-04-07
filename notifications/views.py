from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from notifications.models import Notification
from notifications.serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        user = request.user
        notifications = Notification.objects.filter(user=user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)


@api_view(http_method_names=["GET"])
@permission_classes((permissions.IsAdminUser,))
def get_notification_by_user(request, **kwargs):
    notifications = Notification.objects.filter(user=kwargs.get("user_id")).all()
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)


