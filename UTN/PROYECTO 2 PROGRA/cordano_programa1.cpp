#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//Funciones globales
int matriz[3][3];

//Prototipo de funcion
int menu();
void llenarMatriz();
void mostrarMatriz();
int buscarValor();
int devolverValor();
int ordenarMatriz();

// PROGRAMA PRINCIPAL
int main(){
    int op = menu();

    switch(op){
        case 1: 
            llenarMatriz();
            break;
        case 2:
            mostrarMatriz();
            break;
        case 6:
            cout << "Saliste del menu" << endl;
            break;
    }

    return 0;
}


// MENU INTERACTIVO
int menu(){
    int opcion;

    do{
        cout << "\t\t--- MENU INTERACTIVO ---" << '\n' << endl;
        cout << "Elija una opcion.\n" << endl;
        cout << "1. Cargar la matriz" << endl;
        cout << "2. Mostrar los valores de la matriz" << endl;
        cout << "3. Buscar un valor especifico ingresado por el usuario dentro de la matriz" << endl;
        cout << "4. Devolver el valor maximo o minimo de la matriz" << endl;
        cout << "5. Ordenar los valores de la matriz de forma ascendente o descendente" << endl;
        cout << "6. Salir del programa" << endl;
        cin >> opcion;
    } while (opcion <=0 || opcion > 6);

    return opcion;
}

// CARGAR LA MATRIZ
void llenarMatriz(){
    srand(time(NULL));
    int respuesta;
    
    do{
        cout << "Elija de que manera desea cargar la matriz 3x3:" << endl;
        cout << "1. Valores aleatorios" << endl;
        cout << "2. De manera manual" << endl;
        cout << "3. SALIR" << endl;
        cin >> respuesta;

        switch (respuesta){
        case 1:
            for(int i = 0; i<3; i++){
                for (int j = 0; j<3; j++){
                    matriz[i][j] = rand() % 100+1;
                }
            }
            break;
        case 2:
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    cout << "Digite el numero [" <<i<< "][" <<j<<"]: ";
                    cin >> matriz[i][j];
                }
            }
            break;
        case 3:
            cout << "Saliste del menu"; // Se podria agregar una forma de volver al menu anterior
        }

    } while (respuesta != 1 && respuesta != 2 && respuesta !=3);

    main();
}

// MOSTRAR MATRIZ
void mostrarMatriz(){
    int volver;

    cout << "-------------------";
    for(int i = 0; i < 3; i ++){
        cout << endl;
        for(int j = 0; j < 3; j++){
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }
    cout << "-------------------";
    cout << endl;

    cout << "Esa es su matriz cargada. \nDesea volver al menu interactivo?" << endl;
    cout << "1. Si" << endl;
    cout << "2. No" << endl;
    cin >> volver;
    
    switch(volver){
        case 1:
            main();
            break;
        case 2:
            break;
    }
}

//BUSQUEDA DE UN VALOR INGRESADO POR EL USUARIO DENTRO DE LA MATRIZ
