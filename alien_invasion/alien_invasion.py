import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
# 管理游戏资源和行为的类
    def __init__(self):
# 初始化游戏并创建游戏资源
        pygame.init()
# 设置帧率属性
        self.clock = pygame.time.Clock()
# 创建1个1200*800的游戏窗口并将标题设为Alien Invasion
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height 
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

# 拆分成keydown
    def _check_events_keydown(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

# 拆分成keyup
    def _check_events_keyup(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


# 响应按键和鼠标事件，将事件与run_game分离
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
# 检查按键向右，如果停止，飞船不移动
            elif event.type ==pygame.KEYDOWN:
                self._check_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_events_keyup(event)

    def _update_screen(self):
# 设置背景颜色,只能放在循环里，否则背景颜色只出现1次
        self.screen.fill(self.settings.bg_color)
# 绘制飞船
        self.ship.blitme()
# 让最近绘制的屏幕可见
        pygame.display.flip()   


# 开始游戏主循环
    def run_game(self):
# 开始侦听键盘和鼠标事件
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
# 设置帧率为60,只能放在循环里，否则只在游戏开始前运行1次，循环后帧率就不受控制了
            self.clock.tick(60)


if __name__ == "__main__":
# 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()

