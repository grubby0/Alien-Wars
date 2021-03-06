import highscore as hs


class GameStats():
    """跟踪游戏统计信息"""

    def __init__(self, settings):
        """初始化统计信息"""
        self.settings = settings
        self.reset_stats()

        # 游戏刚启动时处于静止状态，点击Play按钮激活
        self.game_active = False

        # 在任何情况下都不应重置最高得分
        self.high_score = hs.load_json()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
