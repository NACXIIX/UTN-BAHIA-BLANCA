#include <iostream>
#include <cstdlib> // Para generar numeros aleatorios
#include <ctime> // Obtener la semilla de los numeros aleatorios
using namespace std;

// ---------------FUNCIONES GLOBALES --------------- //
const int n = 3;
int filas = n;
int columnas = n;
bool validacionMatrizCargada = false;
int matriz[n][n];

// --------------- PROTOTIPOS DE FUNCIONES --------------- //
int menu();
void cargarMatriz(int matriz[][n], int filas, int columnas);
void mostrarMatriz(int matriz[][n], int filas, int columnas);
void buscarValor(int matriz[][n], int filas, int columnas);
void devolverValor(int matriz[][n], int filas, int columnas);
void ordenarMatriz(int matriz[][n], int filas, int columnas);
void opcionesMenu();
void consultarVueltaAlMenu();
void mensajeErrorMatrizVacia();

// --------------- PROGRAMA PRINCIPAL --------------- //
int main(){

    cout << "\n\t-----Bienvenidos al Menu Interactivo-----" << endl;
    opcionesMenu();

    return 0;
}

// --------------- FUNCION CREADA PARA EVITAR RECURSIVIDAD A LA FUNCION MAIN --------------- //
void opcionesMenu(){
    int op = menu();
    switch(op){
        case 1: 
            cargarMatriz(matriz, filas, columnas);
            break;
        case 2:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                mostrarMatriz(matriz, filas, columnas);
            }
            break;
        case 3:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                buscarValor(matriz, filas, columnas);
            }
            break;
        case 4:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                devolverValor(matriz, filas, columnas);
            }
            break;
        case 5:
            if (!validacionMatrizCargada){
                mensajeErrorMatrizVacia();
            } else {
                ordenarMatriz(matriz, filas, columnas);
            }
            break;
        case 6:
            cout << ".\n..\n...\n...." << endl;
            cout << "Saliste del programa" << endl;
            break;
    }
}

// --------------- MENU INTERACTIVO --------------- //
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

// --------------- LLENADO DE LA MATRIZ --------------- //
void cargarMatriz(int matriz[][n], int filas, int columnas){
    srand(time(NULL)); // Se inicializa la semilla para generar num aleatorios.
    int respuesta;
    bool cortarMatriz = false; // Booleano para mantener el control de que la digitacion manual de la matriz se corte en los bucles si se digita un numero invalido

    do{
        cout << "Elija de que manera desea cargar la matriz 3x3 [Valores permitidos del 1 al 100 inclusive]" << endl;
        cout << "1. Valores aleatorios" << endl;
        cout << "2. De manera manual" << endl;
        cout << "3. Volver al menu" << endl;
        cout << "> Elija la opcion: ";
        cin >> respuesta;

        switch (respuesta){
        case 1:
            for(int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    matriz[i][j] = rand() % 100+1; // se generan num aleatrios entre 1-100
                }
            }
            validacionMatrizCargada = true;
            break;
        case 2:
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    cout << "Digite el numero [" <<i<< "][" <<j<<"]: "; // Numeros de manera manual
                    cin >> matriz[i][j];
                    if ((matriz[i][j] <= 0) || (matriz[i][j] > 100)){
                        cout << "\nPOR FAVOR LA PROXIMA VEZ DIGITE UN NUMERO VALIDO. \nRECUERDE QUE LOS NUMEROS VALIDOS SON DE 1 AL 100. \nLLENE LA MATRIZ NUEVAMENTE.";
                        cortarMatriz = true; // Se digito mal, cortarmatriz se pasa a valor verdadero
                        break; // Salimos del bucle for interno ya que hubo un error de digitacion (Salimos con cortarmatriz en true)
                    } 
                }
                if (cortarMatriz == true){ // En el bucle for externo se ve que cortarmatriz esta en true asique tambien lo cortamos con un break
                    break;
                } else {
                    validacionMatrizCargada = true; // Si no existen cortes en la digitacion de la matriz verificamos que se cargo correctamente y validamos la carga
                };
            }
            break;
        case 3:
            main();
            break;
        }
    } while (respuesta != 1 && respuesta != 2 && respuesta !=3);

    if (respuesta != 3){
        main();
    }
}

    // --------------- MOSTRANDO LA MATRIZ --------------- //
