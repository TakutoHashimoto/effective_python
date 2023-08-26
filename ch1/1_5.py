"""
URLのクエリ文字列を複合する例
"""

from urllib.parse import parse_qs


my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)
print(repr(my_values))
# => {'red': ['5'], 'blue': ['0'], 'green': ['']}

print(f"Red: {my_values.get('red')}")
print(f"Green: {my_values.get('green')}")
print(f"Opacity: {my_values.get('opacity')}")  # opacity: 不透明度
"""
=>
Red: ['5']
Green: ['']
Opacity: None
引数が空白、もしくは定義されていないものの場合はデフォルト値を0とする方が良さそう
論理式で行うように書いてみる
"""

red = my_values.get("red", [""])[0] or 0
green = my_values.get("green", [""])[0] or 0
opacity = my_values.get("opacity", [""])[0] or 0
print(f"Red: {red!r}")  # !rをつけると値がクォーテーションで囲まれる
print(f"Green: {green!r}")
print(f"Opacity: {opacity!r}")
"""
=>
Red: '5'
Green: 0
Opacity: 0
"""