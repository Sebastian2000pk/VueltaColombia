
from utils.controller import Controller

class Classification(Controller):
  def get_lamp(self, lamp):
    self.get_query = """SELECT 
      c.regitration_number, 
      c.name, 
      c.last_name, 
      c.country,
      time(l.time) as time, 
      t.name
    FROM lamps AS l INNER JOIN cyclists AS c ON l.cyclist_number = c.regitration_number
    INNER JOIN teams AS t ON l.team_number = t.team_number
    WHERE lamp_number = {}
    ORDER BY l.time ASC""".format(lamp)
    result_set = self.get_data
    return [{
      'cyclist_number': row[0],
      'name': row[1],
      'last_name': row[2],
      'country': row[3],
      'time': row[4],
      'team_name': row[5]
    } for row in result_set]
    
  @property
  def general(self):
    self.get_query = """
    SELECT 
      c.regitration_number, 
      c.name, 
      c.last_name, 
      c.country, 
      time(sum(strftime('%s', l.time) - strftime('%s', '00:00:00')), 'unixepoch') AS time, 
      t.name
    FROM lamps AS l INNER JOIN cyclists AS c ON l.cyclist_number = c.regitration_number
    INNER JOIN teams AS t ON l.team_number = t.team_number
    GROUP BY l.cyclist_number
    ORDER BY time ASC
    """
    result_set = self.get_data
    return [{
      'cyclist_number': row[0],
      'name': row[1],
      'last_name': row[2],
      'country': row[3],
      'time': row[4],
      'team_name': row[5]
    } for row in result_set]
    
  def lamp_team(self, team_number: int, lamp: int):
    self.get_query = """
    SELECT 
      l.team_number, 
      t.name, 
      t.country,
      time(sum(strftime('%s', l.time) - strftime('%s', '00:00:00')), 'unixepoch') AS time
    FROM lamps AS l INNER JOIN teams AS t ON l.team_number = t.team_number
    WHERE l.team_number = {} AND lamp_number = {}
    GROUP BY l.team_number
    ORDER BY time ASC
    LIMIT 3
    """.format(team_number, lamp)
    result_set = self.get_data
    return [{
      'team_number': row[0],
      'team_name': row[1],
      'country': row[2],
      'time': row[3],
    } for row in result_set]
    
  def general_team(self, team_number: int):
    self.get_query = """
    SELECT 
      l.team_number, 
      t.name, 
      t.country,
      time(sum(strftime('%s', l.time) - strftime('%s', '00:00:00')), 'unixepoch') AS time
    FROM lamps AS l INNER JOIN teams AS t ON l.team_number = t.team_number
    WHERE l.team_number = {}
    GROUP BY l.team_number
    ORDER BY time ASC
    LIMIT 3
    """.format(team_number)
    result_set = self.get_data
    return [{
      'team_number': row[0],
      'team_name': row[1],
      'country': row[2],
      'time': row[3],
    } for row in result_set]