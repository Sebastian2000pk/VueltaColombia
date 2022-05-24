
# db
from utils.connection import Conection
connection = Conection()

# controllers
from controllers.teams import Teams
from controllers.cyclists import Cyclists
from controllers.lamp import Lamps
from controllers.classification import Classification



if __name__ == '__main__':
  is_runing = True
  while is_runing:
    # -------- Menu de opciones ------------------#
    print("""
    --------------------------------------
        1. Equipos  
        2. Ciclistas
        3. Etapas
        4. Clasificación
        5. Salir
    --------------------------------------
    """)
    option = int(input("Elija una de las operaciones: "))
    
    # -------------------------- Equipos --------------------------------------#
    if option == 1:
      option = 0

      while option != 4:
        print("""
        --------------------------------------
                      EQUIPOS
        --------------------------------------
            1. Ver
            2. Crear
            3. Editar
            4. regresar
        --------------------------------------
        """)

        option = int(input("digita la opción: "))

        # Obtener la lista de equipos -----------------
        if option == 1:
          team = Teams(connection)
          result = team.get_data()
          print(result)
         
        # Crear un equipo  ----------------------------
        elif option == 2:
          try:
            data = (
              input("Nombre del equipo: "),
              input("País: "),
              input("Nombre del director: "),
              input("Marca de la bicicleta: "),
              input("Marca del computador: "),
              input("Dirección de la sede: "),
              int(input("Número de teléfono: ")),
              input("Correo electrónico: ")
            )
            team = Teams(connection)
            team.create(data)
            
          except Exception as e:
            print(e)
          
        # Actualizar sede de un equipo ----------------
        elif option == 3:
          team = Teams(connection)
          try:
            team.update_headquarters_address(int(input("Número de equipo: ")), input("Dirección de la sede: "))
          except Exception as e:
            print(e)
        
        elif option == 4:
          print("Regresando...")
          continue
        
        else:
          print("Opción incorrecta, digítala nuevamente.")
          continue
        
          
    # -------------------------- Ciclistas --------------------------------------#
    elif option == 2: 
      option = 0

      while option != 4:

        print("""
        --------------------------------------
                       CICLISTAS
        --------------------------------------
            1. Ver
            2. Crear
            3. Editar
            4. regresar
        --------------------------------------
        """)
        option = int(input("digita la opción: "))

        # Ver los ciclistas ----------------
        if option == 1:
          cyclist = Cyclists(connection)
          print(cyclist.get_data())
          
        # Crear ciclista ----------------
        elif option == 2:
          try:
            cyclist = Cyclists(connection)
            
            cyclist.create((
              int(input("Ingresa el número de identificación del ciclista: ")),
              input("Ingresa el nombre del ciclista: "),
              input("Ingresa el apellido del ciclista: "),
              input("Ingresa la fecha de nacimiento del ciclista (DD/MM/AAAA): "),
              input("Ingresa el país del ciclista: "),
              int(input("Ingresa el número del equipo: ")),
              input("Ingresa la foto del ciclista: "),
              int(input("Ingresa el ranking de UCI: ")),
            ))
            
          except Exception as e:
            print(e)
          
        # Actualizar ranking UCI ----------------
        elif option == 3:
          try:
            cyclist = Cyclists(connection)
            regitration_number = int(input("Ingresa el número de registro del ciclista: "))
            position = int(input("Ingresa la posición del ciclista: "))
            cyclist.update_ranking_cyclist(regitration_number, position)
            
          except Exception as e:
            print(e)
            
            
        elif option == 4:
          print("Regresando...")
          continue
        else:
          print("Opción incorrecta, digítala nuevamente.")  
          continue
          
    # -------------------------- Etapas --------------------------------------#
    elif option == 3: 
      print("""
        --------------------------------------
                       ETAPAS
        --------------------------------------
            1. Ver etapa
            2. Registrar etapas
            3. Editar registro de etapa
            4. regresar
        --------------------------------------
        """)
      option = int(input("digita la opción: ")) 
      
      # Ver etapa -----------------------------------
      if option == 1:
        lamp = Lamps(connection)
        lamp_number = int(input("Ingresa el número de la etapa: "))
        result = lamp.get_data(lamp_number)
        print(result)
      
      # Crear registro etapa -----------------------------------
      elif option == 2:
        try:
          lamp = Lamps(connection)
          lamp.create((
            int(input("Ingresa el número de la etapa: ")),
            int(input("Ingresa el número de registro del ciclista: ")),
            int(input("Ingresa la position en la etapa: ")),
            input("Ingresa tiempo que usó (HH:MM): "),
            int(input('Ingrese el número del equipo: ')),
            int(input('El ciclista se retiró (0) No (1) Si: '))
          ))
        except Exception as e:
          print(e)
          
      # Crear registro etapa -----------------------------------
      elif option == 3:
        try:
          lamp = Lamps(connection)
          lamp.update(
            int(input("Ingresa id del registro: ")),
            int(input("Ingresa el número de registro del ciclista: ")),
            int(input("Ingresa la position en la etapa: ")),
            input("Ingresa tiempo que usó (HH:MM:SS): "),
            int(input('Ingrese el número del equipo: ')),
            int(input('El ciclista se retiró (0) No (1) Si: '))
          )
        except Exception as e:
          print(e)
        
          
      else:
        print("Opción incorrecta, digítala nuevamente.") 
        continue
      
    # -------------------------- Clasificación --------------------------------------#
    elif option == 4: 
      print("""
        --------------------------------------
                    CLASIFICACIÓN
        --------------------------------------
            1. Etapa
            2. General
            3. Equipo (Etapa)
            4. Equipo (General)
        --------------------------------------
        """)
      option = int(input("digita la opción: ")) 
      
      # Clasificación por etapa ------------------------------
      if option == 1:
        try:
          classificaciont = Classification(connection)
          lamp_number = int(input("Ingresa el número de la etapa: "))
          result = classificaciont.get_lamp(lamp_number)
          print(result)
          
        except Exception as e:
          print(e)
        
      # Clasificación general -----------------------------------  
      elif option == 2:
        try:
          classificaciont = Classification(connection)
          result = classificaciont.general
          print(result)
          
        except Exception as e:
          print(e)
        
      # Clasificación etapa por equipo -------------------------  
      elif option == 3:
        try:
          classificaciont = Classification(connection)
          team_number = int(input("Ingrese el número del equipo: "))
          lamp_number = int(input("Ingrese el número de la etapa: "))
          result = classificaciont.lamp_team(team_number, lamp_number)
          print(result)
          
        except Exception as e:
          print(e)
        
      # Clasificación general por equipo -------------------------  
      elif option == 4:
        try:
          classificaciont = Classification(connection)
          team_number = int(input("Ingrese el número del equipo: "))
          result = classificaciont.general_team(team_number)
          print(result)
          
        except Exception as e:
          print(e)
                
    elif option == 5:
      is_runing = False
      print("Saliendo...")
      
    else:
      print("Opción incorrecta, digítala nuevamente.")
      