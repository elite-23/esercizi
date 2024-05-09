'''
Sistema di gestione dello zoo virtuale

CLASSI:

    1. Zoo: questa classe rappresenta uno zoo. Lo zoo ha dei recinti fences e dei guardiani dello zoo, zoo_keepers.

    2. Animal: questa classe rappresenta un animale nello zoo. Ogni animale ha questi attributi: name, species, age, height, width, preferred_habitat, 
        health che è uguale a round(100 * (1 / age), 3).

    3. Fence: questa classe rappresenta un recinto dello zoo in cui sono tenuti gli animali. 
        I recinti possono contenere uno o più animali. I recinti possono hanno gli attributi area, temperature e habitat.

    4. ZooKeeper: questa classe rappresenta un guardiano dello zoo responsabile della gestione dello zoo. 
        I guardiani dello zoo hanno un nome, un cognome, e un id. Essi possono nutrire gli animali, pulire i recinti e svolgere altri compiti nel nostro zoo virtuale.


FUNZIONALITÀ:
    1. add_animal(animal: Animal, fence: Fence) (Aggiungi nuovo animale): consente al guardiano dello zoo di aggiungere un nuovo animale allo zoo. 
        L'animale deve essere collocato in un recinto adeguato in base alle esigenze del suo habitat e se c'è ancora spazio nel recinto, 
        ovvero se l'area del recinto è ancora sufficiente per ospitare questo animale.

    2. remove_animal(animal: Animal, fence: Fence) (Rimuovi animale): consente al guardiano dello zoo di rimuovere un animale dallo zoo. 
        L'animale deve essere allontanato dal suo recinto. Nota bene: L'area del recinto deve essere ripristinata dello spazio che l'animale rimosso occupava.

    3. feed(animal: Animal) (Dai da mangiare agli animali): implementa un metodo che consenta al guardiano dello zoo di nutrire tutti gli animali dello zoo. 
        Ogni volta che un animale viene nutrito, la sua salute incrementa di 1% rispetto alla sua salute corrente, ma le dimensioni dell'animale (height e width) 
        vengono incrementate del 2%. Perciò, l'animale si può nutrire soltanto se il recinto ha ancora spazio a sufficienza per ospitare l'animale ingrandito dal cibo.

    4. clean(fence: Fence) (Pulizia dei recinti): implementare un metodo che consenta al guardiano dello zoo di pulire tutti i recinti dello zoo. 
        Questo metodo restituisce un valore di tipo float che indica il tempo che il guardiano impiega per pulire il recinto. 
        Il tempo di pulizia è il rapporto dell'area occupata dagli animali diviso l'area residua del recinto. Se l'area residua è pari a 0, restituire l'area occupata.

    5. describe_zoo() (Visualizza informazioni sullo zoo): visualizza informazioni su tutti i guardani dello zoo, sui recinti dello zoo che contengono animali. 

E.s.: Se abbiamo un guardiano chiamato Lorenzo Maggi con matricola 1234, e un recinto Fence(area=100, temperature=25, habitat=Continentale) 
con due animali Animal(name=Scoiattolo, species=Blabla, age=25, ...), Animal(name=Lupo, species=Lupus, age=14,...) 
ci si aspetta di avere una rappresentazione testuale dello zoo come segue:

GUARDIANS:

    ZooKeeper(name=Lorenzo, surname=Maggi, id=1234)

FENCES:

    Fence(area=100, temperature=25, habitat=Continent)

WITH ANIMALS:

    Animal(name=Scoiattolo, species=Blabla, age=25)

    Animal(name=Lupo, species=Lupus, age=14)

#########################

Fra un recinto e l'altro mettete 30 volte il carattere #.
'''

class Animal:
    def __init__(self, name :str, species :str, age :int, height :float, width :float , preferred_habitat :str) -> None:
        self.name=name
        self.species=species
        self.age=age
        self.height=height
        self.width=width
        self.preferred_habitat=preferred_habitat
        self.health=round(100 * (1 / age), 3)

    def __str__(self) -> str:
        return "Animal(name="+self.name+", species="+self.species+", age="+str(self.age)+", height="+str(self.height)+",width="+str(self.width)+", preferred_habitat="+self.preferred_habitat+")\n"
    
    def __eq__(self, value :object) -> bool:
        if self.name==value.name:
            return True
        else:
            return False
    
    
    


class Fence:
    def __init__(self, area :float, temperature :float, habitat :str) -> None:
        self.area=area
        self.temperature=temperature
        self.habitat=habitat
        self.animals :list[Animal]=[]
    
    def __str__(self) -> str:
        if len(self.animals)==0:
            return "Fence(area="+str(self.area)+", temperature="+str(self.temperature)+", habitat="+self.habitat+")\n\nWith animals:\n\n\tNone"
        else:
            f="Fence(area="+str(self.area)+", temperature="+str(self.temperature)+", habitat="+self.habitat+")\n\nWith animals:\n"
            for i in self.animals:
                f+="\n\t"+i.__str__()
            return f


    def add_animal(self,animal :Animal) -> None:
        self.area= self.area - (animal.height*animal.width)
        self.animals.append(animal)

    def remove_animal(self, animal :Animal) -> None:
        for i in self.animals:
            if i==animal:
                self.animals.remove(animal)
                self.area= self.area + (animal.height*animal.width)
                break

class ZooKeeper:
    def __init__(self,name :str, surname :str, id :int) -> None:
        self.name=name
        self.surname=surname
        self.id=id

    def __str__(self) -> str:
        return "ZooKeeper(name="+self.name+", surname="+self.surname+", id="+str(self.id)+")\n"

    def add_animal(self, animal: Animal, fence: Fence) -> None:
        if animal.preferred_habitat==fence.habitat:
            if animal.height*animal.width <= fence.area:
                fence.add_animal(animal)
            else:
                print("The animal can't fit in the fence because it's too big.")
        else:
            print("The animal can't be put in this fence because its ideal habitat is different.")

    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        if animal in fence.animals:
            fence.remove_animal(animal)
        else:
            print("This animal is not present in this fence.")

    def feed(animal: Animal):
        pass

    def clean(fence: Fence):
        pass


class Zoo:
    def __init__(self,fences :list[Fence], zoo_keepers :list[ZooKeeper]) -> None:
        self.fences=fences
        self.zoo_keepers=zoo_keepers

    def __str__(self) -> str:
        
        z="GUARDIANS:\n"
        for i in self.zoo_keepers:
            z+="\n\t"+i.__str__()
        
        z+="\nFENCES:\n"
        for i in self.fences:
            z+="\n\t"+i.__str__()
            z+="\n##############################\n"
        
        return z

    def describe_zoo(self):
        print(self.__str__())

A1=Animal("Sandro","scorpione",1,0.2,0.2,"sand")
A2=Animal("Pietro","Schimmia",12,1.2,0.5,"jungle")
F1=Fence(45,23,"jungle")
F2=Fence(133,12,"sand")
K1=ZooKeeper("Gaia","Flati",1)
K2=ZooKeeper("Luca","Cavalleri",2)
Z=Zoo([F1,F2],[K1,K2])
K1.add_animal(A1,F2)
K2.add_animal(A2,F1)
Z.describe_zoo()