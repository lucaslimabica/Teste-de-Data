# Tema 6 - a82451 - Lucas Bica

class AnoInvalido(Exception):
    """Exceção levantada para anos inválidos."""

    def __init__(self, ano):
        super().__init__(f"Ano inválido: {ano}. Não existe ano 0.")


class MesInvalido(Exception):
    """Exceção levantada para meses inválidos."""

    def __init__(self, mes):
        super().__init__(f"Mês inválido: {mes}. O mês deve estar entre 1 e 12.")


class DiaInvalido(Exception):
    """Exceção levantada para dias inválidos."""

    def __init__(self, dia, mes):
        super().__init__(f"Dia inválido: {dia}, para o mês {mes}.")


class Data:
    """
    Classe que implementa o armazenamento e validação de uma data.

    Se for instanciada com valores inválidos, levanta uma exceção específica.
    """

    def __init__(self, ano, mes, dia):
        self.validar_data(ano, mes, dia)
        self.ano, self.mes, self.dia = ano, mes, dia

    def __str__(self):
        return f"{self.ano}/{self.mes:02d}/{self.dia:02d}"

    @staticmethod
    def validar_data(ano, mes, dia):
        """
        Valida se a data é possível. Levanta exceções específicas para casos inválidos.

        :param ano: int - Ano da data.
        :param mes: int - Mês da data.
        :param dia: int - Dia da data.

        :raises AnoInvalido: Se o ano é inválido (ex: ano 0).
        :raises MesInvalido: Se o mês é inválido (menor que 1 ou maior que 12).
        :raises DiaInvalido: Se o dia é inválido para o mês/ano fornecido.
        """
        if ano < 1:
            raise AnoInvalido(ano)

        if mes <= 0 or mes >= 13:
            raise MesInvalido(mes)

        if 1 > dia > 31:
            raise DiaInvalido(dia, mes)

        if not Data.is_bissexto(ano):
            if dia > 28:
                raise DiaInvalido(dia, mes)
        elif Data.is_bissexto(ano):
            if dia > 29:
                raise DiaInvalido(dia, mes)

        if mes in [4, 7, 9, 11]:
            if dia >= 31:
                raise DiaInvalido(dia, mes)

    @staticmethod
    def is_bissexto(ano):
        """
        Verifica se um ano é bissexto.

        :param ano: int - Ano a ser verificado.
        :return: bool - True se o ano for bissexto; False caso contrário.
        """
        return ano % 400 == 0 or ((ano % 4 == 0) and (ano % 100 != 0))
