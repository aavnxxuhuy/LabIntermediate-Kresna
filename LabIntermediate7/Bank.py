class BankAccount:
   #Kode awal yang diberikan
    _lastAssignedNumber = 1000  
    def __init__(self):
        self._balance = 0
        BankAccount._lastAssignedNumber += 1
        self._accountNumber = BankAccount._lastAssignedNumber

   # Kode untuk menampilkan nomor rekening
    def get_account_number(self):
        return self._accountNumber

# Membuat sejumlah akun dan mencetak nomor akun masing-masing
number_of_accounts = 5  
accounts = []

for _ in range(number_of_accounts):
    account = BankAccount()
    accounts.append(account)
    print(f"Account Number: {account.get_account_number()}")

# Verifikasi bahwa setiap akun memiliki nomor yang berbeda
for i in range(len(accounts)):
    print(f"Account {i+1} Number: {accounts[i].get_account_number()}")
