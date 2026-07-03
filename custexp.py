def agval():
    ag=int(input("Enter a age:="))
    try:
        assert ag >= 18, "Age must be 18 or above"
        print(ag)
        '''if(ag<18):
            raise ValueError ("Age should be 18 or greater")
        else:
            print("Welcome to voting")'''
    except Exception as e:
        print(e)

agval()

