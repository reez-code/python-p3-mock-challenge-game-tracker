class Game:
    average = {}
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "_title") and self._title is not None:
            raise AttributeError("Title cannot be changed after instantiation")
        else:
            if isinstance(title, str) and len(title):
                self._title = title
            else:
                raise ValueError("Title must be a non-empty string.")


    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in Result.all if result.game == self]))

    def average_score(self, player):
        scores = [result.score for result in Result.all if result.player == player]
        average = sum(scores) / len(scores)
        return average
    
    
class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and  2 <= len(username) <= 16:
            self._username = username
        else:
            raise ValueError("The username must be a string between 2 and 16 characters")

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return  list(set([result.game for result in Result.all if result.player == self]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        games = [result.game for result in Result.all if result.player == self]
        return games.count(game)
    
    @classmethod
    def average_score(self, player):
        scores = [result.score for result in Result.all if result.player == player]
        average = sum(scores) / len(scores)
        return average

    @classmethod
    def highest_scored(cls, game):
        scores = [cls.average_score(result.player) for result in Result.all if result.game == game]
        highest_score = max(scores)
        player = [result.player for result in Result.all if cls.average_score(result.player) == highest_score]
        return player[0]
  

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, "_score") and self._score is not None:
            raise AttributeError("Score cannot be changed after instantiation")
        else:
            if isinstance(score, int) and 1 <= score <= 5000:
                self._score = score
            else:
                raise ValueError("The score must be an integer between 1 and 5000")
            
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise ValueError("player must be an instance of the Player class")
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        else:
            raise ValueError("game must be an instance of the Game class")