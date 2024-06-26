#include <iostream>

using namespace std;

int main(){
    short unsigned int Dia, Mes;
    cout << "ingrese el mes de su nacimiento: ";
    cin >> Mes;
    cout << "Ahora ingrese el dia de su nacimiento: ";
    cin >> Dia;

    if (Mes >= 1 && Mes <= 12){
        switch(Mes){
            case 1: // enero
                if(Dia <=20){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: CAPRICORNIO" << endl;
                    break;
                } else {
                    if (Dia > 20 && Dia <= 31){
                        cout << "Dia: " << Dia << endl;
                        cout << "Mes: " << Mes << endl;
                        cout << "Signo del zodiaco: ACUARIO" << endl;
                    
                    } else {
                        cout << "Datos incorrectos";
                    }
                }
                break;
            case 2: // febrero
                if (Dia < 20){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: ACUARIO";
                    
                } else {
                    if (Dia >= 20 && Dia <= 28){
                        cout << "Dia: " << Dia << endl;
                        cout << "Mes: " << Mes << endl;
                        cout << "Signo del zodiaco: PISCIS";
                    } else {
                        cout << "Datos incorrectos";
                    }
                }
                break;
            case 3: // marzo
                if(Dia <= 20){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: PISCIS";
                } else {
                    if (Dia >= 21 && Dia <= 31){
                        cout << "Dia: " << Dia << endl;
                        cout << "Mes: " << Mes << endl;
                        cout << "Signo del zodiaco: ARIES";
                    } else {
                        cout << "Datos incorrectos";
                    }
                }
                break;
            case 4: // abril
                if(Dia <= 19){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: ARIES" << endl;
                } else {
                    if (Dia >= 20 && Dia <= 30){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: TAURO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 5: //mayo
                if(Dia <= 20){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: TAURO" << endl;
                } else {
                    if (Dia >= 21 && Dia <= 30){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: GEMINIS" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 6: // junio
                if(Dia <= 21){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: GEMINIS" << endl;
                } else {
                    if (Dia >= 22 && Dia <= 30){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: CANCER" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 7: // julio
                if(Dia <= 22){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: CANCER" << endl;
                } else {
                    if (Dia >= 23 && Dia <= 31){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: LEO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 8: // agosto
                if(Dia <= 23){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: LEO" << endl;
                } else {
                    if (Dia >= 24 && Dia <= 31){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: VIRGO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 9: // septiembre
                if(Dia <= 22){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: VIRGO" << endl;
                } else {
                    if (Dia >= 23 && Dia <= 30){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: LIBRA" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 10: // octubre
                if(Dia <= 22){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: LIBRA" << endl;
                } else {
                    if (Dia >= 23 && Dia <= 31){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: ESCORPIO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 11: // noviembre
                if(Dia <= 22){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: ESCORPIO" << endl;
                } else {
                    if (Dia >= 23 && Dia <= 30){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: SAGITARIO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 12: // diciembre
                if(Dia <= 21){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: SAGITARIO" << endl;
                } else {
                    if (Dia >= 22  && Dia <= 31){
                    cout << "Dia: " << Dia << endl;
                    cout << "Mes: " << Mes << endl;
                    cout << "Signo del zodiaco: CAPRICORNIO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
        }
    } else {
        cout << "Datos incorrectos";
    }

        
    return 0;

}