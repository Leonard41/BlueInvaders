name_user_1 = input("ingrese su nombre")
name_user_2 = input("ingrese su nombre")

election_1 = input("piedra (pi), papel (pa), tijeras (ti)")
election_2 = input("piedra (pi), papel (pa), tijeras (ti)")

if election_1.lower() == "pi" and election_2.lower() == "pa":
    print("Gano el usuario " + name_user_2)
elif election_1.lower() == "ti" and election_2.lower() == "pi":
    print("Gano el usuario" + name_user_2)
elif election_1.lower() == "pa" and election_2.lower() == "ti":
    print("Gano el usuario" + name_user_2)
elif election_1.lower() == "pa" and election_2.lower() == "pa":
    print("empate")
elif election_1.lower() == "pa" and election_2.lower() == "pi":
    print("Gano el usuario" + name_user_1)
elif election_1.lower() == "pi" and election_2.lower() == "ti":
    print("Gano el usuario" + name_user_1)
elif election_1.lower() == "ti" and election_2.lower() == "pa":
    print("Gano el usuario" + name_user_1)
elif election_1.lower() == "pi" and election_2.lower() == "pi":
    print("Empate")
elif election_1.lower() == "ti" and election_2.lower() == "ti":
    print("Empate")
