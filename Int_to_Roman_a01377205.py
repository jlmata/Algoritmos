#Jose Luis Mata Lomeli
#A01377205
#

class examen_progra:
    
    #Funcion
    def int_to_Roman(self, num):
        
        #Diccionarios
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]

        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        
        #Transformar
        num_roman = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                num_roman += syb[i]
                num -= val[i]
            i += 1
        return num_roman

#Pruebas
print(examen_progra().int_to_Roman(4))
print(examen_progra().int_to_Roman(7))
print(examen_progra().int_to_Roman(9))
print(examen_progra().int_to_Roman(67))
print(examen_progra().int_to_Roman(117))
print(examen_progra().int_to_Roman(1001))