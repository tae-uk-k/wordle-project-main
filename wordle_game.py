from Wordle import Wordle
from SaveData import saveData

s=saveData()
s.start_game()

w = Wordle()
ans = input("난이도를 입력하세요(쉬움 : 0, 보통 : 1, 어려움 : 2) : ")
w.setDifficulty(ans)
w.preSetting()
w.gamePlay()
turn = w.getTurn()

print(turn, "번째에 맞췄습니다. ")
s.save_game_state(s.player_name, s.score)








