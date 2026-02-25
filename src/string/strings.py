class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo (se lee igual de izquierda a derecha y viceversa).
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si es palíndromo, False en caso contrario
        """
        limpio = ""
        for c in texto:
            if c != " ":
                limpio += c.lower()

        invertido = ""
        for i in range(len(limpio) - 1, -1, -1):
            invertido += limpio[i]

        return limpio == invertido
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        
        Args:
            texto (str): Cadena a invertir
            
        Returns:
            str: Cadena invertida
        """
        resultado = ""
        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        return resultado
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        
        Args:
            texto (str): Cadena para contar vocales
            
        Returns:
            int: Número de vocales en la cadena
        """
        vocales = "aeiouAEIOU"
        contador = 0
        for c in texto:
            if c in vocales:
                contador += 1
        return contador
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        
        Args:
            texto (str): Cadena para contar consonantes
            
        Returns:
            int: Número de consonantes en la cadena
        """
        vocales = "aeiouyAEIOUY"
        contador = 0

        for c in texto:
            if (
                c.isalpha()
                and c not in vocales
                    and c.lower() != 'y'
            ):
                contador += 1

        return contador
    

    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas (contienen exactamente los mismos caracteres).
        
        Args:
            texto1 (str): Primera cadena
            texto2 (str): Segunda cadena
            
        Returns:
            bool: True si son anagramas, False en caso contrario
        """
        limpio1 = ""
        limpio2 = ""

        for c in texto1:
            if c != " ":
                limpio1 += c.lower()

        for c in texto2:
            if c != " ":
                limpio2 += c.lower()

        if len(limpio1) != len(limpio2):
            return False

        lista1 = sorted(limpio1)
        lista2 = sorted(limpio2)

        return lista1 == lista2
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        
        Args:
            texto (str): Cadena para contar palabras
            
        Returns:
            int: Número de palabras en la cadena
        """
        if texto.strip() == "":
            return 0
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en Mayuscula la primera letra de cada palabra en una cadena.
        
        Args:
            texto (str): Cadena
            
        Returns:
            str: Cadena con la primera letra de cada palabra en mayúscula
        """
        resultado = ""
        nueva_palabra = True

        for c in texto:
            if c == " ":
                resultado += c
                nueva_palabra = True
            else:
                if nueva_palabra:
                    resultado += c.upper()
                    nueva_palabra = False
                else:
                    resultado += c
        return resultado
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        
        Args:
            texto (str): Cadena con posibles espacios duplicados
            
        Returns:
            str: Cadena sin espacios duplicados
        """
        resultado = ""
        espacio_anterior = False

        for c in texto:
            if c == " ":
                if not espacio_anterior:
                    resultado += c
                espacio_anterior = True
            else:
                resultado += c
                espacio_anterior = False

        return resultado
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        
        Args:
            texto (str): Cadena a verificar
            
        Returns:
            bool: True si la cadena representa un número entero, False en caso contrario
        """
        if texto == "":
            return False

        if texto[0] == "-":
            if len(texto) == 1:
                return False
            inicio = 1
        else:
            inicio = 0

        for i in range(inicio, len(texto)):
            if texto[i] < "0" or texto[i] > "9":
                return False

        return True
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        
        Args:
            texto (str): Cadena a cifrar
            desplazamiento (int): Número de posiciones a desplazar cada letra
            
        Returns:
            str: Cadena cifrada
        """
        resultado = ""

        for c in texto:
            if "a" <= c <= "z":
                base = ord("a")
                nueva = (ord(c) - base + desplazamiento) % 26
                resultado += chr(base + nueva)
            elif "A" <= c <= "Z":
                base = ord("A")
                nueva = (ord(c) - base + desplazamiento) % 26
                resultado += chr(base + nueva)
            else:
                resultado += c

        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        
        Args:
            texto (str): Cadena cifrada
            desplazamiento (int): Número de posiciones que se desplazó cada letra
            
        Returns:
            str: Cadena descifrada
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        
        Args:
            texto (str): Cadena principal
            subcadena (str): Subcadena a buscar
            
        Returns:
            list: Lista con las posiciones iniciales de cada ocurrencia
        """
        if subcadena == "":
            return []

        posiciones = []
        n = len(texto)
        m = len(subcadena)

        for i in range(n - m + 1):
            coincide = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    coincide = False
                    break
            if coincide:
                posiciones.append(i)

        return posiciones