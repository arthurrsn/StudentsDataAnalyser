from os import system
from platform import system as platform_system

def identificar_sistema_operacional() -> str:
    """
    Identifica o sistema operacional do dispositivo.

    Returns:
    str: O nome do sistema operacional.
    """
    sistema = platform_system()
    if sistema == "Windows":
        return "Windows"
    elif sistema == "Darwin":
        return "Mac"
    elif sistema == "Linux":
        return "Linux"
    else:
        return "Sistema não identificado"

sistema_operacional = identificar_sistema_operacional()

def clear() -> None:
    """
    Limpa a tela do terminal, dependendo do sistema operacional.
    """
    if sistema_operacional == 'Windows':
        return system('cls')
    elif sistema_operacional == 'Linux' or sistema_operacional == 'Mac':
        return system('clear')
