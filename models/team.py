class Team():
  def __init__(self, connection, data):
    self.connection = connection
    self.team_number = data[0]
    self.name = data[1]
    self.country = data[2]
    self.name_director = data[3]
    self.bike_brand = data[4]
    self.bike_computer_brand = data[5]
    self.headquarters_address = data[6]
    self.phone_number = data[7]
    self.email = data[8]
    
  def __str__(self):
      return str([
        self.team_number,
        self.name,
        self.country,
        self.name_director,
        self.bike_brand,
        self.bike_computer_brand,
        self.headquarters_address,
        self.phone_number,
        self.email])
  
  def save(self):
    self.connection.set_data("""INSERT INTO teams (
      name, 
      country, 
      name_director, 
      bike_brand, 
      bike_computer_brand, 
      headquarters_address, 
      phone_number, 
      email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
        self.name,
        self.country,
        self.name_director,
        self.bike_brand,
        self.bike_computer_brand,
        self.headquarters_address,
        self.phone_number,
        self.email
      ))
  
  # actualizar direcion de la sede
  def update_headquarters_address(self, new_address):
    self.connection.set_data("""UPDATE teams SET 
      headquarters_address = '{}' 
      WHERE team_number = '{}'""".format(
        new_address,
        self.team_number
      ))
  