import base64

def bestmatch(query, list):
  matches = [element for element in list if query.lower() in element.lower()]
  return matches[0] if matches else False

def isAccesskey(key):
  with open('accesskey.txt', 'r') as file:
    accesskey = base64.b64decode(file.read()).decode('utf-8')
  return accesskey == key

def save(account, password, note=False):
  with open('creds.txt', 'a') as file:
    file.write(account + '|' + base64.b64encode(password.encode()).decode() + '|' + note + '\n')
  return True

def check(account, password):
  accounts = []
  passwords = []
  with open('creds.txt', 'r') as file:
    content = file.read().strip()
    allCreds = content.split('\n')
    for creds in allCreds:
      accounts.append(creds.split('|')[0])
      passwords.append(
        base64.b64decode(creds.split('|')[1]).decode('utf-8')
      )
  return account in accounts and password in passwords

def creds(account_or_note):
  accounts = []
  passwords = []
  notes = []
  with open('creds.txt', 'r') as file:
    content = file.read().strip()
    allCreds = content.split('\n')
    for creds in allCreds:
      accounts.append(creds.split('|')[0])
      passwords.append(creds.split('|')[1])
      notes.append(creds.split('|')[2])
  if account_or_note != '':
    result_acc = bestmatch(account_or_note, accounts)
    result_note = bestmatch(account_or_note, notes)
    if result_acc != False:
      return { "account": accounts[accounts.index(result_acc)], "password": base64.b64decode(passwords[accounts.index(result_acc)]).decode('utf-8'), "note": notes[accounts.index(result_acc)] }
    elif result_note != False:
      return { "account": accounts[notes.index(result_note)], "password": base64.b64decode(passwords[accounts.index(result_note)]).decode('utf-8'), "note": notes[notes.index(result_note)] }
    else:
      return False
