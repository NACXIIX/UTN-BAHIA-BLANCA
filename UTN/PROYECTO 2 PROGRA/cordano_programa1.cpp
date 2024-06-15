#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

//Funciones globales
const int n = 3;
int matriz[n][n];
bool validacionMatrizCargada = false;

//Prototipos de funciones
int menu();
void cargarMatriz();
void mensajeErrorMatrizVacia();
void mostrarMatriz();
void buscarValor();
int devolverValor();
void ordenarMatriz();

// PROGRAMA PRINCIPAL
int main(){
    int op = menu();

    switch(op){
        case 1: 
            cargarMatriz();
            break;
        case 2:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                mostrarMatriz();
            }
            break;
        case 3:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                buscarValor();
            }
            break;
        case 4:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                cout << "El valor es: " << devolverValor();
            }
            break;
        case 5:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                ordenarMatriz();
            }
            break;
        case 6:
            cout << ".\n..\n...\n...." << endl;
            cout << "Saliste del programa" << endl;
            break;
    }

    return 0;
}


// MENU INTERACTIVO
int menu(){
    int opcion;

    do{
        cout << "\t\t--- MENU INTERACTIVO ---" << '\n' << endl;
        cout << "1. Cargar la matriz" << endl;
        cout << "2. Mostrar los valores de la matriz" << endl;
        cout << "3. Buscar un valor especifico ingresado por el usuario dentro de la matriz" << endl;
        cout << "4. Devolver el valor maximo o minimo de la matriz" << endl;
        cout << "5. Ordenar los valores de la matriz de forma ascendente o descendente" << endl;
        cout << "6. Salir del programa\n" << endl;
        cout << "> Elija la opcion: ";
        cin >> opcion;
        cout << endl;
    } while (opcion <=0 || opcion > 6);

    return opcion;
}

// CARGAR LA MATRIZ
void cargarMatriz(){
    srand(time(NULL));
    int respuesta;
    
    do{
        cout << "Elija de que manera desea cargar la matriz 3x3:" << endl;
        cout << "1. Valores aleatorios" << endl;
        cout << "2. De manera manual" << endl;
        cout << "3. Volver al menu" << endl;
        cout << "> Elija la opcion: ";
        cin >> respuesta;

        switch (respuesta){
        case 1:
            for(int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    matriz[i][j] = rand() % 100+1;
                }
            }
            break;
        case 2:
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    cout << "Digite el numero [" <<i<< "][" <<j<<"]: ";
                    cin >> matriz[i][j];
                }
            }
            break;
        case 3:
            main();
            break;
        }

    } while (respuesta != 1 && respuesta != 2 && respuesta !=3);

    validacionMatrizCargada = true;

    if (respuesta != 3){
        main();
    }
}

// MOSTRAR MATRIZ
void mostrarMatriz(){
    int volver;

    cout << "-------------------";
    for(int i = 0; i < n; i ++){
        cout << endl;
        for(int j = 0; j < n; j++){
            cout << matriz[i][j] << "\t";
        }
        cout << endl;
    }
    cout << "-------------------";
    cout << endl;

    do{
        cout << "Esa es su matriz cargada. \nDesea volver al menu interactivo?" << endl;
        cout << "1. Si" << endl;
        cout << "2. No" << endl;
        cout << "> Elija la opcion: ";
        cin >> volver;
        
        switch(volver){
            case 1:
                main();
                break;
            case 2:
                break;
        }
    } while (volver <= 0 || volver > 2);
}

//BUSQUEDA DE UN VALOR INGRESADO POR EL USUARIO DENTRO DE LA MATRIZ

void buscarValor(){
    int numero, volver;
    bool encontrado = false;
    cout << "Digite el valor que esta buscando" << endl;
    cout << "> ";
    cin >> numero;

    for(int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if(matriz[i][j] == numero){
                encontrado = true;
                cout << "Tu numero se encontro en la posicion : [" << i << "][" << j << "]\n";
            }
        }
    }

    if (encontrado == false){
        cout << "El numero que ingresaste no se ha encontrado.\n";
    }

    do{
        cout << "Desea volver al menu interactivo?" << endl;
        cout << "1. Si" << endl;
        cout << "2. No" << endl;
        cout << "> Elija la opcion: ";
        cin >> volver;

        switch(volver){
            case 1:
                main();
                break;
            case 2:
                cout << ".\n..\n...\n...." << endl;
                cout << "Saliste del programa" << endl;
                break;
        }
    } while (volver <= 0 || volver > 2);
}



