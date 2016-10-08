#!/usr/bin/env python3
###################################################################
#
#   CSSE1001/7030 - Assignment 2
#
#   Student Username: s4378702
#
#   Student Name: Youwen Mao
#
###################################################################

###################################################################
#
# The following is support code. DO NOT CHANGE.

from a2_support import *

# End of support code
################################################################

# Write your code here

class GameObject(object):
    """
    Manage all the object in the game.
    """
    def __init__(self,name,position):
        """
        Consturctor
        
        GameObject.__init__(GameObject, str, tuple)
        """
        self._name = name
        self._position = position

    def set_position(self,position):
        """
        Set gameobject position.

        GameObject.set_position(GameObject, tuple)
        """
        x,y = position
        if x%1 == 0 and y%1 ==0:
            self._position = position

    def get_position(self):
        """
        Get gameobject position.

        GameObject.get_position(GameObject) -> (int, int)
        """
        return self._position

    def set_name(self,name):
        """
        Set gameobject name.

        GameObject.set_position(GameObject, str)
        """
        self._name = name

    def get_name(self):
        """
        Get gameobject name.

        GameObject.get_name(GameObject) -> str
        """
        return self._name

    def __str__(self):
        """
        Returns a human readable representation of this instance.

        GameObject.__str__(GameObject) -> str
        """
        return GAME_OBJECT_FORMAT.format(self._name,self._position)

class Pokemon(GameObject):
    """
    Manage pokemons.
    """
    def __init__(self,name,position,terrain):
        """
        Consturctor
        
        Pokemon.__init__(Pokemon, str, tuple, str)
        """
        super().__init__(name,position)
        self._terrain = terrain

    def set_terrain(self,terrain):
        """
        Set pokemon terrain.

        Pokemon.set_Terrain(Pokemon, str)
        """
        self._terrain = terrain

    def get_terrain(self):
        """
        Get pokemon terrain.

        Pokemon.get_Terrain(Pokemon) -> str
        """
        return self._terrain

    def __str__(self):
        """
        Returns a human readable representation of this instance.

        Pokemon.__str__(Pokemon) -> str
        """
        return POKEMON_FORMAT.format(self._name,self._position,self._terrain)

class Wall(GameObject):
    """
    Manage pokemons.
    """
    pass

class Player(GameObject):
    """
    Manage the player
    """
    def __init__(self,name):
        """
        Consturctor
        
        Plyaer.__init__(Player, str)
        """
        self._name = name
        self._position = None
        self._list = []
        self._dex = Dex(self._list)

    def get_pokemons(self):
        """
        Get pokemon caught by player.

        Player.get_pokemons(Player) -> list
        """
        return self._list

    def get_dex(self):
        """
        Get dex of player.

        Player.get_dxe(Player) -> Dex
        """
        return self._dex
    
    def reset_pokemons(self):
        """
        Reset the list of pokemon player caught and the dex of player.

        Player.reset_pokemons(Player)
        """
        self._list.clear()
        self._dex = Dex(self._list)

    def register_pokemon(self, pokemon):
        """
        Register the pokemon.

        Player.register_pokemon(Player, Pokemon)
        """
        self._list.append(pokemon)
        self._dex.register(pokemon.get_name())
        
    def __str__(self):
        """
        Returns a human readable representation of this instance.

        Player.__str__(Player) -> str
        """
        return PLAYER_FORMAT.format(self._name,self._position,len(self._list))
    
