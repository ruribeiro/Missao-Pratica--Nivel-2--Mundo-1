def loginUsuario (perfil):
   perfil = perfil.lower()
   if perfil == 'admin':
      print("Bem-vindo, administrador!")
   else:
      print("Bem-vindo, usuário!")

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
loginUsuario('etc')
  
