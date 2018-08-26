'''
See the article

https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

Essential is the use of * symbol, (or **).
The reason: Whenever you use a variable number of arguments. *args

          whenever you use a variable number of keywords arguments , **kwargs
'''



def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print( "another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')


def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs:
            print ("%s == %s" %(key,value))

kwargs = {'name' :"yasoob"}
greet_me(name ="yasoob")