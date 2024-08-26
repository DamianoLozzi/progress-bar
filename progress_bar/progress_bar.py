from tqdm import tqdm
from tqdm.asyncio import tqdm as atqdm
from colorama import Fore,Style 

def get_default_format(bar_color):
    return f"{{l_bar}}{Style.RESET_ALL}{bar_color}{{bar}}{Style.RESET_ALL}| {{n_fmt}}/{{total_fmt}} {bar_color}[{Style.RESET_ALL}{Fore.YELLOW}{{elapsed}}{bar_color}<{Style.RESET_ALL}{Fore.YELLOW}{{remaining}}{bar_color},{Fore.YELLOW}{{rate_fmt}} {{postfix}}{Style.RESET_ALL}{bar_color}]{Style.RESET_ALL}"

def get_progress_bar(iterable, desc="Processing", total=None, mininterval=0.1, disable=False,bar_color=None, bar_format=None, ascii=None):
    ascii=ascii if ascii else "░█"
    bar_color=bar_color if bar_color else Fore.GREEN
    desc=bar_color+desc+Style.RESET_ALL
    bar_format=bar_format if bar_format else get_default_format(bar_color)
    return tqdm(iterable, desc=desc, total=total, mininterval=mininterval, disable=disable, bar_format=bar_format, ascii=ascii)

def get_async_progress_bar(iterable, desc="Processing", total=None, mininterval=0.1, disable=False,bar_color=None, bar_format=None, ascii=None,leave=False):
    ascii=ascii if ascii else "=█"
    bar_color=bar_color if bar_color else Fore.BLUE
    desc=bar_color+desc+Style.RESET_ALL
    bar_format=bar_format if bar_format else get_default_format(bar_color)
    return atqdm(iterable, desc=desc, total=total, mininterval=mininterval, disable=disable, bar_format=bar_format, ascii=ascii,leave=leave)
