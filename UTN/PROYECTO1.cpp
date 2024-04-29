#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(){
    int dia, mes;
    cout << "ingrese el mes de su nacimiento: ";
    cin >> mes;
    cout << "Ahora ingrese el dia de su nacimiento: ";
    cin >> dia;

    if (mes <= 12){
        switch(mes){
            case 1: // enero
                if(dia <=20){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: CAPRICORNIO" << endl;
                    break;
                } else {
                    if (dia > 20 && dia <= 31){
                        cout << "Dia: " << dia << endl;
                        cout << "Mes: " << mes << endl;
                        cout << "Signo del zodiaco: ACUARIO" << endl;
                    
                    } else {
                        cout << "Datos incorrectos";
                    }
                }
                break;
            case 2: // febrero
                if (dia < 20){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: ACUARIO";
                    
                } else {
                    if (dia >= 20 && dia <= 28){
                        cout << "Dia: " << dia << endl;
                        cout << "Mes: " << mes << endl;
                        cout << "Signo del zodiaco: PISCIS";
                    } else {
                        cout << "Datos incorrectos";
                    }
                }
                break;
            case 3: // marzo
                if(dia <= 20){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: PISCIS";
                } else {
                    if (dia >= 21 && dia <= 31){
                        cout << "Dia: " << dia << endl;
                        cout << "Mes: " << mes << endl;
                        cout << "Signo del zodiaco: ARIES";
                    } else {
                        cout << "Datos incorrectos";
                    }
                }
                break;
            case 4: // abril
                if(dia <= 19){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: ARIES" << endl;
                } else {
                    if (dia >= 20 && dia <= 30){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: TAURO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 5: //mayo
                if(dia <= 20){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: TAURO" << endl;
                } else {
                    if (dia >= 21 && dia <= 30){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: GEMINIS" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 6: // junio
                if(dia <= 21){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: GEMINIS" << endl;
                } else {
                    if (dia >= 22 && dia <= 30){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: CANCER" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 7: // julio
                if(dia <= 22){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: CANCER" << endl;
                } else {
                    if (dia >= 23 && dia <= 31){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: LEO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 8: // agosto
                if(dia <= 23){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: LEO" << endl;
                } else {
                    if (dia >= 24 && dia <= 31){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: VIRGO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 9: // septiembre
                if(dia <= 22){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: VIRGO" << endl;
                } else {
                    if (dia >= 23 && dia <= 30){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: LIBRA" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 10: // octubre
                if(dia <= 22){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: LIBRA" << endl;
                } else {
                    if (dia >= 23 && dia <= 31){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: ESCORPIO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 11: // noviembre
                if(dia <= 22){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: ESCORPIO" << endl;
                } else {
                    if (dia >= 23 && dia <= 30){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: SAGITARIO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
            case 12: // diciembre
                if(dia <= 21){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: SAGITARIO" << endl;
                } else {
                    if (dia >= 22  && dia <= 31){
                    cout << "Dia: " << dia << endl;
                    cout << "Mes: " << mes << endl;
                    cout << "Signo del zodiaco: CAPRICORNIO" << endl;
                    } else {
                        cout << "Datos incorrectos" << endl;
                    }
                }
                break;
        }
    } else {
        cout << "Numero de mes invalido, ingrese un numero de mes entre el 1 y el 12";
    }

    // PREGUNTARLE AL USUARIO SI LE GUSTA FESTEJAR SU CUMPLEAÑOS
    
    string pregunta;
    cout << "\n\nTe gusta festejar tu cumpleaños? " << endl;
    cin.ignore();
    getline (cin, pregunta);

    if (pregunta == "Si" || pregunta == "si" || pregunta == "SI" || pregunta == "sI"){
        cout << "Que bueno";
    } else if ( pregunta == "No" || pregunta == "no" || pregunta == "NO" || pregunta == "nO"){
        cout << "Que lastima";
    } else {
        cout << "ERROR. Las unicas respuestas permitidas son SI y NO";
    }
    
    // PREGUNTARLE AL USUARIO LA CANTIDAD DE INVITADOS

    float invitados;
    double total_invitados;
    cout << "\n\nPorfavor ingrese el numero de invitados para su cumpleaños: ";
    cin >> invitados;

    total_invitados = round(sqrt(pow(invitados, 4)));

    cout << "\n\n Tus invitados a la cuarta, raiz cuadrado y redondeando el valor son: " << total_invitados;

    return 0;
}