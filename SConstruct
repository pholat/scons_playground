#!python
print("Budujemy")
env = Environment()
env['CPPPATH']='#Include'
libpath='#Libraries/Lib/'
Export('libpath')
Export('env')

def print_cmd_line(s, targets, sources, env):
    pass
    """s       is the original command line string
       targets is the list of target nodes
       sources is the list of source nodes
       env     is the environment"""
#   sys.stdout.write(" Making %s ...\n"% (' and '.join([str(x) for x in targets])))
    print(">>><<<"+s+ " ...")
#    a = int()
#    text = "line number: " + str(a) 
#    print(text)
#    for a in sources:
#        print(a.name)

env['PRINT_CMD_LINE_FUNC'] = print_cmd_line

SConscript('mkfile/SConscript')                                                 #export common variables
SConscript('Libraries/Src/SConscript', variant_dir=libpath, duplicate=0 )       #create library
SConscript('Src/SConscript', variant_dir='build', duplicate=0 )
