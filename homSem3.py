class Group:
    def __init__(self, name):
        self.name = name

class Stream:
    def __init__(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

class StreamComparator:
    def compare(self, stream1, stream2):
        return len(stream1.groups) - len(stream2.groups)

class StreamService:
    def sort_streams(self, streams, comparator):
        return sorted(streams, key=lambda x: len(x.groups), reverse=True)

class Controller:
    def __init__(self, stream_service):
        self.stream_service = stream_service

    def sort_streams(self, streams):
        return self.stream_service.sort_streams(streams, StreamComparator())

# Пример использования
if __name__ == "__main__":
    group1 = Group("Group 1")
    group2 = Group("Group 2")
    group3 = Group("Group 3")

    stream1 = Stream()
    stream1.add_group(group1)
    stream1.add_group(group2)

    stream2 = Stream()
    stream2.add_group(group3)

    stream_service = StreamService()
    controller = Controller(stream_service)

    streams = [stream1, stream2]
    sorted_streams = controller.sort_streams(streams)

    for stream in sorted_streams:
        print("Поток с {} группой".format(len(stream.groups)))