class Dex(object):
    """
    Manage the dex.
    """
    def __init__(self, pokemon_names):
        """
        Consturctor
        
        Dex.__init__(Dex, list)
        """
        self._pokemons ={}
        self.expect_pokemons(pokemon_names)

    def expect_pokemons(self, pokemon_names):
        """
        Expect the pokemons.

        Dex.expect_pokemons(Dex, list)
        """
        for i in pokemon_names:
            self._pokemons[i] = False
    
    def expect_pokemons_from_dex(self,other_dex):
        """
        Expect the pokemons for other dex.

        Dex.expect_pokemons_from_dex(Dex, Dex)
        """
        pokemonslist = []
        for i in other_dex.get_pokemons():
            pokemonslist.append(i[0])
        self.expect_pokemons(pokemonslist)

    def register(self,pokemon_name):
        """
        Register the pokemons in dex and return True iff the pokemon has been registered, else False.

        Dex.register(Dex, list) -> bool
        """
        try:
            if self._pokemons[pokemon_name]:
                return True
            else:
                self._pokemons[pokemon_name] = True
                return False
        except Exception as s:
            raise UnexpectedPokemonError(str(DexError(s))+" is not expected by this Dex")

    def register_from_dex(self,other_dex):
        """
        Register the pokemons from other dex in this dex.

        Dex.register(Dex, Dex)
        """
        other_dex = other_dex.get_registered_pokemons()
        exist = []
        for i in other_dex:
            if i in self.get_unregistered_pokemons():
                exist.append(i)
        for x in exist:
            self.register(x)

    def get_pokemons(self):
        """
        Get all pokemons in the dex.

        Dex.get_pokemons(Dex) -> tuple
        """
        pokemon_list = []
        for i in sorted(list(self._pokemons)):
            pokemon_list.append((i,self._pokemons[i]))
        return pokemon_list
    def get_registered_pokemons(self):
        """
        Get all registered pokemons in the dex.

        Dex.get_get_registered_pokemons(Dex) -> list
        """
        rgd_pokemons = []
        for i in sorted(list(self._pokemons)):
            if self._pokemons[i]:
                rgd_pokemons.append(i)
        return rgd_pokemons
    def get_unregistered_pokemons(self):
        """
        Get all unregistered pokemons in the dex.

        Dex.get_get_unregistered_pokemons(Dex) -> list
        """
        urgd_pokemons = []
        for i in sorted(list(self._pokemons)):
            if not self._pokemons[i]:
                urgd_pokemons.append(i)
        return urgd_pokemons
    def __len__(self):
        """
        Return the numbers of pokemons in the dex.

        Dex.__len__(Dex) -> int
        """
        return len(self._pokemons)

    def __contains__(self,name):
        """
        Return True iff the name of pokemon exist in Dex, else False.

        Dex.__contains__(Dex, str) -> bool
        """
        if self._pokemons[name]:
            return True
        else:
            return False

    def __str__(self):
        """
        Returns a human readable representation of this instance.

        Dex.__str__(Dex) -> str
        """
        rgd_pokemons = ""
        urgd_pokemons = ""
        for i in self.get_registered_pokemons():
            if i is self.get_registered_pokemons()[-1]:
                rgd_pokemons += i
            else:
                rgd_pokemons += i
                rgd_pokemons += ", "
        for s in self.get_unregistered_pokemons():
            if s is self.get_unregistered_pokemons()[-1]:
                urgd_pokemons += s
            else:
                urgd_pokemons += s
                urgd_pokemons += ", "
        self._string = str(DEX_FORMAT.format(len(self.get_registered_pokemons()),rgd_pokemons,len(self.get_unregistered_pokemons()),urgd_pokemons))
        return self._string

class Level(object):
    """
    Manage the Level.
    """
    def __init__(self,player,data):
        """
        Consturctor
        
        Level.__init__(Level, Player, dict)
        """
        self._player = player
        self._data = data
        player_position = (self._data["player"][0], self._data["player"][0])
        pkml = []
        for i in self._data["pokemons"]:
            pkml.append(i["name"])
        self._dex = Dex(pkml)
        self._player.get_dex().expect_pokemons(pkml)
        self._cell = {}
        for s in self._data["pokemons"]:
            self._cell[(s["position"][0],s["position"][1])] = Pokemon(s["name"],s["position"],self._data["terrain"])###
        self._wall = {}
        for x in self._data["walls"]:
            self._wall[x] = "wall"
        if not is_position_valid(player_position, self.get_size()):
            raise InvalidPositionError
        for n in list(self._wall):
            if not is_wall_position_valid(n, self.get_size()):
                raise InvalidPositionError
        xcount = 0
        ycount = 0
        x, y= self.get_size()
        while xcount != x:
            self._wall[(xcount,-0.5)] = "wall"
            self._wall[(xcount,y-0.5)] = "wall"
            xcount += 1
        while ycount != y:
            self._wall[(-0.5,ycount)] = "wall"
            self._wall[(x-0.5,ycount)] = "wall"
            ycount += 1
    def get_size(self):
        """
        Get the grid size of this level.
        
        Level.get_size(Level) -> tuple
        """
        return (self._data["rows"], self._data["columns"])
    
    def get_terrain(self):
        """
        Get the terrain of this level.
        
        Level.get_terrain(Level) -> str
        """
        return self._data["terrain"]

    def get_dex(self):
        """
        Get the Dex of this level
        
        Level.get_dex(Level) -> Dex
        """
        return self._dex


    def get_starting_position(self):
        """
        Get the starting point of player of this level.
        
        Level.get_starting_position(Level) -> str
        """
        return self._data["player"]

    def is_obstacle_at(self,position):
        """
        Return True iff there is a wall, else False.
        
        Level.is_obstacle_at(Level. tuple) -> bool
        """
        if position in self.get_obstacles():
            return True
        else:
            return False

    def get_obstacles(self):
        """
        Get all the walls existed in this level.
        
        Level.get_obstacles(Level) -> list
        """
        return list(self._wall)

    def get_pokemons(self):
        """
        Get all the pokemons existed in this level.
        
        Level.get_pokemons(Level) -> Pokemon
        """
        pkl = []
        for i in list(self._cell):
            pkl.append(self._cell[(i[0],i[1])])
        return pkl

    def get_pokemon_at(self,position):
        """
        Return the pokemon exist in this position, else None.
        
        Level.get_pokemon_at(Level, tuple) -> Pokemon
        """
        pkm = None
        if position in self._cell:
            pkm = self._cell[position]
        return pkm
    def catch_pokemon_at(self,position):
        """
        Catch and register the pokemon in this position and return it.
        
        Level.catch_pokemon_at(Level, tuple) -> Pokemon
        """
        try:
            if is_position_valid(position, self.get_size()):
                pass
            else:
                raise InvalidPositionError(x)
            pkm = self.get_pokemon_at(position)
            if pkm is not None:
                self.get_dex().register(pkm.get_name())
                self._player.register_pokemon(pkm)
                x,y = pkm.get_position()
                del self._cell[(x,y)]
            return pkm
        except Exception as x:
            raise InvalidPositionError(x)

    def is_complete(self):
        """
        Returns True iff pokemon with name is registered in this Dex, else False.
        
        Level.is_complete(Level) -> bool
        """
        if self.get_dex().get_unregistered_pokemons() == []:
            return True
        else:
            return False

    