void mostrarMatriz(int matriz[][n], int filas, int columnas){
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

    cout << "Esa es su matriz cargada. \n";
    consultarVueltaAlMenu();
}

// --------------- BUSQUEDA DE UN VALOR INGRESADO POR EL USUARIO DENTRO DE LA MATRIZ --------------- //
void buscarValor(int matriz[][n], int filas, int columnas){
    int numero, volver;
    bool encontrado = false;
    cout << "Digite el valor que esta buscando" << endl;
    cout << "> ";
    cin >> numero;

    for(int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if(matriz[i][j] == numero){
                encontrado = true; // Se encontro
                cout << "Tu numero se encontro en la posicion : [" << i << "][" << j << "]\n"; // Lo mostramos
            }
        }
    }

    if (!encontrado){
        cout << "El numero que ingresaste no se ha encontrado.\n" << endl;
    }

    consultarVueltaAlMenu();
}

// --------------- RETORNO DE VALOR MAXIMO O MINIMO DE LA MATRIZ --------------- //
void devolverValor(int matriz[][n], int filas, int columnas){
    int nArreglo = n*n;
    int arreglo [nArreglo];
    int k = 0;
    int mayor = 0;
    int menor = 100;
    int opcion;
    int valorDevuelto;
    
    // Llenando arreglo con los valores de la matriz.
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j ++){
            arreglo[k] = matriz[i][j];
            k++;
        }
    }

    //Se guarda en las variables menor y mayor sus valores respectivos.
    for(int i = 0; i < nArreglo; i++){
        if (arreglo[i] < menor){
            menor = arreglo[i];
        }
    
        if (arreglo[i] > mayor){
            mayor = arreglo[i];
        }
    }

    do {
        cout << "Estas buscando el menor o el mayor?" << endl;
        cout << "1. Mayor" << endl;
        cout << "2. Menor" << endl;
        cout << "3. Volver al menu\n";
        cout << "> Elija la opcion: ";
        cin >> opcion;
        if (opcion < 1 || opcion > 3) {
            cout << "\nRecuerde de elegir la opcion 1,2 o 3." << endl;
        }
    } while (opcion < 1 || opcion > 3);

    switch (opcion){
        case 1:
            valorDevuelto = mayor;
            break;
        case 2:
            valorDevuelto = menor;
            break;
        case 3:
            main();
    }
    
    if (opcion == 1){
    cout << "\nEl valor mayor es: " << valorDevuelto << '\n' << endl;
    } else if (opcion == 2){
    cout << "\nEl valor menor es: " << valorDevuelto << '\n' << endl;
    }

    if (opcion == 1 || opcion == 2){
        consultarVueltaAlMenu();
    }
}

// --------------- ORDENAMIENTO ASCENDENTE O DESCENDENTE DE LA MATRIZ --------------- //
void ordenarMatriz(int matriz[][n], int filas, int columnas){
    int nArreglo = n*n;
    int arreglo [nArreglo];
    int k = 0; // variable para controlar el llenado del arreglo con los valores de la matriz
    int kAsc = 0; // variable para controlar el llenado del arreglo de forma ascendente
    int kDesc = 0; // variable para controlar el llenado del arreglo de forma ascendente

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
        
        // Mostramos la matriz de manera ascendente
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

        //  Mostramos la matriz de manera descendente
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
    consultarVueltaAlMenu();
}

// ---------------  CONSULTAMOS AL USUARIO SI DESEA VOLVER AL MENU --------------- //
void consultarVueltaAlMenu(){
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
        default:
            cout << "Recuerde elegir entre la opcion 1 o 2." << endl;
            consultarVueltaAlMenu();
            break;
    }
}

// ---------------  FUNCION QUE MUESTRA MENSAJE DE ERROR --------------- //
void mensajeErrorMatrizVacia(){
    cout << "PRIMERO DEBE CARGAR LA MATRIZ." << endl;
    consultarVueltaAlMenu();
}