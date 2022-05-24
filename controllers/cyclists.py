from utils.controller import Controller

class Cyclists(Controller):
  def __init__(self, connection):
    super().__init__(connection)
    self.get_query = 'SELECT * FROM cyclists'

  def create(self, data: tuple):
    """
    params
    data: tuple (indetification_number int, name str, last_name str, birth_date str, country str, team_number int, photo str, ranking_UCI int)
    """
    
    query = """INSERT INTO cyclists (
      indetification_number, 
      name, 
      last_name, 
      birth_date, 
      country, 
      team_number,
      photo,
      ranking_UCI) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
    self.set_data(query, data)
    print('Ciclista creado!')
    
  def update_ranking_cyclist(self, registration_number: int, position: int) -> None:
    """
    Parameters
    registration_number: int Número de registro del ciclista
    position: int Posicion el en ranking en el que esta el ciclista
    """
    
    self.set_data("""UPDATE cyclists SET ranking_UCI = '{}' WHERE regitration_number = '{}'""",
      (position, registration_number))
    print('Ranking actualizado!')