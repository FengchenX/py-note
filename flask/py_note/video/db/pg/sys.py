from db.pg import base


class VideoSysDB(base.SystemDB):
    def __init__(self, file):
        self.Sql = file