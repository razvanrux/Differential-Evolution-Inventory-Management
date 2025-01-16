## Functia 'inventory_cost'
1. **Cel mai favorabil caz:**
   -Complexitatea este determinata de iterarea prin lista 'demand': **O(n)** unde 'n' este numarul de elemnte din 'demand'

2. **Cel mai defavorabil caz:**
    -Cererea este intotdeauna mai mare decat 'inventory_level', totusi complexitatea ramane liniara deoarece se efectueaza o singura iteratie prin lista 'demand' deci complexitatea este de **O(n)**
       
   3. **Cazul mediu:**
    -Costurile sunt calculate pentru fiecare element, iar conditiile din 'if' sunt evaluate constant, iar complexitatea ramane **O(n)**


## Functia 'simulate_inventory'
1. **Cel mai favorabil caz:**
    - Daca inventarul este intotdeauna suficient, doar lista 'inventory_levels' este actualizata complexitatea este **O(n)**
2. **Cel mai defavorabil caz:** 
   - Daca inventarul scade sub punctul de reaprovizionare pentru fiecare cerere, o comanda suplimentara este plasata la fiecare pas, totusi, operatiile se efectueaza intr-o singura iteratie, deci complexitatea ramane **O(n)**
3. **Cazul mediu:**
   - Cereri aleatoare si comportament variabil al inventarului, complexitatea ramane liniara **O(n)**


## Functia 'differential_evolution'
1. **Cel mai favorabil caz:**
    -Daca optimizarea converge rapid, numarul de iteratii este minim iar complexitatea depinde de numarul de membri ai populaiei ('P') si numarul de parametri ('D'): **O(P \* D \* K\_min)** unde 'K\_min' este numarul minim de iteratii.
2. **Cel mai defavorabil caz:**
-Algoritmul necesita toate iteratiile maxime posibile ('K\_max') si evalueaza toate combinatiile posibile: **O(P \* D \* K\_max)**.
3. **Cazul mediu:**
-Numarul de iteratii este undeva intre minim si maxim:  **O(P \* D \* K\_med)**.



# Demonstratia corectitudinii pentru functia simulate_inventory:

### Preconditii:
    -'demand' este o lista de cereri pentru fiecare perioada.
    -'reorder_point' este punctul optim de reaprovizionare
    -'order_quantity' este cantitatea optima de reaprovizionare

### Scopul
Scopul functiei este sa calculeze nivelurile de inventar pentru fiecare perioada.

### Postconditii:
    -lista rezultata 'inventory_levels' reflecta corect evolutia inventarului in fiecare perioada tinand cont de cererea('d') si reaprovizionarea daca inventarul scade sub sau egal cu 'reorder_point'.

### Demonstratia corectitudinii:
### Initializare:

La inceputul executiei:
    -'inventory_level' este initializat cu valoarea 'reorder_point', ceea ce asigura ca punctul de plecare este corect conform parametrilor primiti.

### Mentinerea invariantelor:
In fiecare iteratie:
- **Verificarea conditiei**
        -Se verifica daca 'inventory_level <= reorder_point'. Daca aceasta conditie este adevarata, se adauga 'order_quantity' la inventar.
        -Aceasta asigura ca reaprovizionarea are loc doar cand este necesara, conform punctului de reaprovizionare.
  - **Salvarea nivelului intervalului**
          -"inventory_levels.append(inventory_level)":
        -Nivelul curent al inventarului este salvat inainte de scaderea cererii curente, reflectand situatia corecta la inceputul perioadei.
  -**Actualizare inventar**
          -'inventory_level -= d':
            -Cererea curenta este scazuta din inventar, actualizand nivelul de inventar pentru urmatoarea perioada.

### Invarianti:
- Inventarul este actualizat corect in functie de cerere si reaprovizionare.
- Fiecare pas adauga un singur element la 'inventory_levels'.

### Finalizare:
La sfarsitul buclei:
- Lista 'inventory_levels' contine valorile nivelurilor de inventar pentru toate perioadele cererii.
- Functia returneaza lista completa.