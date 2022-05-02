# db
from utils.connection import Conection
connection = Conection()

# models
from models.team import Team


if __name__ == '__main__':
  is_runing = True
  while is_runing:
    # -------- Menu de opciones ------------------#
    print("\n(1) Ver equipos")
    print("(2) Crear equipo")
    print("(3) Buscar equipo")
    print("(4) Salir")
    option = input("Elija una de las operaciones:")
    
    # -------- Obtener todo los equipos ------------------#
    if option == "1":
      result = connection.get_data("SELECT * FROM teams")
      team_list = result
      print(team_list)
      
    # -------- Crear equipo ------------------#
    elif option == "2":
      try:
        data = (
          None,
          input("Nombre del equipo: "),
          input("País: "),
          input("Nombre del director: "),
          input("Marca de la bicicleta: "),
          input("Marca del computador: "),
          input("Dirección de la sede: "),
          input("Número de teléfono: "),
          input("Correo electrónico: ")
        )
        team = Team(connection, data)
        team.save()
        print("Equipo creado!")
      except Exception as e:
        print('Error!', e)
        
    # -------- Buscar equipo por id ------------------#  
    elif option == "3":
      try:
        result = connection.get_data("SELECT * FROM teams WHERE team_number = '{}'".format(input("Número del equipo: ")))
        if len(result) == 0:
          print("No se encontró el equipo")
          continue
        team = Team(connection, result[0])
        print("\n", team)
        
        print("\n(1) Actualizar sede\n(otra tecla) Salir")
        operation = input("Elija una de las operaciones:")
        
        # -------- Actualizar sede ------------------#
        if operation == "1":
          try:
            team.update_headquarters_address(input("Dirección de la sede: "))
            print("Equpo actualizado!")
          except Exception as e:
            print('Error!', e)
            
      except Exception as e:
        print('Error!', e)
      
    # -------- Salir ------------------#
    elif option == "4":
      is_runing = False
      
    else:
      print("Opcion no valida")