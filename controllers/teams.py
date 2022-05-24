from utils.controller import Controller

class Teams(Controller):
  def __init__(self, connection):
    super().__init__(connection)
    self.get_query = 'SELECT * FROM teams'

  def create(self, data: tuple):
    """
    params
    data: tuple (name str, country str, name_director str, bike_brand str, bike_computer_brand str, headquarters_address str, phone_number int, email str)
    """
    
    query = """INSERT INTO teams (
      name, 
      country, 
      name_director, 
      bike_brand, 
      bike_computer_brand, 
      headquarters_address, 
      phone_number, 
      email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"""
    self.set_data(query, data)
    print('Equipo creado!')
    # result = [{
    #   'team_number': row[0],
    #   'name': row[1],
    #   'country': row[2],
    #   'name_director': row[3],
    #   'bike_brand': row[4],
    #   'bike_computer_brand': row[5],
    #   'headquarters_address': row[6], 
    #   'phone_number': row[7],
    #   'email': row[8]
    # } for row in result_set]
    # return result
    
  def update_headquarters_address(self, team_number: int, headquarters_address: str):
    query = """UPDATE teams SET headquarters_address = '{}' WHERE team_number = '{}'"""
    self.set_data(query, (headquarters_address, team_number))
    print('Sede actualizada!')