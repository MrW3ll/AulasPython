# %%
class Transacao:
    def __init__(self,valor,tipo,categoria,data):
        self.valor = valor
        self.tipo = tipo.lower()
        self.categoria = categoria
        self.data = data

class Conta:
    def __init__(self):
        self.nome = ''
        self.movimentacoes = []

    def cal_saldo(self):
        total_saldo = 0.0
        for m in self.movimentacoes:
            if m.tipo == 'entrada':
                total_saldo += m.valor
            elif m.tipo == 'saida':
                total_saldo -= m.valor
        return total_saldo

    def add_transacao(self,trans):
        self.movimentacoes.append(trans)
        return self.cal_saldo()

    def listar_transacao(self):
        print(f'A conta possui {len(self.movimentacoes)} movimentos.')
        for m in self.movimentacoes:
            print(f'[{m.tipo}]: {m.categoria} R${m.valor}|{m.data}')
        print(f'Saldo dísponivel R${self.cal_saldo()}')    

    def tipo_transacao(self):
        qtd_entrada = 0
        qtd_saida = 0
        
        for m in self.movimentacoes:
            if m.tipo == 'saida':
                qtd_saida += 1
            elif m.tipo == 'entrada':    
                qtd_entrada += 1



    def aproveitando(self):
        qtd_saida = 0
        valor_saida = 0.0

        for m in self.movimentacoes:
            if m.tipo == 'saida':
                qtd_saida += 1
                valor =+ m.valor
                
        return (qtd_saida/len(self.movimentacoes)) * 100, valor_saida        



# %%
from datetime import datetime
con = Conta()

while True:

    opcao = int(input('Selecione a ação desejada:\n 1.Cadastrar \n2.Listar \n3.Calcular saldo \n4.Sair \n'))

    if opcao == 1:
       
       while True:
                
            try:
                valor = float(input('Digite o valor da movimento: '))
                break
            except:
                print('Valor em formato incorreto!\n Favor verificar.')
                continue

       while True:
            tipo = input('Digite o tipo do movimento:\n [1] Entrada \n[2]Saida ')
            if tipo == '1':
                 tipo = 'entrada'
                 break
            elif tipo == '2':
                tipo = 'saida'
                break
            else:
                print('Opção invalida!')

       categoria = input('Digite o categoria do movimento: ')


       while True:
            data_str = input('Digite o data da movimento: ')
            try:
                data = datetime.strptime(data_str,'%d/%m/%Y')
                break
            except:
                print('Data em formato incorreto!\n Favor verificar.')
                continue  
            
       
       trans = Transacao(valor,tipo,categoria,data)
       con.add_transacao(trans)


    elif opcao == 2:
       con.listar_transacao()

    elif opcao == 3:
        saldo = con.cal_saldo()
        print(f'Saldo: {saldo}')


    elif opcao == 4:
        print('Encerrando programa...')
        break





# %%
