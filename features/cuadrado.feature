Feature: Funcion cuadrado
    Como usuario
    Quiero calcular el cuadrado de un numero
    Para obtener x²

    Scenario: Cuadrado de numeros positivos
        Given tengo el numero 4
        When ejecuto la funcion cuadrado
        Then el resultado debe ser 16

    Scenario: Cuadrado de numeros negativos
        Given tengo el numero -6
        When ejecuto la funcion cuadrado
        Then el resultado debe ser 36