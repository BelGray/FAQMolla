
class Configs:
    token: str
    admins = [685578986784686116, 1072379692318998598, 337530579803439107]
    default_color = 0xFFFFFF
    def __init__(self, key):
        """CONSTRICTOR"""
        self.token = key

    def is_admin(self, author_id: int):
        return True if author_id in Configs.admins else False

    def get_ru_community_role(self,id=1092161312336912384):
        return id

    def get_eng_community_role(self,id=1092162682926403765):
        return id

    def get_welcome_channel(self, id = 1092196394632216627):
        return id

    def get_rules_channel(self, id = 1078429568148439058):
        return id

    def get_ru_news_channel(self, id = 1078429568148439057):
        return id

    def get_eng_news_channel(self, id = 1092207387659730974):
        return id

    def get_ru_logs_channel(self, id = 1086310760034074664):
        return id

    def get_eng_logs_channel(self, id = 1092207696989667348):
        return id


