import json

class GameStats:
    """Armazena dados estatísticos da Invasão Alienígena."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # Pontuação máxima lida do arquivo.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Inicializa os dados que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Carrega a pontuação máxima de um arquivo."""
        try:
            with open('high_score.json', 'r') as f:
                return int(json.load(f))
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        """Salva a pontuação máxima em um arquivo."""
        with open('high_score.json', 'w') as f:
            json.dump(self.high_score, f)
        self.level = 1
    