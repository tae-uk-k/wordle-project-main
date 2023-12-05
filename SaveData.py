import pickle

class saveData:

    def save_game_state(self,player_name, score):
        data = {
           'player_name': player_name,
           'score': score
           }
        with open('game_state.pkl', 'wb') as file:
            pickle.dump(data, file)
    def load_game_state(self):
        try:
            with open('game_state.pkl', 'rb') as file:
                data = pickle.load(file)
                return data['player_name'], data['score']
        except FileNotFoundError:
            return None, 0
    def start_game(self):
        self.player_name, self.score = self.load_game_state()

        if self.player_name is None:
            self.player_name = input("플레이어 이름을 입력하세요: ")
        if self.score is None:
            self.score=0

        print(f"안녕하세요, {self.player_name}! 현재 점수는 {self.score}점입니다.")
        
    def set_score(self, new_score):
        player_name, old_score = self.load_game_state()
        self.save_game_state(player_name, new_score)

    def get_score(self):
        _, score = self.load_game_state()
        return score

