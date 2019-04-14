from db.pg import base


class VideoSysDB(base.SystemDB):
    def __init__(self, file):
        self.Sql = file
    def AddVideo(self,video):
        cursor=self.conn.cursor()
        try:
            sql = """INSERT INTO video(id, name, url, "desc", thumb) VALUES('%s', '%s', '%s', '%s', '%s')""" \
            %(video['id'], video['name'], video['url'], video['desc'], video['thumb']) 
            cursor.execute(sql)
            # self.conn.commit()
        finally:
            cursor.close()

    def GetVideos(self, video={}):
        cursor =self.conn.cursor()
        try:
            args=''
            comma='WHERE'
            for k, v in video.items():
                if k == 'id':
                    args = "%s %s id='%s'" %(args, comma, v)
                    comma = "AND"
            
            sql="""SELECT * FROM video %s""" % args
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
               videos = {"id":row[0], "name":row[1], "url":row[2], "desc":row[3], "thumb":row[4]}
            return videos 
        finally:
            cursor.close()