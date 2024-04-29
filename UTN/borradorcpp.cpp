#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main () {
    int Mes, Dia;
    string bisiesto;
    cout << "ingrese mes" << endl;
    cin >> Mes;
    cout << "ingrese dia" << endl;
    cin >> Dia;

    // año normal
        if (Mes == 2){
            cout << "El año es bisiesto? Si o no?";
            cin >> bisiesto;
            if (bisiesto == "Si" || bisiesto == "si" || bisiesto == "SI" || bisiesto == "sI"){
                if (Dia <= 19){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: ACUARIO" << endl; 
                }
                else if (Dia >= 20 && Dia <=29){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: PISCIS" << endl; 
                } else {
                    cout << "DATOS INCORRECTOS";
                }
            } else {
                if (Dia <= 19){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: ACUARIO" << endl; 
                }
                else if (Dia >= 20 && Dia <=28){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: PISCIS" << endl; 
                } else {
                    cout << "DATOS INCORRECTOS";
                }
            }
        }


    return 0;
}