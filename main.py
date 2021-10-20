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
def extract_partea_fractionara(numar):
    return str(numar).split('.')[1]
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
        if element > capat1 and element < capat2 :
            rezlut_list.append(element)
    if len(rezlut_list)==0:
        return  None
    else :
        return rezlut_list

def test_get_numere_din_interval():
    assert get_numere_din_interval([1.2,1.1,4,10,11.1],1,5)==[1.2,1.1,4]
    assert get_numere_din_interval([1.2, 1.1, 4, 10, 11.1], 1, 11) == [1.2, 1.1, 4,10]
    assert get_numere_din_interval([1, 1.1, 4, 10, 11.1], -4, -1) == None
def get_numere_partea_intreaga_divizor_partea_fractionara(lista):
    '''
    programul verifica daca partea intreaga a unui numar este divizor al partii fractionare si returneaza o lista cu aceste elemente
    :param lista:
    :return: rezult_list
    '''
    rezult_list=[]
    for element in lista:
        intreg=int(extract_partea_intreaga(element))
        fractionar =int(extract_partea_fractionara(element))
        if fractionar % intreg == 0:
            rezult_list.append(element)
    if len(rezult_list) == 0:
        return None
    else:
        return rezult_list
def test_get_numere_partea_intreaga_divizor_partea_fractionara():
    assert get_numere_partea_intreaga_divizor_partea_fractionara([1.4,3.3 ,-3.3 ,2.4, 8.9 ,19.9])==[1.4, 3.3, -3.3, 2.4]
    assert get_numere_partea_intreaga_divizor_partea_fractionara([1.4, 3.3,-3.3,8.9,19.9]) == [1.4, 3.3, -3.3,]
    assert get_numere_partea_intreaga_divizor_partea_fractionara([ 8.9, 19.9]) == None
def convertire_numere_in_format_string(lista):
    '''
    transforma numerele din lista in format string si retuneaza o lista cu aceste stringuri
    :param lista:
    :return: rezult_list
    '''
    rezult_list=[]

    lista_numere = ["zero","unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua",]
    lista_semne = ["minus", "virgula"]
    for element in lista:
        elem_nou = ""
        if element < 0:
            elem_nou += lista_semne[0]
        if int(element) == element:
            while element > 9:
                elem_nou += lista_numere[element % 10]
                element = element // 10
            elem_nou += lista_numere[int(element)]
        else:
            nri = int(extract_partea_intreaga(element))
            nrf = int(extract_partea_fractionara(element))
            while nri > 9:
                elem_nou += lista_numere[nri % 10]
                nri = nri // 10
                elem_nou += lista_numere[nri]
            while nrf > 9:
                elem_nou +=lista_numerel [nri % 10]
                nri = nri // 10
            elem_nou += lista_semne[1]
            elem_nou += lista_numere[nrf]
        rezult_list.append(elem_nou)
    return rezult_list
def main():
    stop = False
    lista = []
    while not stop:
        print("""
            1 -> Citire lista 
            2 -> Afiseaza partea intreaga a elementelor
            3 -> Afișeza numerele care aparțin unui interval deschis citit de la tastatură.
            4 -> Afișarea numerelor a căror parte întreagă este divizor al părții fracționare
            5 -> Convertire numere in format string
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
            inceput=float(input("Dati inceputul intervalului: "))
            final=float(input("Dati finalul intervalului: "))
            print(get_numere_din_interval(lista,inceput,final))
        elif command == '4':
           print(get_numere_partea_intreaga_divizor_partea_fractionara(lista))
        elif command == '5':
            print(convertire_numere_in_format_string(lista))
    test_get_numere_din_interval()
    test_get_numere_partea_intreaga_divizor_partea_fractionara()
if __name__ == '__main__':
    main()