import random as rn


class Pokemon:
    # Starts the pokemon off with standard stats
    def __init__(self, name, type, level=5):
        stat_inc_per_level = .3 * level
        self.name = name
        self.level = level
        self.type = type
        self.hp = int(10 * stat_inc_per_level)
        self.maxhp = self.hp
        self.attackstat = int(7 + stat_inc_per_level)
        self.defensestat = int(2 + (.8 * stat_inc_per_level))
        self.knockedOut = False
        if "Munchlax" == self.name:
            self.moveset = ["Lick", "Tackle", "Defense Curl", None]
        elif "Pichu" == self.name:
            self.moveset = ["Thunder Shock", "Tail Whip", "Sweet Kiss", None]
        elif "Igglybuff" == self.name:
            self.moveset = ["Sing", "Pound", "Defense Curl", None]
        elif "Togepi" == self.name:
            self.moveset = ["Growl", "Pound", "Sweet Kiss", "Life Dew"]
        elif "Wynaut" == self.name:
            self.moveset = ["Counter", "Splash", "Charm", None]
        elif "Azurill" == self.name:
            self.moveset = ["Splash", "Water Gun", "Tail Whip", None]
        elif "Magby" == self.name:
            self.moveset = ["Smog", "Ember", "Leer", None]
        elif "Smoochum" == self.name:
            self.moveset = ["Lick", "Pound", "Confusion", None]
        elif "Bonsly" == self.name:
            self.moveset = ["Rock Throw", "Fake Tears", "Flail", None]
        elif "MimeJr" == self.name:
            self.moveset = ["Pound", "Confusion", None, None]
        elif "Cleffa" == self.name:
            self.moveset = ["Splash", "Pound", "Sing", "Sweet Kiss"]
        elif "Elekid" == self.name:
            self.moveset = ["Leer", "Thunder Shock", "Quick Attack", None]

    def __repr__(self):
        # Printing a Pokemon object tells you all the details of that Pokemon
        return """{name} is level {level} and is a {type} type. 
They currently have {hp} hp, {attack} attack, and {defense} defense.
Their moves are: 
    {a}     {b} 
    {c}     {d}""".format(name=self.name, level=self.level, type=self.type,
                      hp=self.hp, attack=self.attackstat, defense=self.defensestat, a=self.moveset[0],
                      b=self.moveset[1], c=self.moveset[2], d=self.moveset[3])

    def typeAdvantage(self, opponent):
        if self.type == "electric" and (opponent.type == "water"):
            return True
        elif self.type == "water" and (opponent.type == "rock" or opponent.type == "fire"):
            return True
        elif self.type == "rock" and (opponent.type == "electric"):
            return True

    def typeDisadvantage(self, opponent):
        if self.type == "water" and (opponent.type == "electric"):
            return True
        elif self.type == "rock" and (opponent.type == "water"):
            return True
        elif self.type == "fire" and (opponent.type == "water"):
            return True
        elif self.type == "electric" and (opponent.type == "rock"):
            return True

    def getKnockedOut(self):
        # Changes condition of knocked out to true
        self.knockedOut = True
        # Makes it so that the minimum health a Pokemon can have is 0
        if self.hp != 0:
            self.hp = 0
        print("{name} has been knocked out!".format(name=self.name))

    def cpuAttackOpponent(self, opponent=None):
        # This function determins the attack used and calculates damage
        if self.knockedOut == True:
            print("{name} is knocked out and can't attack".format(name=self.name))
            return
        attacks = ["Lick", "Tackle", "Defense Curl", "Thunder Shock",
                   "Tail Whip", "Sing", "Pound", "Growl", "Life Dew",
                   "Counter", "Splash", "Charm", "Sweet Kiss",
                   "Water Gun", "Smog", "Ember", "Leer", "Lick",
                   "Confusion", "Rock Throw", "Fake Tears", "Flail",
                   "Thunder Shock", "Quick Attack"]
        move = self.moveset[0]
        while move not in self.moveset:
            move = input("""
Please pick a valid move
{a}      {b}
{c}      {d}
Please pick a move: """.format(a=self.moveset[0], b=self.moveset[1], c=self.moveset[2], d=self.moveset[3],
                               name=self.name))
        if move not in attacks:
            print("That's not a valid attack!")
            self.attackOpponent(opponent)
            return
        if self.typeAdvantage(opponent) == True:
            opponent.hp = opponent.hp - (2 * (self.attackstat - opponent.defensestat))
        elif self.typeDisadvantage(opponent) == True:
            opponent.hp = opponent.hp - (int(.5 * (self.attackstat - opponent.defensestat)))
        else:
            opponent.hp = opponent.hp - (self.attackstat - opponent.defensestat)
        if opponent.hp <= 0:
            opponent.getKnockedOut()
        print("{name} used {move}".format(name=self.name, move=self.moveset[0]))
        print("{name} hp is now {hp}".format(name=opponent.name, hp=opponent.hp))

    def attackOpponent(self, opponent=None):
        # This function determins the attack used and calculates damage
        if self.knockedOut == True:
            print("{name} is knocked out and can't attack".format(name=self.name))
            return
        attacks = ["Lick", "Tackle", "Defense Curl", "Thunder Shock",
                       "Tail Whip", "Sing", "Pound", "Growl", "Life Dew",
                       "Counter", "Splash", "Charm", "Sweet Kiss",
                       "Water Gun", "Smog", "Ember", "Leer", "Lick",
                       "Confusion", "Rock Throw", "Fake Tears", "Flail",
                       "Thunder Shock", "Quick Attack"]
        move = input("""{name} moves are
    {a}      {b}
    {c}      {d}
Please pick a move: """.format(a=self.moveset[0], b=self.moveset[1], c=self.moveset[2], d=self.moveset[3],
                                   name=self.name))
        while move not in self.moveset:
            move = input("""
Please pick a valid move
    {a}      {b}
    {c}      {d}
Please pick a move: """.format(a=self.moveset[0], b=self.moveset[1], c=self.moveset[2], d=self.moveset[3],
                                   name=self.name))
        if move not in attacks:
            print("That's not a valid attack!")
            self.attackOpponent(opponent)
            return
        if self.typeAdvantage(opponent) == True:
            opponent.hp = opponent.hp - (2 * (self.attackstat - opponent.defensestat))
        elif self.typeDisadvantage(opponent) == True:
            opponent.hp = opponent.hp - (int(.5 * (self.attackstat - opponent.defensestat)))
        else:
            opponent.hp = opponent.hp - (self.attackstat - opponent.defensestat)
        if opponent.hp <= 0:
            opponent.getKnockedOut()
        print("{name} hp is now {hp}".format(name=opponent.name, hp=opponent.hp))


