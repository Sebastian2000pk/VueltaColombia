class Cyclist():
  def __init__(self, connection, data):
    self.regitration_number = None
    self.indetification_number = None
    self.name = None
    self.last_name = None
    self.birth_date = None
    self.country = None
    self.team_number = None
    self.photo = None
    self.ranking_UCI = None
    
  def __str__(self):
    return str([
      self.regitration_number,
      self.indetification_number,
      self.name,
      self.last_name,
      self.birth_date,
      self.country,
      self.team_number,
      self.photo,
      self.ranking_UCI])
    
  def save(self):
    self.connection.set_data("""INSERT INTO cyclists (
      indetification_number, 
      name, 
      last_name, 
      birth_date, 
      country, 
      team_number,
      phone,
      ranking_UCI) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'""".format(
        self.indetification_number,
        self.name,
        self.last_name,
        self.birth_date,
        self.country,
        self.team_number,
        self.phone,
        self.ranking_UCI
      ))
    
  
  def update_ranking_cyclist(self, position: int) -> None:
    """
    Parameters:
    position: int Posicion el en ranking en el que esta el ciclista
    """
    
    self.connection.set_data("""UPDATE cyclists SET 
      ranking_UCI = '{}' 
      WHERE regitration_number = '{}'""".format(
        position,
        self.regitration_number
      ))