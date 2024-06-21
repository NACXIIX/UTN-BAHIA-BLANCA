#!/bin/bash
// Usar la API de weatherapi.com para obtener el clima actual de una ciudad

# ApiKEY
apiKEY="2aa68ad99f2648c9906160348242106"

read -p "Ingrese una ciudad para saber su clima actual: " ciudad
ciudad_ingresada=$(echo $ciudad_ingresada | tr ' ' '%20')

url="http://api.weatherapi.com/v1/current.json?key=$apiKEY&q=$ciudad_ingresada&aqi=no"

curl --request GET $url > response.json