class Trainer:
    def __init__(self, pokemonTeam, name, maxPokemon = 1):
        self.name = name
        self.pokemonTeam = pokemonTeam
        self.current_pokemon = 0
        self.maxPokemon = maxPokemon

    def __repr__(self):
        print("{name} has the following pokemon:".format(name=self.name))
        for pokemon in self.pokemonTeam:
            print(pokemon.name)
        return "{your}'s current pokemon is {name}".format(your=self.name, name=self.pokemonTeam[self.current_pokemon].name)

    def switchPokemon(self):
        self.current_pokemon = 0
        print("Please pick a pokemon")
        for team_member in self.pokemonTeam:
            print(team_member)
        new_pokemon = input("Pick one please: ")
        if new_pokemon in self.pokemonTeam:
            print("You picked {pokemon}".format(pokemon=new_pokemon))
            for pokemon in self.pokemonTeam:
                if new_pokemon == pokemon.name:
                    return
                else:
                    self.current_pokemon += 1

    def runAway(self):
        for pokemon in self.pokemonTeam:
            pokemon.getKnockedOut()

    def attackOtherTrainer(self, other_trainer):
        if other_trainer.pokemonTeam[other_trainer.current_pokemon].knockedOut == False:
            my_pokemon = self.pokemonTeam[self.current_pokemon]
            opponents_pokemon = other_trainer.pokemonTeam[other_trainer.current_pokemon]
            my_pokemon.attackOpponent(opponents_pokemon)
        else:
            return

    def cpuAttack(self, playerTrainer):
        if len(playerTrainer.pokemonTeam) > 0:
            my_pokemon = self.pokemonTeam[self.current_pokemon]
            opponents_pokemon = playerTrainer.pokemonTeam[playerTrainer.current_pokemon]
            my_pokemon.cpuAttackOpponent(opponents_pokemon)
        else:
            return


