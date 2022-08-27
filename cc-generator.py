import random
from randomtimestamp import randomtimestamp
from datetime import datetime


class CC():
  '''Individual card info and methods.
  '''


  CCDATA = {
    'amex': {
      'len_num': 15,
      'len_cvv': 4,
      'pre': [34, 37],
      'remaining': 13
    },
    'discover': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [6001],
      'remaining': 12
    },
    'mc': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [51, 55],
      'remaining': 14
    },
    'visa13': {
      'len_num': 13,
      'len_cvv': 3,
      'pre': [4],
      'remaining': 12
    },
    'visa16': {
      'len_num': 16,
      'len_cvv': 3,
      'pre': [4],
      'remaining': 15
    },    
  }

  def __init__(self):
    self.cc_type = None
    self.cc_len = None
    self.cc_num = None
    self.cc_cvv = None
    self.cc_exp = None
    self.cc_prefill = []

  def generate_cc_exp(self):
    '''Generates a card expiration date that is 
    between 1 and 3 years from today. Sets `cc_exp`.
    '''
    self.cc_exp = randomtimestamp(
        start_year = datetime.now().year + 1,
        text = True,
        end_year = datetime.now().year + 3,
        start = None,
        end = None,
        pattern = "%m-%Y")
    
  def generate_cc_cvv(self):
    '''Generates a type-specific CVV number.
    Sets `cc_cvv`. 
    '''
    this = []
    length = self.CCDATA[self.cc_type]['len_cvv']

    for x_ in range(length):
      this.append(random.randint(0, 9))

    self.cc_cvv = ''.join(map(str,this))

  def generate_cc_prefill(self):
    '''Generates the card's starting numbers
    and sets `cc_prefill`.
    '''
    this = self.CCDATA[self.cc_type]['pre']
    self.cc_prefill = random.choices(this)

  def generate_cc_num(self):
    '''Uses Luhn algorithm to generate a theoretically 
    valid credit card number. Sets `cc_num`. 
    ''' 
    remaining = self.CCDATA[self.cc_type]['remaining']
    working = self.cc_prefill + [random.randint(1,9) for x in range(remaining - 1)] 

    check_offset = (len(working) + 1) % 2
    check_sum = 0

    for i, n in enumerate(working):
      if (i + check_offset) % 2 == 0:
        n_ = n*2
        check_sum += n_ -9 if n_ > 9 else n_
      else:
        check_sum += n

    temp = working + [10 - (check_sum % 10)]
    self.cc_num = "".join(map(str,temp)) 

  def return_new_card(self):
    '''Returns a dictionary of card details.
    '''
    return {'cc_type': self.cc_type,
            'cc_num': self.cc_num, 
            'cc_cvv': self.cc_cvv,
            'cc_exp': self.cc_exp}

  def print_new_card(self):
    '''Prints a single card to console.
    '''
    hr = '--------------------------------'

    print(f'%s' % hr)
    print(f'Type: %s' % self.cc_type)
    print(f'Number: %s' % self.cc_num)
    print(f'CVV: %s' % self.cc_cvv)
    print(f'Exp: %s' % self.cc_exp)


class CCNumGen(): 
  '''Generates theoretically valid credit card numbers
  with CVV and expiration date. Prints a list of dictionaries. 
  '''
  hr = '--------------------------------'

  card_types = ['amex','discover','mc','visa13','visa16']

  def __init__(self, type='visa16', number=1):

    self.type = type
    self.num = number
    self.card_list = []

    if self.type not in self.card_types:
      print('Card type not recognized. Task ended.')
      return
    if not isinstance(self.num, int):
      print('Number of cards must be a whole number. Task ended.')
      return

    print(self.hr)
    print(f'Generating %s %s cards...' % (self.num, self.type))

    for x_ in range(0, self.num):
      new = CC()
      new.cc_type = self.type
      new.generate_cc_exp()
      new.generate_cc_cvv()
      new.generate_cc_prefill()
      new.generate_cc_num()
      self.card_list.append(new.return_new_card())
      new.print_new_card()

    print(self.hr)
    print('Task complete.')
    print(self.hr)

  def print_card_list(self):
    '''Prints the list of cards to console.
    '''
    for d in self.card_list:
      print('------------------------------')
      for k in d:
        print(f'%s: %s' % (k, d[k]))


amex = CCNumGen('amex', 2)
discover = CCNumGen('discover', 2)
mc = CCNumGen('mc', 2)
visa13 = CCNumGen('visa13', 2)
visa16 = CCNumGen('visa16', 2)
