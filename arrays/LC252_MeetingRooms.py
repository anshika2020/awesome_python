from typing import List


class LC252MeetingRooms:

    @staticmethod
    def canattendallmeetings(intervals: List[List[int]]):
        sorted(intervals)
        for i in range(len(intervals)-1):
            if intervals[i][1] >intervals[i + 1][0]:
                return False
        return True


if __name__ == "__main__":
    rooms = LC252MeetingRooms()
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(rooms.canattendallmeetings(intervals))