class Game(object):
    """
    Manage the game.
    """
    def __init__(self):
        """
        Consturctor
        
        Game.__init__(Game)
        """
        self._player = Player(DEFAULT_PLAYER_NAME)
        self._levels_list = []
        self._level = -1
        self._game_file = None
        self._data = []
        self._pkmc = {}
    def load_file(self,game_file):
        """
        Loads a game from a file.
        
        Game.load_file(Game, str)
        """
        try:
            self._levels_list = []
            self._game_file = load_game_file(game_file)
            for i in self._game_file["levels"]:
                self._data.append(i)
                self._levels_list.append(Level(self._player,i))
            self._level = -1
            self._pkmc = {}
        except:
            pass
        
    def load_url(self,game_url):
        """
        Loads a game from a url.
        
        Game.load_erl(Game, str)
        """
        try:
            self._levels_list = []
            self._game_file = load_game_url(game_url)
            for i in self._game_file["levels"]:
                self._data.append(i)
                self._levels_list.append(Level(self._player,i))
            self._level = -1
            self._pkmc = {}
        except:
            pass
    
    def start_next_level(self):
        """
        Attempts to start the next level of the game, Returns True iff the game is completed, else False.
        
        Game.start_next_level(Game) -> bool
        """
        if self.is_complete():
            return True
        else:
            if (self._level+1) != len(self._levels_list):
                previous = None
                if self.get_level() != None:
                    previous = self.get_level().get_dex().get_registered_pokemons()
                self._level += 1
                ###
                
                for i in self._data[self._level]['walls']:
                    if not is_wall_position_valid(i,self.get_level().get_size()):
                        raise InvalidPositionError()
                for s in self._data[self._level]['pokemons']:
                    if not is_cell_position_valid(s['position'],self.get_level().get_size()):
                        raise InvalidPositionError()
                if not is_cell_position_valid(self._data[self._level]['player'],self.get_level().get_size()):
                    raise InvalidPositionError()
                
                ###
                self._player.get_dex().expect_pokemons(self.get_level().get_dex().get_unregistered_pokemons())
                if previous != None:
                    '''for x in previous:'''
                    for x in list(self._pkmc):
                        if x in self.get_level().get_dex().get_unregistered_pokemons():
                            self.get_level().get_dex().register(x)
                self._player.set_position(self.get_level().get_starting_position())
            return False

    def get_player(self):
        """
        Returns the player of the game.
        
        Game.get_player(Game) -> Player
        """
        return self._player

    def get_level(self):
        """
        Returns the current level, an instance of Level, else None if the game hasn’t started.
        
        Game.get_level(Game) -> bool
        Game.get_level(Game) -> dict
        """
        if self._level == -1:
            return None
        else:
            return self._levels_list[self._level]

    def __len__(self):
        """
        Returns the total number of levels in the game.
        
        Game.__len__(Game) -> int
        """
        return len(self._game_file["levels"])
    
    def is_complete(self):
        """
        Returns True iff no levels remain incomplete, else False.
        
        Game.is_complete(Game) -> bool
        """
        if len(self._levels_list)-1 == self._level:
            return True
        else:
            return False

    def move_player(self,direction):
        """
        Attempts to move the player in the given direction. Returns whatever the player would hit in attempting to move, else None.
        
        Game.move_player(Game, str) -> Pokemon
        Game.move_player(Game, str) -> Wall
        """
        try:
            position = None
            x1,y1 = DIRECTION_DELTAS[direction]
            x2,y2 = DIRECTION_WALL_DELTAS[direction]
            x,y = self._player.get_position()
            position_wall = (x2+x, y2+y)
            if_wall = False
            if self.get_level().is_obstacle_at(position_wall):
                if_wall = True
                position = Wall("#",position_wall)
            if not if_wall:
                if is_position_valid((x1+x,y1+y),self.get_level().get_size()):
                    position_pokemon = (x1+x, y1+y)
                    position = self.get_level().get_pokemon_at(position_pokemon)
                    if position is not None:
                        self.get_level().catch_pokemon_at(position_pokemon)
                        self._pkmc[position.get_name()] = None
                    self._player.set_position(position_pokemon)
            return position
        except Exception as x:
            raise DirectionError(x)

"""
if __name__ == "__main__":
    import gui
    gui.main()
"""
