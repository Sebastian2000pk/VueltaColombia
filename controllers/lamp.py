from utils.controller import Controller

class Lamps(Controller):
  def __init__(self, connection):
    super().__init__(connection)
    
  def get_data(self, lamp):
    self.get_query = 'SELECT * FROM lamps WHERE lamp_number = {}'.format(lamp)
    result_set = super().get_data
    return [{
      'id': row[0],
      'lamp_number': row[1],
      'cyclist_number': row[2],
      'position': row[3],
      'time': row[4],
      'team_number': row[5],
      'retired': row[6]
    } for row in result_set]

  def create(self, data: tuple):
    """
    params
    data: tuple (lamp_number int, cyclist_number int, position int, time str, team_number int, retired int)
    """
    
    query = """INSERT INTO lamps (
      lamp_number, 
      cyclist_number, 
      position, 
      time,
      team_number,
      retired) VALUES ('{}', '{}', '{}', '{}', '{}',  '{}')"""
    self.set_data(query, data)
    print('Etapa registrada!')
    
  def update(self, id: int, cyclist_number: int, position: int, time: str, team_number: int, retired: int):
    query = """UPDATE lamps SET cyclist_number = '{}', position='{}', time='{}', team_number='{}', retired='{}' WHERE id='{}'"""
    print(query)
    self.set_data(query, (cyclist_number, position, time, team_number, retired, id))
    print('Registro de etapa actualizado!')