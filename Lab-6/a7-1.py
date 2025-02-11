class Password_manager:
    def __init__(self):
        self._old_passwords = ['abc567', 'hij098', 'lmno56']

    @property
    def get_pwd(self):
        return self._old_passwords[0]
    @get_pwd.setter
    def set_pwd(self, a):
        if a not in self._old_passwords:
            self._old_passwords.insert(0, a)
        else:
            return "Password Already Exists!"
    def is_correct(self, b):
        if b==self._old_passwords[0]:
            return True
        else:
            False

pm = Password_manager()
user=input("Enter Password: ")
if pm.is_correct(user):
    new_pwd = input("Enter new password: ")
    pm.set_pwd = new_pwd
    print(f"Current password changed to: {pm.get_pwd}")
    print(f"Old passwords: {pm._old_passwords}")
else:
    print("Incorrect Password")