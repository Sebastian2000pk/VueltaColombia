from sqlite3 import connect

class Conection():
  def __init__(self):
    try:
      self.con = connect('vueltaColombia.db')
      # ----------- tabla de equipos --------------------#
      self.set_data("""CREATE TABLE IF NOT EXISTS teams (
        team_number INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT, 
        country TEXT, 
        name_director TEXT, 
        bike_brand TEXT,
        bike_computer_brand TEXT,
        headquarters_address TEXT,
        phone_number INTEGER,
        email TEXT)""")
      # ----------- tabla de ciclistas --------------------#
      self.set_data("""CREATE TABLE IF NOT EXISTS cyclists (
        regitration_number INTEGER PRIMARY KEY AUTOINCREMENT, 
        indetification_number INTEGER, 
        name TEXT, 
        last_name TEXT, 
        birth_date TEXT, 
        country TEXT,
        team_number INTEGER, 
        photo TEXT,
        ranking_UCI INTEGER)""")
      # ----------- tabla de etapas --------------------#
      self.set_data("""CREATE TABLE IF NOT EXISTS lamps (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        lamp_number INTEGER, 
        cyclist_number INTEGER, 
        position INTEGER, 
        time TEXT,
        team_number INTEGER,
        retired INTEGER)""")

      
    except Exception as e:
      print('DB no connected!', e)

  # operaciones de selección
  def get_data(self, query):
    try:
      cursor = self.con.cursor()
      cursor.execute(query)
      data = cursor.fetchall()
      return data
    except Exception as e:
      raise e;
    
  # operaciones de inserción, actualización y eliminación
  def set_data(self, query):
    try:
      cursor = self.con.cursor()
      cursor.execute(query)
      self.con.commit()
    except Exception as e:
      print('Error!', e)
      raise e;