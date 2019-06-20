#***********************************************************************************************
#                          BOILER PLATE PARA CLASSES NO PYTHON
#***********************************************************************************************
'''
Função: Classe modelo

Propriedades:
    prop1: propriedade 1
    _prop2: propriedade 2

Métodos:
    multi():    Executa uma multiplicação de prop1 e prop2
    soma(num1): Executa a soma de prop1 com num1
    (...)

Exemplo de instanciamento de objeto
import Classe
obj = Classe.MinhaClasse(1,2)
<obj> = Classe.MinhaClasse(<argumento1>,<argumento2>)
'''
#*********************************** NOME DA CLASSE *******************************************
class MinhaClasse(object):        #Nome da classe(classe Pai)

#********************************* VARIÁVEIS DE CLASSE ****************************************
    '''
    Alterando o valor de uma variável de classe pelo objeto MinhaClasse, nota-se que
    reflete em todos os objetos.
    Classe.MinhaClasse.set_variavel_classe(1)
    '''

    var_classe = 5

#************************************* CONSTRUCTOR *********************************************
    '''
    O método __init__ é executado toda vez que se cria uma nova instância da classe.
    No momento da criação de um novo objeto, nesse caso, as propriedades
    são inicializadas com os valores de arg1 e arg2. 
    A palavra self está se referindo ao próprio objeto criado.
    '''

    def __init__(self, arg1, arg2):
        self.prop1 = arg1
        self._prop2 = arg2       #Variável começando com underline é interna da classe

# ************************************** DESTRUCTOR *********************************************
    '''
    Metodo chamado quando o objeto é destruído
    Destruição dos objetos:
    del(<nome do objeto>)  
    Ex: del(obj1)              
    '''

    def __del__(self):
        pass

#************************************* MÉTODOS DA CLASSE ****************************************
    '''
    Sintaxe para nomear métodos
    get_<nome do método>    Para "pegar" informações
    set_<nome do método>    Para alterar propriedades
    '''

    def get_multi(self):                #Todos os métodos declarados é obrigatório o uso da palavra reservada self.
        return (self.prop1*self._prop2)

    def get_soma(self, num1):
        self.resultado = self.prop1+num1+self.var_classe
        return (self.resultado)

    def set_propriedade_1(self, arg):
        self._prop2 = arg

    def _dif(self):                     #Método interno, declarado com underline na frente
        pass

    @classmethod                        #Método usado para alterar variáveis de classe
    def set_variavel_classe(cls, arg):
        cls.var_classe = arg

#*********************************** OUTRAS OBSERVAÇÕES *****************************************
'''
Função isinstance, retorna se o valor pertence ao tipo do segundo parâmetro
Exemplo:
>>> isinstance(1, int)
>>> True

Como a classe está dentro de um módulo, para acessar a classe não esquecer de
indicar o módulo que a contém, exemplo:
>>> Classe.MinhaClasse.set_variavel_classe(1)

A palavra reservada self indica que se refere a características do próprio objeto
(cada objeto terá as suas). A palavra reservada cls indica uma característica da
classe, que infuenciará todos os objetos.
'''