int devolverValor(){
    int nArreglo = n*n;
    int arreglo [nArreglo];
    int k = 0;
    int mayor = 0;
    int menor = 100;
    int opcion;
    int valorDevuelto;
    
    //Llenando arreglo con los valores de la matriz.
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j ++){
            arreglo[k] = matriz[i][j];
            k++;
        }
    }

    for(int i = 0; i < nArreglo; i++){
        if (arreglo[i] < menor){
            menor = arreglo[i];
        }
    
        if (arreglo[i] > mayor){
            mayor = arreglo[i];
        }
    }

    cout << "Estas buscando el menor o el mayor?" << endl;
    cout << "1. Mayor" << endl;
    cout << "2. Menor" << endl;
    cout << "3. Volver al menu\n";
    cout << "> Elija la opcion: ";
    cin >> opcion;

    do{
        switch(opcion){
            case 1:
                valorDevuelto = mayor;
                break;
            case 2:
                valorDevuelto = menor;
                break;
            case 3:
                main();
        }
    } while (opcion <= 0 || opcion > 3);

    return valorDevuelto;
}


// Funcion que ordena la matriz de manera ascendente o descendente.
void ordenarMatriz(){
    int nArreglo = n*n;
    int arreglo [nArreglo];
    int k = 0;
    int kAsc = 0;
    int kDesc = 0;

    //Llenando arreglo con los valores de la matriz.
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j ++){
            arreglo[k] = matriz[i][j];
            k++;
        }
    }

    int opcion;
    cout << "De que manera quiere ordenar la matriz?" << endl;
    cout << "1. De manera ASCENDENTE" << endl;
    cout << "2. De manera DESCENDENTE" << endl;
    cout << "Elija la opcion: ";
    cin >> opcion;
    cout << endl;

    // Una vez ordenado el arreglo con los valores de la matriz, volvemos a cargar la matriz con los valores ordenados.
    int temp, pos;
    switch(opcion){
        
        // ASCENDENTE
        case 1:
            for ( int i = 0; i < nArreglo; i++){
                pos = i;
                while((pos > 0) && (arreglo[pos - 1] > arreglo[pos])) {
                    temp = arreglo[pos];
                    arreglo[pos] = arreglo[pos - 1];
                    arreglo[pos - 1] = temp;
                    pos--;
                }
            }

            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    matriz[i][j] = arreglo[kAsc];
                    kAsc++;
                }
            }
            cout << "Su matriz esta ordenada de manera ascendente y es la siguiente: " << endl;
            for (int i = 0; i<n; i++){
                for (int j = 0; j < n; j++){
                    cout << matriz[i][j] << "\t";
                }
                cout << endl;
            }
            break;

        // DESCENDENTE
        case 2:
            for (int i = nArreglo-1; i >= 0; i--){
                pos = i;
                while((pos < nArreglo-1) && (arreglo[pos+1] > arreglo[pos])){
                    temp = arreglo[pos];
                    arreglo[pos] = arreglo[pos + 1];
                    arreglo[pos + 1] = temp;
                    pos++;
                }
            }

            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    matriz[i][j] = arreglo[kDesc];
                    kDesc++;
                }
            }

            cout << "Su matriz esta ordenada de manera descendente y es la siguiente: " << endl;
            for (int i = 0; i<n; i++){
                for (int j = 0; j < n; j++){
                    cout << matriz[i][j] << "\t";
                }
                cout << endl;
            }
            break;
    }

    int volver;
    cout << "Desea volver al menu interactivo?" << endl;
    cout << "1. Si" << endl;
    cout << "2. No" << endl;
    cout << "> Elija la opcion: ";
    cin >> volver;

    switch(volver){
        case 1:
            main();
            break;
        case 2:
            cout << ".\n..\n...\n...." << endl;
            cout << "Saliste del programa" << endl;
            break;
    }
}

void mensajeErrorMatrizVacia(){
    cout << "PRIMERO DEBE CARGAR LA MATRIZ." << endl;
    cout << "Desea volver al menu principal?" << endl;
    cout << "1. SI" << endl;
    cout << "2. NO" << endl;
    cout << "> Elija la opcion: ";
    int op;
    cin >> op;
    switch (op){
        case 1:
            main();
            break;
        case 2:
            cout << ".\n..\n...\n...." << endl;
            cout << "Saliste del programa" << endl;
            break;
    }
}