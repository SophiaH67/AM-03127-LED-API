from checksum import checksum_message


class DataPacket:
    def __init__(self, data: str):
        self.data = data

    def __str__(self):
        return f"<ID00>{self.data}{checksum_message(self.data)}<E>"
