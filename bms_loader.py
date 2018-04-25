
bms_props = {
  
  #PLAYER 1 - 1P single play 1 guage
  #PLAYER 2 - 1P + 2P couple play 2 guage
  #PLAYER 3 - 1P + 2P double play 1 guage
  #PLAYER 4 - 1P vs 2P battle play 2 guage
  'player': {
    'default': '1',
    'validate': lambda x: x in ['1', '2', '3', '4']
  },

  #RANK 0 - judge +/- 8ms
  #RANK 1 - judge +/- 15ms
  #RANK 2 - judge +/- 18ms
  #RANK 3 - judge +/- 21ms
  'rank': {
    'default': '2',
    'validate': lambda x: x in ['0', '1', '2', '3']
  },

  #TOTAL n - 

}

class BMSFile:

  def __init__(self, file_handle):
    self.set_defaults()
  
  def set_defaults(self):