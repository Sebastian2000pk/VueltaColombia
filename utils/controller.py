class Controller:
  def __init__(self, connection):
    self.__connection = connection
    self.get_query = ''
    
  @property
  def get_data(self):
    try:
      return self.__connection.get_data(self.get_query)    
    except Exception as e:
      raise e
  
  def set_data(self, query: str, data: tuple):
    try:
      self.__connection.set_data(query.format(*data))
    except Exception as e:
      raise e