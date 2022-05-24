class Lap():
  def __init__(self, connection, data):
    self.lap_number = None
    self.ciclyst_number = None
    self.position = None
    self.time_spent = None
    self.team_number = None
    self.withdrew_lap = None
    
  def __str__(self):
    return str([
      self.lap_number,
      self.ciclyst_number,
      self.position,
      self.time_spent,
      self.team_number,
      self.withdrew_lap])
    
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