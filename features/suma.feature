Feature: Funcion suma
    Como usuario
    Quiero sumar dos numeros
    Para obtener el resultado correspondiente

    Scenario: Sumar numeros positivos
        Given tengo los numeros 5 y 3
        When ejecuto la funcion suma
        Then el resultado debe ser 8

    Scenario: Sumar numeros negativos
        Given tengo los numeros -2 y -3
        When ejecuto la funcion suma
        Then el resultado debe ser -5