class Trait:
    name = None
    type = None
    subtype = None

    def __init__(self, name: str, primary_type: str, subtype: str):
        self.name = name
        self.type = primary_type
        self.subtype = subtype
        pass


class Character:
    """todo: load these via file configuration?"""
    trait_definitions = {
        'Strength': Trait('Strength', 'Attribute', 'Physical'),
        'Dexterity': Trait('Strength', 'Attribute', 'Physical'),
        'Stamina': Trait('Strength', 'Attribute', 'Physical'),

        'Charisma': Trait('Strength', 'Attribute', 'Social'),
        'Manipulation': Trait('Strength', 'Attribute', 'Social'),
        'Appearance': Trait('Strength', 'Attribute', 'Social'),

        'Perception': Trait('Strength', 'Attribute', 'Mental'),
        'Intelligence': Trait('Strength', 'Attribute', 'Mental'),
        'Wits': Trait('Strength', 'Attribute', 'Mental'),

        'Alertness': Trait('Alertness', 'Ability', 'Talent'),
        'Athletics': Trait('Athletics', 'Ability', 'Talent'),
        'Brawl': Trait('Brawl', 'Ability', 'Talent'),
        'Empathy': Trait('Empathy', 'Ability', 'Talent'),
        'Expression': Trait('Expression', 'Ability', 'Talent'),
        'Intimidation': Trait('Intimidation', 'Ability', 'Talent'),
        'Leadership': Trait('Leadership', 'Ability', 'Talent'),
        'PrimalUrge': Trait('PrimalUrge', 'Ability', 'Talent'),
        'Streetwise': Trait('Streetwise', 'Ability', 'Talent'),
        'Subterfuge': Trait('Subterfuge', 'Ability', 'Talent'),

        'AnimalKen': Trait('AnimalKen', 'Ability', 'Skill'),
        'Crafts': Trait('Crafts', 'Ability', 'Skill'),
        'Drive': Trait('Drive', 'Ability', 'Skill'),
        'Etiquette': Trait('Etiquette', 'Ability', 'Skill'),
        'Firearms': Trait('Firearms', 'Ability', 'Skill'),
        'Larceny': Trait('Larceny', 'Ability', 'Skill'),
        'Melee': Trait('Melee', 'Ability', 'Skill'),
        'Performance': Trait('Performance', 'Ability', 'Skill'),
        'Stealth': Trait('Stealth', 'Ability', 'Skill'),
        'Survival': Trait('Survival', 'Ability', 'Skill'),

        'Academics': Trait('Academics', 'Ability', 'Knowledge'),
        'Computer': Trait('Computer', 'Ability', 'Knowledge'),
        'Enigmas': Trait('Enigmas', 'Ability', 'Knowledge'),
        'Investigation': Trait('Investigation', 'Ability', 'Knowledge'),
        'Law': Trait('Law', 'Ability', 'Knowledge'),
        'Medicine': Trait('Medicine', 'Ability', 'Knowledge'),
        'Occult': Trait('Occult', 'Ability', 'Knowledge'),
        'Rituals': Trait('Rituals', 'Ability', 'Knowledge'),
        'Science': Trait('Science', 'Ability', 'Knowledge'),
        'Technology': Trait('Technology', 'Ability', 'Knowledge'),
    }

    name: str = None
    player: str = None
    breed: str = None
    auspice: str = None
    tribe: str = None

    traits = {}

    def __init__(self, data: dict):
        for trait in self.trait_definitions:
            self.name = data['Name']
            self.player = data['Player']
            self.breed = data['Breed']
            self.auspice = data['Player']
            self.tribe = data['Tribe']

            self.traits[trait] = data[trait]
