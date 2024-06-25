#include <iostream>
using namespace std;

/*
Implementa una función que reciba un arreglo de enteros y calcule la suma de todos sus 
elementos.
*/


// Determinamos las funciones
void vector();
int sumaNumeros(int arreglo[], int longitudArreglo);

// Variables a nivel global
int arreglo[100], longitudArreglo;

// Programa principal
int main(){
    vector();

    cout << "La suma de tus elementos es: " << sumaNumeros(arreglo,longitudArreglo);
    return 0;
}

// Funcion llenado del vector
void vector(){
    cout << "Digame el tamaño de su arreglo: ";
    cin >> longitudArreglo;

    for(int i = 0; i<longitudArreglo; i++){
        cout << "Diga el valor para la posicion " << i+1 << " de su arreglo: ";
        cin >> arreglo[i];
    }
}

// Funcion que suma los valores del vector
int sumaNumeros(int arreglo[], int longitudArreglo){
    int suma = 0;
    
    for(int i = 0; i<longitudArreglo; i++){
        suma += arreglo[i];
    }

    return suma;
}