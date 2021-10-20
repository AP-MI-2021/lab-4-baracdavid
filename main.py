def citire_lista():
    result_list = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = float(string_element)
        result_list.append(element)

    return result_list
def extract_partea_intreaga(numar):
    return str(numar).split('.')[0]
def afisare_partea_intreaga(lista):
   """
   afiseaza partea intreaga a tuturor elementelor din lista
   :param lista:
   :return: result_list
   """
   result_list = []
   for element in lista :
        result_list.append(int(extract_partea_intreaga(element)))
   return result_list
def get_numere_din_interval(lista,capat1,capat2):
    '''
    fuctia returneaza numerele din lista ce ce afla in intervalul deschis dat de capat1 si capat 2
    :param lista:
    :param capat1:
    :param capat2:
    :return: rezult_list
    '''
    rezlut_list=[]
    for element in lista:
        if element >= capat1 and element <= capat2 :
            rezlut_list.append(element)
    return rezlut_list

def test_get_numere_din_interval():
    assert get_numere_din_interval([1.2,1.1,4,10,11.1],1,5)==[1.2,1.1,4]
def main():
    stop = False
    lista = []
    while not stop:
        print("""
            1 -> Citire lista 
            2 -> Afiseaza partea intreaga a elementelor
            3 -> Afișeza numerele care aparțin unui interval deschis citit de la tastatură.
            4 ->
            5 -> 
            x -> Exit
         """)
        command = input("Alege comanda: ")
        if command == 'x':
            stop = True
        elif command == '1':
            lista = citire_lista()
        elif command == '2':
            print(afisare_partea_intreaga(lista))
        elif command == '3':
            inceput=int(input("Dati inceputul intervalului: "))
            final=int(input("Dati finalul intervalului: "))
            print(get_numere_din_interval(lista,inceput,final))
    test_get_numere_din_interval()
if __name__ == '__main__':
    main()