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
    cargarPrecios();
    leerPrecios();

    return 0;
}

void cargarPrecios(){
    ofstream archivito;
    string nombreArchivito;
    cout << "Escriba el nombre del archivo: ";
    getline(cin,nombreArchivito);

    archivito.open(nombreArchivito.c_str(),ios::out);
    
    if (archivito.is_open()){
        cout << "Ingrese el ID del producto: ";
        getline(cin,archivito);
        archivito<<"Coca" << ",";
        archivito<<"Coca" << "," << endl;
        archivito<<"1,";
        archivito<<"3,";
        archivito<<"2,";
    } else {
        cout << "Hubo un error.";
    }
}

void leerPrecios(){
    ifstream archivo("a.csv");
    string linea;
    char delimitador = ','; // Este lo uso si quiero mostrar cada valor separado por coma
    char saltoDeLinea = '\n'; // Este lo uso si quiero mostrar fila por fila.

    if (archivo.is_open()){
        getline(archivo,linea);

        while (getline(archivo,linea)){
            stringstream ss(linea);
            string idProducto, producto, volumen, precio, stock;

            cout << "----\t----\t----\t";
            getline(ss,idProducto,delimitador);
                cout << "\nID Producto:" << idProducto << endl;
            getline(ss,producto,delimitador);
                cout << "Producto:" << producto << endl;
            getline(ss,volumen,delimitador);
                cout << "Volumen:" << volumen << endl;
            getline(ss,precio,delimitador);
                cout << "Precio:" << precio << endl;
            getline(ss,stock,delimitador);
                cout << "Stock:" << stock << endl;
        }

        archivo.close();
    } else {
        cout << "Hubo un error al intentar abrir el archivo.";
    }
}