#Simulador de cajero automatico

saldo = 1000
Repes = int(input("Cuantas veces desea repertir ? \n"))

for i in range (Repes):

 def menu():
    

    print("\n ==CAJERO==")
    print("1. Consultar saldo")
    print("2. Retirar")
    print("3. depositar")

 menu()
 opcion = int(input("Por favor eliga una opcion: \n"))

 if opcion == 1:
    print (f"Su saldo es: {saldo} ")

 elif opcion == 2:
   Retira = int(input("Que cantidad desea retirar? \n"))
   saldo -= Retira
   print("Retiro exitoso")
   print(f"Su saldo ahora es de: {saldo}")

 elif opcion == 3:
   Deposita = int(input("Que cantidad desea depositar? \n"))
   saldo += Deposita
   print("Deposito exitoso")
   print(f"Su saldo ahora es: {saldo}")

 else:
   print("No es una opcion valida!")