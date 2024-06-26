#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#define coca "cocacola.csv" //  En la def coca almacenamos la ruta del archivo.

using namespace std;

// Prototipos de funcion
void cargarPrecios();
void leerPrecios();

// Programa principal
int main(){
    leerPrecios();
    cargarPrecios();
    return 0;
}

void cargarPrecios(){
    ofstream archivito;
    string nombreArchivito;
    cout << "Escriba el nombre del archivo: ";
    getline(cin,nombreArchivito);

    archivito.open(nombreArchivito.c_str(),ios::out);
    
    if (archivito.is_open()){

        archivito<<"Hola, probando probando.. ja" << endl;
        archivito<<"A ver si probamos un tab \t";
        archivito<<"Hola.";
    } else {
        cout << "Hubo un error.";
    }

}


void leerPrecios(){
    ifstream archivo(coca);

    string linea;
    char delimitador = ','; // Este lo uso si quiero mostrar cada valor separado por coma
    char saltoDeLinea = '\n'; // Este lo uso si quiero mostrar fila por fila.

    if (archivo.is_open()){
        getline(archivo,linea);

        while (getline(archivo,linea)){
            stringstream ss(linea);
            string valor;

            while (getline(ss,valor,saltoDeLinea)){
                cout << "Valor: " << valor << endl;
            }
        }

        archivo.close();
    } else {
        cout << "Hubo un error al intentar abrir el archivo.";
    }
}