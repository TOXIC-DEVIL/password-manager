from utils import isAccesskey, save, check, creds
from simple_chalk import yellow, green, red, blue, white
import base64

def main():
  exists = False
  with open('accesskey.txt', 'r') as file:
    exists = file.read() != ''
  if exists == False:
    access_key = input(yellow('[ ? ] Write an access key: ')) 
    with open('accesskey.txt', 'w') as file:
      file.write(base64.b64encode(access_key.encode()).decode())
    print(green('[ + ] Successfully set new access key.'))
  else:
    access_key = input(yellow('[ ? ] Write your access key: '))
    is_ak = isAccesskey(access_key)
    if is_ak == True:
      print(green('[ + ] Verification success.\n'))
    else:
      print(red('[ ! ] Verification failed.'))
      quit()

  while True:
    action = input(yellow('[ ? ] Do you want to write, view or viewall password?: ')).lower()
    if action == 'write' or action == 'view' or action == 'viewall':
      break
    else:
      print(red('Please enter \'write\', \'view\' or \'viewall\''))
  if action == 'write':
    while True:
      account = input(yellow('[ ? ] Enter your username, id or email: '))
      password = input(yellow('[ ? ] Enter the corresponding password: '))
      note = input(yellow('[ ? ] Enter any additional notes (eg: netflix password) : '))
      if account == '' or password == '':
        print(red('Please enter a valid account (username, id or email) and password.'))
      elif check(account, password) == True:
        print(red('Entered account (username, id or email) and password is already exists.'))
      else:
        break
    save(account, password, note)
    print(green('[ + ] Successfully saved account and password.'))
  elif action == 'view':
    while True:
      account = input(yellow('[ ? ] Enter your account (username, id or email) or note: '))
      if account != '':
        break
      else:
        print(red('Please enter a valid account (username, id or email) or note.'))
    print(blue('[ - ] Searching...'))
    try:
      credentials = creds(account)
      print(green('Account : ') + white(credentials['account']) + green('\nPassword : ') + white(credentials['password']) + ('' if credentials['note'] == False else green('\nNote:\n') + white(credentials['note'])))
    except Exception as e:
      print(red('[ ! ] Unable to find account, please recheck your username, id or email.'))
    quit()
  elif action == 'viewall':
    with open('creds.txt', 'r') as file:
      content = file.read()
      allCreds = content.split('\n')
      for creds in allCreds:
        creds = { "account": creds.split('|')[0], "password": creds.split('|')[1], "note": creds.split('|')[2] }
        print(green('Account : ') + white(creds['account']) + green('\nPassword : ') + white(creds['password']) + ('' if creds['note'] == False else green('\nNote:\n') + white(creds['note']) + '\n') + green('\n-------------------------\n'))

if __name__ == '__main__':
  main()
