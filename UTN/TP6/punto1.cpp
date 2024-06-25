#include <iostream>
using namespace std;
/*
Escribe una función que reciba dos números enteros y devuelva su suma.
*/

int sumaNumeros(int numero1, int numero2);

int main(){
    int n1, n2, suma;
    cout << "Elija dos numeros y lo vamos a sumar: ";
    cin >> n1 >> n2;

    suma = sumaNumeros(n1,n2);

    cout << "La suma de sus numeros son: " << suma;
    
    return 0;
}

int sumaNumeros(int numero1, int numero2){
    int suma;
    suma = numero1 + numero2;

    return suma;
}