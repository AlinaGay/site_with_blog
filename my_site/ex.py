from decimal import Decimal
from datetime import datetime


goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

def add(items, title, amount, expiration_date=None):
    if expiration_date is not None:
       expiration_date= datetime.strptime(expiration_date, '%Y-%m-%d').date()
    if items.get(title) == None:
       items[title] = [{'amount': amount, 'expiration_date': expiration_date}]     
    else:
       items[title].append({'amount': amount, 'expiration_date': expiration_date})
    
def add_by_note(items, note):
    note_list = list(note.split(" "))
    if '-' in note_list[-1]:
       expiration_date = note_list[-1]
       amount = Decimal(note_list[-2])
       title = ' '.join(note_list[:-2])
       add(items, title, amount, expiration_date)
    else:
        amount = Decimal(note_list[-1])
        title = ' '.join(note_list[:-1])
        add(items, title, amount)

def find(items, needle):
   needle_list = []
   for title in items.keys():
      if needle in title:
         needle_list.append(title)
   if needle_list == []:
      return 'Нет таких продуктов!'
   else:      
      return f'Вывод: {needle_list}'
     
def amount(items, needle):
   total_amount = 0
   for title, value in items.items():
      if needle.lower() == title.lower():
         count = len(value)
         for i in range(count):
            total_amount += value[i]['amount']
      return f'Вывод: {total_amount}'
   
   return 'Нет таких продуктов!'  

def expire(items, in_advance_days=0):
   today = datetime.today()
   expired_product_list = []
   for title, value in items.items():
      count = len(value)
      for i in range(count):
         value_dict = value[i]
         differnce = value_dict['expiration_date'] - today
         if differnce <= in_advance_days:
            expired_product = tuple(title, value_dict['amount'])
            expired_product_list.append(expired_product)
   if len(expired_product_list) != 0:         
      return f'Вывод: {expired_product_list}'
   else:
      return 'У вас нет просроченных продуктов!'        
            

add_by_note(goods, 'Вода газированная 4 2023-07-15')
add(goods, 'Вода', Decimal('1.6'), '2023-10-28') 
print(find(goods, 'йц'))  
print(amount(goods, 'Пельмени Универсальные'))
print(expire(goods, 2))            