Munchlax = Pokemon("Munchlax", "normal")
Pichu = Pokemon("Pichu", "electric")
Igglybuff = Pokemon("Igglybuff", "normal")
Togepi = Pokemon("Togepi", "normal")
Wynaut = Pokemon("Wynaut", "psychic")
Azurill = Pokemon("Azurill", "water")
Magby = Pokemon("Magby", "fire")
Smoochum = Pokemon("Smoochum", "psychic")
Bonsly = Pokemon("Bonsly", "rock")
MimeJr = Pokemon("MimeJr", "psychic")
Cleffa = Pokemon("Cleffa", "normal")
Elekid = Pokemon("Elekid", "electric")

available_pokemon = [Munchlax, Pichu, Igglybuff, Togepi, Wynaut, Azurill, Magby, Smoochum, Bonsly, MimeJr, Cleffa, Elekid]
for pokemon in available_pokemon:
    random_level = rn.randint(3, 10)
    pokemon.level = random_level


def battle():
    pokemons = available_pokemon
    string_pokemon_names = ["Munchlax", "Pichu", "Igglybuff", "Togepi", "Wynaut", "Azurill", "Magby", "Smoochum", "Bonsly", "MimeJr", "Cleffa", "Elekid"]
    player = Trainer([], input("Please pick your name: "), 3)
    cpu = Trainer([], input("Please pick your opponent's name: "), 3)
    while len(player.pokemonTeam) < player.maxPokemon:
        print("""The available pokemon are: 
{a}     {b}     {c}     {d}
{e}     {f}     {g}     {h}
{i}     {j}     {k}     {l}""".format(a=pokemons[0].name, b=pokemons[1].name, c=pokemons[2].name, d=pokemons[3].name,
                                      e=pokemons[4].name, f=pokemons[5].name, g=pokemons[6].name, h=pokemons[7].name,
                                      i=pokemons[8].name, j=pokemons[9].name, k=pokemons[10].name, l=pokemons[11].name))
        selected_pokemon = input("Please pick a pokemon: ")
        if selected_pokemon in string_pokemon_names:
            adding_index = 0
            for pokemon in string_pokemon_names:
                if selected_pokemon == pokemon:
                    player.pokemonTeam.append(pokemons[adding_index])
                    cpu.pokemonTeam.append(pokemons[rn.randint(0, 11)])
                else:
                    adding_index += 1
        else:
            print("Please select a valid pokemon")
    while (len(player.pokemonTeam) > 0) or (len(cpu.pokemonTeam) > 0):
        if (len(player.pokemonTeam) > 0) and (len(cpu.pokemonTeam) >0):
            if player.pokemonTeam[player.current_pokemon].knockedOut == True:
                if len(player.pokemonTeam) > 0:
                    player.pokemonTeam.pop(player.current_pokemon)
                    player.switchPokemon()
                if cpu.pokemonTeam[cpu.current_pokemon].knockedOut == True:
                    if len(cpu.pokemonTeam) > 0:
                        cpu.pokemonTeam.pop(cpu.current_pokemon)
                        cpu.current_pokemon = rn.randint(0, len(cpu.pokemonTeam))
                else:
                    return
            else:
                player.attackOtherTrainer(cpu)
        else:
            return
        if len(cpu.pokemonTeam) > 0:
            if cpu.pokemonTeam[cpu.current_pokemon].knockedOut == True:
                if len(cpu.pokemonTeam) > 0:
                    cpu.pokemonTeam.pop(cpu.current_pokemon)
                    cpu.current_pokemon = rn.randint(0, len(cpu.pokemonTeam))
                else:
                    return
            else:
                cpu.cpuAttack(player)
        else:
            return
    print(player.pokemonTeam)
    if player.pokemonTeam == [] :
        print("Sorry you lost :(")
    else:
        print("You win!!!")

battle()


