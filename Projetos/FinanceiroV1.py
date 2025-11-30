import os
from datetime import datetime


class Transacao:
    def __init__(self, valor, tipo, categoria, data):
        self.valor = valor
        self.tipo = tipo.lower()
        self.categoria = categoria.lower()
        self.data = data
        

class Conta:
    def __init__(self):
        self.movimentacoes = []

    def calcular_saldo(self):
        total_saldo = 0.0
        poupanca = self.adicionar_poupanca()
        for m in self.movimentacoes:
            if m.tipo == "entrada":
                total_saldo += m.valor
            elif m.tipo == "saida":
                total_saldo -= m.valor
        saldo = total_saldo - poupanca
        return saldo, poupanca

    def adicionar_poupanca(self):
        total_poupanca = 0.0
        for m in self.movimentacoes:
            if m.categoria == "salario":
                total_poupanca += m.valor * 0.05
        return total_poupanca

    def adicionar_transacao(self, trans):
        self.movimentacoes.append(trans)
        return self.calcular_saldo()

    def listar_transacao(self):
        print(f"A conta possui {len(self.movimentacoes)} movimentos.\n")
        
        for m in self.movimentacoes:
             print( 
                 f'Data: {m.data.strftime("%d/%m/%Y")} |'
                 f'Tipo: {m.tipo.capitalize()}:\n'
                 f'Categoria: {m.categoria.capitalize()} |' 
                 f'Valor: R${m.valor:,.2f}' 
             ) 
        
        saldo, poupanca = self.cal_saldo() 
        print(f"\nSaldo atual: R${saldo:,.2f}") 
        print(f"Saldo Poupança: R${poupanca:,.2f}\n")


    def tipo_transacao(self):
        qtd_entrada = 0
        qtd_saida = 0
        for m in self.movimentacoes:
            if m.tipo == "saida":
                qtd_saida += 1
            elif m.tipo == "entrada":
                qtd_entrada += 1

    def saude_financeira(self):
        qtd_saida = 0
        valor_saida = 0.0

        if len(self.movimentacoes) == 0:
            return 0, 0.0
        else:    
            for m in self.movimentacoes:
                if m.tipo == "saida":
                    qtd_saida += 1
                    valor_saida += m.valor

            percentual_saida = (qtd_saida / len(self.movimentacoes)) * 100
            return percentual_saida, valor_saida

    def menu_conta(self):
        os.system("cls")

        return input(
            "Selecione a ação desejada:\n\n[1]Cadastrar \n[2]Listar \n[3]Saldo \n[4]Verificar Saude \n[5]Saldo Poupanca \n[6]Sair\n"
        )


    def menu_inicial(self):
        return int(
            input(
                "\n\n[1] Voltar menu \n[2] Sair\n"
            )
        )



con = Conta()

while True:

    opcao = con.menu_conta()

    if opcao == '1':
        os.system("cls")

        while True:
            try:
                valor = float(input("Digite o valor da movimento: "))
                break
            except:
                print("Valor em formato incorreto!\n Favor verificar.")
                continue

        while True:
            tipo = input(
                "Digite o tipo do movimento:\n\n[1] Entrada \n[2] Saida\n "
            )
            if tipo == "1":
                tipo = "entrada"
                break
            elif tipo == "2":
                tipo = "saida"
                break
            else:
                print("Opção invalida!")

        categoria = input("Digite o categoria do movimento: ")

        while True:
            data_str = input("Digite o data da movimento: ")
            try:
                data = datetime.strptime(data_str, "%d/%m/%Y")
                break
            except:
                print("Data em formato incorreto!\n Favor verificar.")
                continue

        trans = Transacao(valor, tipo, categoria, data)
        con.adicionar_transacao(trans)

    elif opcao == '2':

        os.system("cls")
        con.listar_transacao()
        con.menu_inicial()

    elif opcao == '3':
        os.system("cls")
        
        saldo, poupanca = con.calcular_saldo()
        print(f"Saldo disponivel: {saldo:.2f}\n")
        print(f"Saldo poupanca: {poupanca:.2f}")

        con.menu_inicial()

    elif opcao == '4':

        os.system("cls")
        percentual_saida, valor_saida = con.saude_financeira()
        if percentual_saida < 30:
            print("Sua saúde financeira está BOA!")
        elif percentual_saida <= 60:
            print("Sua saúde financeira está REGULAR!")
        else:
            print(
                f"Sua saúde financeira está em RISCO! Você teve R${valor_saida:.2f} em saídas ({percentual_saida:.2f}%)."
            )
        con.menu_inicial()

    elif opcao == '5':

        os.system("cls")
        poupanca = con.adicionar_poupanca()
        print(f"Saldo Poupança: {poupanca:.2f}")
        con.menu_inicial()

    elif opcao == '6':
        os.system("cls")
        print("Encerrando programa...")
        break

    else:
        print("Opção invalida! Tente novamente.")
