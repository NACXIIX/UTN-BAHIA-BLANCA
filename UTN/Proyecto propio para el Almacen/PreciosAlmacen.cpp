#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

#define coca "cocacola.csv"

using namespace std;

//Prototipos de funcion
void LeerPrecios();


int main(){
    LeerPrecios();

    return 0;
}

void LeerPrecios(){
    ifstream archivo(coca);

    string linea;
    char delimitador = ',';
    if (archivo.is_open()){
        getline(archivo,linea);
    }

}