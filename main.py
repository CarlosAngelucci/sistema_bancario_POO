from abc import ABC, abstractproperty
from datetime import datetime

class Conta:
  def __init__(self,numero, cliente):
    self._saldo = saldo
    self._numero = numero
    self._agencia = agencia
    self._cliente = cliente
    self._historico = Historico()

  @classmethod
  def nova_conta(cls, cliente, numero):
    return cls(numero, cliente)

  @property
  def saldo(self):
    return self._saldo

  @property
  def numero(self):
    return self._numero

  @property
  def agencia(self):
    return self._agencia

  @property
  def cliente(self):
    return self._cliente

  @property
  def historico(self):
    return self._historico
  
  def saldo(self):
    return self._saldo

  def sacar(self, valor):
    if self._saldo >= valor:
      self._saldo -= valor
      self._historico.append(f"Saque de {valor}")
      print("\n ===== Saque realizado com sucesso! ===== \n"")
      return True
    else:
      print("\n @@@ Operação falhou! Você não tem saldo suficiente. @@@")

  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      self._historico.append(f"Depósito de {valor}")
      print("\n ===== Depósito realizado com sucesso! ===== \n")
    else:
      print("\n @@@ Operação falhou! O valor informado é inválido. @@@")
      
  def nova_conta(self, cliente, numero):
    pass

class ContaCorrente(Conta):
  def __init__(self, numero, cliente, limite=500, limite_saques=3):
    super().__init__(numero, cliente)
    self._limite = limite
    self._limite_saques = limite_saques

  def sacar(self, valor):
    numero_saques = len(
      [transacao for transacao in self._historico if transacao[tipo] == Saque.__name__]
    )

    excedeu_limte =  valor > self.limite
    excedeu_saques = numero_saques >= self._limite_saques

    if excedeu_limite:
      print("\n@@@ Operação falhou! O valor excede o limite da conta. @@@")
    elif excedeu_saques:
      print("\n@@@ Operação falhou! O número de saques excede o limite. @@@")

    else:
      return.super().sacar(valor)

    return False

  def __str__(self):
    return f"""
            Agência: \t {self.agencia}
            C/C: \t {self.numero}
            Titutlar: \t {self.cliente.nome}
            """

class Historico:
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes

  def adicionar_transacao(self, transacao):
    self._transacao.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"")
      }
    )

class Transacao(ABC):
  @property
  @abstractproperty
  def valor(self):
    pass

  @property
  @abstractproperty
  def registrat(self):
    pass

class Depositar(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor

  def registrar(self, conta):
    sucesso_transacao = conta.depositar(self.valor)

    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)
      
class Sacar(Transacao):
  def __init__(self, valor):
    self._valor = valor
  
  @property
  def valor(self):
    return self._valor

  def sucesso_transacao(self, conta):
    sucesso_transacao = conta.sacar(self.valor)

    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)
      
class Cliente:
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []

  def realizar_transacao(self, conta, transacao):
    transacao.registrar(conta)

  def registrar_conta(self, conta):
    self.contas.append(conta)

class PessoaFisica(Cliente):
  def __ini__(self, cpf, nome, data_nascimento, endereco):
    self.cpf = cpf
    self.nome = nome
    self.data_nascimento = data_nascimento
    super.__init__(endereco)
