#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){
    short unsigned int Dia, Mes;
    cout << "ingrese el mes de su nacimiento: ";
    cin >> Mes;
    cout << "Ahora ingrese el dia de su nacimiento: ";
    cin >> Dia;

    if (Mes >= 1 && Mes <= 12){
        if (Mes == 1){
            if(Dia <= 20){ 
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: CAPRICORNIO" << endl;
            } else if (Dia >= 21 && Dia <= 31) {
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: ACUARIO" << endl;
            } else {
                cout << "DATOS INCORRECTOS" << endl;
            }
        } else if (Mes == 2){
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
        } else if (Mes == 3){
            if (Dia <= 20){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: PISCIS" << endl; 
            }
            else if (Dia >= 21 && Dia <=31){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: ARIES" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 4){
            if (Dia <= 19){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: ARIES" << endl; 
            }
            else if (Dia >= 20 && Dia <=30){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: TAURO" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 5){
            if (Dia <= 20){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: TAURO" << endl; 
            }
            else if (Dia >= 21 && Dia <=31){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: GEMINIS" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 6){
            if (Dia <= 21){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: GEMINIS" << endl; 
            }
            else if (Dia >= 22 && Dia <=30){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: CANCER" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 7){
            if (Dia <= 22){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: CANCER" << endl; 
            }
            else if (Dia >= 23 && Dia <=31){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: LEO" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 8){
            if (Dia <= 23){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: LEO" << endl; 
            }
            else if (Dia >= 24 && Dia <=31){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: VIRGO" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 9){
            if (Dia <= 22){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: VIRGO" << endl; 
            }
            else if (Dia >= 23 && Dia <=30){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: LIBRA" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 10){
            if (Dia <= 22){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: LIBRA" << endl; 
            }
            else if (Dia >= 23 && Dia <=31){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: ESCORPIO" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 11){
            if (Dia <= 22){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: ESCORPIO" << endl; 
            }
            else if (Dia >= 23 && Dia <=30){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: SAGITARIO" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        } else if (Mes == 12){
            if (Dia <= 22){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: SAGITARIO" << endl; 
            }
            else if (Dia >= 23 && Dia <=31){
                cout << "Dia: " << Dia << endl;
                cout << "Mes: " << Mes << endl;
                cout << "Signo del zodiaco: CAPRICORNIO" << endl; 
            } else {
                cout << "DATOS INCORRECTOS";
            }
        }
    } else {
        cout << "DATOS INCORRECTOS" << endl;
    }

    // PREGUNTARLE AL USUARIO SI LE GUSTA FESTEJAR SU CUMPLEAÑOS
    
    string Pregunta;
    cout << "\n\nTe gusta festejar tu cumpleaños? " << endl;
    cin.ignore();
    getline (cin, Pregunta);

    if (Pregunta == "Si" || Pregunta == "si" || Pregunta == "SI" || Pregunta == "sI"){
        cout << "Que bueno";
    } else if ( Pregunta == "No" || Pregunta == "no" || Pregunta == "NO" || Pregunta == "nO"){
        cout << "Que lastima";
    } else {
        cout << "ERROR. Las unicas respuestas permitidas son SI y NO";
    }
    
    // PREGUNTARLE AL USUARIO LA CANTIDAD DE INVITADOS

    float Invitados;
    double Total_invitados;
    cout << "\n\nPorfavor ingrese el numero de invitados para su cumpleaños: ";
    cin >> Invitados;

    Total_invitados = round(sqrt(pow(Invitados, 4)));

    cout << "\n\n Tus invitados a la cuarta, raiz cuadrado y redondeando el valor son: " << Total_invitados;

    return 0;
}