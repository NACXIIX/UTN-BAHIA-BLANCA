#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#define coca "cocacola.csv" //  En la def coca almacenamos la ruta del archivo.

using namespace std;

// Prototipos de funcion
void LeerPrecios();

// Programa principal
int main(){
    LeerPrecios();

    return 0;
}

void LeerPrecios(){
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