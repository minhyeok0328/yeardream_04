# prac5.py

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, new_animal):
        for animal in self.animals:
            if animal.name == new_animal.name and animal.species == new_animal.species:
                print(f'{new_animal.name} the {new_animal.species}는 이미 동물원에 있습니다. 다른 이름을 사용하거나, 다른 종으로 추가해주세요.dd')
                return

        self.animals.append(new_animal)

    def show_animals(self):
        animals = '현재 동물원에는 다음 동물들이 있습니다 :\n'
        animals += self.get_animals_text()

        print(animals)

    def show_animals_by_species(self, species):
        animals = self.get_animals_text([animal for animal in self.animals if animal.species == species])

        print(animals)

    def get_animals_text(self, animals = []):
        animals_text = ''

        if not animals:
            animals = self.animals

        for animal in animals:
            animals_text += f'- {animal.name} the {animal.species}\n'

        return animals_text


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

def main():
    # 동물원을 선언하고 10마리의 동물들을 추가합니다. 합니다.
    zoo = Zoo()
    zoo.add_animal(Animal("Leo", "Lion"))
    zoo.add_animal(Animal("Harry", "Hippo"))
    zoo.add_animal(Animal("Ella", "Elephant"))
    zoo.add_animal(Animal("Gerry", "Giraffe"))
    zoo.add_animal(Animal("Gira", "Giraffe"))
    zoo.add_animal(Animal("Terry", "Lion"))
    zoo.add_animal(Animal("Barry", "Bear"))
    zoo.add_animal(Animal("Larry", "Leopard"))
    zoo.add_animal(Animal("Cary", "Crocodile"))
    zoo.add_animal(Animal("Mary", "Monkey"))

    # 동물원에 있는 모든 동물을 출력합니다.
    zoo.show_animals()
    ## 출력 결과 : 
    '''
    현재 동물원에는 다음 동물들이 있습니다 :
    - Leo the Lion
    - Harry the Hippo
    - Ella the Elephant
    - Gerry the Giraffe
    - Gira the Giraffe
    - Terry the Lion
    - Barry the Bear
    - Larry the Leopard
    - Cary the Crocodile
    - Mary the Monkey
    '''

    # 특정 종에 해당하는 동물들의 이름만 출력합니다.
    zoo.show_animals_by_species("Lion")
    # 출력 결과 : 
    '''
    - Leo the Lion
    - Terry the Lion
    '''
    zoo.show_animals_by_species("Elephant")
    # 출력 결과 : 
    '''
    - Ella the Elephant
    '''

    # 이미 존재하는 동물을 추가한 경우, 해당 동물이 이미 있음을 출력합니다.
    zoo.add_animal(Animal("Leo", "Lion"))
    # 출력 결과 : 
    '''
    "Leo the Lion"은 이미 동물원에 있습니다. 다른 이름을 사용하거나, 다른 종으로 추가해주세요.
    '''

if __name__ == "__main__":
    main()
