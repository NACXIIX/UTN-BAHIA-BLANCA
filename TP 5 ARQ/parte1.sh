#! /bin/bash
echo "-- BIENVENIDOS A LA CALCULADORA DEL TP5 --"
echo "Porfavor digite dos numeros"
echo "Numero 1: "
read numero1
echo "Numero 2: "
read numero2


echo "Que operacion desea realizar?"
echo "1. SUMA"
echo "2. RESTA"
echo "3. MULTIPLICACION"
echo "4. DIVISION"
read opcion

case $opcion in
    1)
        echo "RESULTADO: $(( numero1 + numero2))"
    ;;
    2)
        echo "RESULTADO: $(( numero1 - numero2))"
    ;;
    3)
        echo "RESULTADO: $(( numero1 * numero2))"
    ;;
    4)
        echo "RESULTADO: $(( numero1 / numero2))"
esac