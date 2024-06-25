#include <iostream>
#include <string>
using namespace std;

/*
a) Crea una estructura "Estudiante" con los campos "nombre", "edad" y "notas" (este 
campo debe almacenar la nota de los 3 parciales). Crea un arreglo de estructuras de 
tamaño 3 y permite que el usuario ingrese los datos de los estudiantes.

b) Mostrar la nota más alta de cada estudiante de forma clara.

c) Calcular y mostrar el promedio de cada alumno y el promedio general del curso.

d) Modificar la nota del tercer parcial del segundo estudiante. Si tiene una nota menor que 
60, se le debe sumar el 25%, si la nota está entre 60 y 80 se le debe sumar el 5% y si es 
mayor que 80 debe restar el 3%

*/

struct Notas{
    int nota1;
    int nota2;
    int nota3;
};

struct Estudiante{
    string nombre;
    int edad;
    struct Notas nota;
}Estudiante[3];

int main(){
    double sumatoriaNotasIndividual = 0, cantidadNotas = 0;
    double sumatoriaNotasGeneral = 0;
    double mayorNota = 0;

    //Llenando campos de los estudiantes
    for(int i = 0; i < 3; i++){
        fflush(stdin);
        cout << "Ingrese el nombre del estudiante: ";
        getline(cin, Estudiante[i].nombre);

        cout << "Ingrese la edad del estudiante: ";
        cin >> Estudiante[i].edad;

        cout << "Ingrese la primer nota del estudiante: ";
        cin >> Estudiante[i].nota.nota1;

        fflush(stdin);

        cout << "Ingrese la segunda nota del estudiante: ";
        cin >> Estudiante[i].nota.nota2;
        cout << "Ingrese la tercer nota del estudiante: ";
        cin >> Estudiante[i].nota.nota3;

        cout << endl;
    }

    //Mostrar nota mayor del estudiante.
    for (int i = 0; i < 3; i++){
        if ( (Estudiante[i].nota.nota1 >= Estudiante[i].nota.nota2) && (Estudiante[i].nota.nota1 >= Estudiante[i].nota.nota3) ){
            cout << "La nota mas alta del estudiante " << Estudiante[i].nombre << " es: " << Estudiante[i].nota.nota1 << endl;
        } else if (Estudiante[i].nota.nota2 >= Estudiante[i].nota.nota3){
            cout << "La nota mas alta del estudiante " << Estudiante[i].nombre << " es: " << Estudiante[i].nota.nota2 << endl;
        } else {
            cout << "La nota mas alta del estudiante " << Estudiante[i].nombre << " es: " << Estudiante[i].nota.nota3 << endl;
        }
    }
    cout << endl;

    //Mostrar promedio de cada alumno y promedio general del curso.
    for(int i = 0; i < 3; i++){
        sumatoriaNotasIndividual += Estudiante[i].nota.nota1;
        sumatoriaNotasIndividual += Estudiante[i].nota.nota2;
        sumatoriaNotasIndividual += Estudiante[i].nota.nota3;
        cantidadNotas += 3;

        cout << "El promedio del alumno " << Estudiante[i].nombre << " es: " << sumatoriaNotasIndividual / cantidadNotas << endl;
        
        sumatoriaNotasGeneral += sumatoriaNotasIndividual;
        sumatoriaNotasIndividual = 0;
        cantidadNotas = 0;
    }
    cout << "El promedio general del curso es: " << sumatoriaNotasGeneral / 9 << endl;

    //Modificar la nota del tercer parcial.
    
    if (Estudiante[1].nota.nota3 < 60){
        Estudiante[1].nota.nota3 = Estudiante[1].nota.nota3 * 1.25;
    } else if (Estudiante[1].nota.nota3 >= 60 && Estudiante[1].nota.nota3 <= 80){
        Estudiante[1].nota.nota3 = Estudiante[1].nota.nota3 * 1.05;
    } else {
        Estudiante[1].nota.nota3 = Estudiante[1].nota.nota3 - (Estudiante[1].nota.nota3 * 0.03);
    }

    cout << Estudiante[1].nota.nota3;
    
    return 0;
}