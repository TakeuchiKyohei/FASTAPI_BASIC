# 型ヒントの練習

from typing import List, Dict

price: int = 100
tax: float = 1.1

def calc_price(price: int, tax: float) -> int:
    return int(price * tax)

if __name__ == "__main__":
    print(f'{calc_price(price=price, tax=tax)}円')

sample_list: List[int] = [1,2,3,4]
sample_dict: Dict[str, int] = {"a": 1, "b": 2}