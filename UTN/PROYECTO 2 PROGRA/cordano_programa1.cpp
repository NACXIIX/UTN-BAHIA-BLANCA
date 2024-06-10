#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

//Funciones globales
int matriz[3][3];

//Prototipo de funcion
void llenarMatriz();
void mostrarMatriz();
int buscarValor();
int devolverValor();
int ordenarMatriz();

// programa principal
int main(){
    int opcion;

    do{
        cout << "\t\t--- MENU INTERACTIVO ---" << '\n' << endl;
        cout << "Elija una opción." << endl;
        cout << "1. Cargar la matriz" << endl;
        cout << "2. Mostrar los valores de la matriz" << endl;
        cout << "3. Buscar un valor específico ingresado por el usuario dentro de la matriz" << endl;
        cout << "4. Devolver el valor máximo o mínimo de la matriz" << endl;
        cout << "5. Ordenar los valores de la matriz de forma ascendente o descendente" << endl;
        cout << "6. Salir del programa" << endl;
        cin >> opcion;

        switch(opcion){
            case 1: 
                llenarMatriz();
                break;
            case 2:
                mostrarMatriz();
        }

        if (opcion == 1){
            mostrarMatriz();
        } else {
            cout << "No esta la matriz cargada correctamente";
        }
    } while (opcion <=0 || opcion > 6);
    return 0;
}


// 
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

}

void mostrarMatriz(){
    for(int i = 0; i < 3; i ++){
        cout << endl;
        for(int j = 0; j < 3; j++){
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }

}