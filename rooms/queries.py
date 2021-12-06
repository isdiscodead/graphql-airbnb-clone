from rooms.models import Room
from rooms.types import RoomListResponse


def resolve_rooms(self, info, page=1):
    if page < 1:
        page = 1
    page_size = 5  # 한 페이지에 들어갈 개수
    skipping = page_size * (page - 1)
    taking = page_size * page
    rooms = Room.objects.all()[skipping:taking]
    total = Room.objects.count()
    return RoomListResponse(arr=rooms, total=total)


def resolve_room(self, info, id):
    try:
        return Room.objects.get(id=id)
    except Room.DoesNotExist:
        return None