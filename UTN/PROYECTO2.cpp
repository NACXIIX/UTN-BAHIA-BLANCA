#include <iostream>

using namespace std;

int main(){
    short int dia, mes;
    cout << "ingrese el mes de su nacimiento: ";
    cin >> mes;
    cout << "Ahora ingrese el dia de su nacimiento: ";
    cin >> dia;
if (mes >= 1 && mes <= 12){
    if (mes == 1){
        if(dia <= 20){ 
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: CAPRICORNIO" << endl;
        } else if (dia >= 21 && dia <= 31) {
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: ACUARIO" << endl;
        } else {
            cout << "DATOS INCORRECTOS" << endl;
        }
    } else if (mes == 2){
        if (dia <= 19){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: ACUARIO" << endl; 
        }
        else if (dia >= 20 && dia <=28){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: PISCIS" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 3){
        if (dia <= 20){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: PISCIS" << endl; 
        }
        else if (dia >= 21 && dia <=31){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: ARIES" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 4){
        if (dia <= 19){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: ARIES" << endl; 
        }
        else if (dia >= 20 && dia <=30){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: TAURO" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 5){
        if (dia <= 20){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: TAURO" << endl; 
        }
        else if (dia >= 21 && dia <=31){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: GEMINIS" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 6){
        if (dia <= 21){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: GEMINIS" << endl; 
        }
        else if (dia >= 22 && dia <=30){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: CANCER" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 7){
        if (dia <= 22){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: CANCER" << endl; 
        }
        else if (dia >= 23 && dia <=31){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: LEO" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 8){
        if (dia <= 23){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: LEO" << endl; 
        }
        else if (dia >= 24 && dia <=31){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: VIRGO" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 9){
        if (dia <= 22){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: VIRGO" << endl; 
        }
        else if (dia >= 23 && dia <=30){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: LIBRA" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 10){
        if (dia <= 22){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: LIBRA" << endl; 
        }
        else if (dia >= 23 && dia <=31){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: ESCORPIO" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 11){
        if (dia <= 22){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: ESCORPIO" << endl; 
        }
        else if (dia >= 23 && dia <=30){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: SAGITARIO" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    } else if (mes == 12){
        if (dia <= 22){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: SAGITARIO" << endl; 
        }
        else if (dia >= 23 && dia <=31){
            cout << "Dia: " << dia << endl;
            cout << "Mes: " << mes << endl;
            cout << "Signo del zodiaco: CAPRICORNIO" << endl; 
        } else {
            cout << "DATOS INCORRECTOS";
        }
    }
} else {
    cout << "DATOS INCORRECTOS" << endl;
}

    
    return 0;

}