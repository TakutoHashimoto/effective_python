# Pythonic 思考
## 1. 使用するPythonのバージョンを知っておく
* 自分が使用するPythonのバージョンを知るには `--version` を使う。

    ```
    % python --version
    Python 3.9.6
    ```

* Python3を使っている場合は `python3 --version` でも同じ結果が得られる。

* Python実行時には組み込みモジュール `sys` の値を調べることで、使用中のPythonのバージョンを確認できる。

    ```python
    import sys

    print(sys.version_info)
    # => sys.version_info(major=3, minor=9, micro=6, releaselevel='final', serial=0)

    print(sys.version)
    # 3.9.6 (default, Mar 20 2023, 23:57:59) 
    # [Clang 14.0.0 (clang-1400.0.29.202)]
    ```


## 2. PEP8スタイルガイドに従う
* Python拡張提案（Enhancement Proposal）#8は、Pythonのコードをどのようにフォーマットするかのスタイルガイド。


## 3. bytesとstrの違いを知っておく
* **※※あまり理解できていない※※**
* 文字列データを表すのに `bytes` と `str` の2種類がある。`bytes` のインスタンスは生の符号なし8ビット値からなり、ASCIIエンコーディングで表示される。
    ```python
    a = b"h\x65llo"
    print(list(a))  # => [104, 101, 108, 108, 111]
    print(a)  # => b'hello'
    ```

* `str` のインスタンスはテキスト文字を表すUnicodeコードポイントを含む。
    ```python
    a = "a\u0300 propos"
    print(list(a))  # => ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
    print(a)  # => à propos
    ```

* **`str` インスタンスはバイナリエンコーディングを持たず、`bytes` インスタンスはテキストエンコーディングを持たない。**

* Unicodeデータをバイナリデータに変換するには、`str` の `encode` メソッドを呼び出さなければならない。逆にバイナリデータをUnicodeデータに変換するには、`bytes` の `decode` メソッドを呼び出す必要がある。


## 4. Cスタイルフォーマット文字列とstr.formatは使わずf文字列で埋め込む
* Pythonには、言語と標準ライブラリに組み込まれた4種類の異なるフォーマット方式がある。


## 5. 複雑な式の代わりにヘルパー関数を書く
### Summary
* Pythonの構文は、ただ複雑なだけで読みにくい1行の式が簡単に書けてしまう。
* 複雑な式（特に同じロジックを繰り返す必要がある場合）は、ヘルパー関数にする。
* `if/else` 条件式は、`or` や `and` のような論理演算子を使用するよりも読みやすい代替手段を提供する。


## 6. インデックスではなく複数代入アンパックを使う
### Summary
* Pythonには1つの代入分で複数の値を代入できるアンパック代入がある。
* アンパックはPythonでは一般的であり、イテラブル内のレベルにあるイテラブルを含めてどのようなイテラブルにも使える。
* アンパックを使えば、シーケンスにインデックスを使わずに済むので、コードが明確になり見た目がスッキリする。


## 7. `range` ではなく `enumerate` を使う
### Summary
* `enumerate` の簡潔な構文で、イテレータでループしながら、要素のインデックスを取り出すことができる。
* `range` でループして、シーケンスのインデックスを処理するよりも、`enumerate` を使う方がよい。
* `enumerate` の第2引数で、カウンタを開始する数（デフォルトは0）を指定できる。

`range` は組み込み関数で、整数集合上でループする繰り返し処理に役立つ（ [1_7_1.py](https://github.com/TakutoHashimoto/effective_python/blob/main/src/1_7_1.py) ）。
文字列のリストのようなデータ構造では、シーケンスを直接ループできる（ [1_7_2.py](https://github.com/TakutoHashimoto/effective_python/blob/main/src/1_7_2.py) ）。

リストの処理で、リストの要素のインデックスが必要なことがよくある。例えば、好きなフレーバーのアイスクリームのランキングを出力したいとする。次の2通り考えられる。
1. `range` を使う（ [1_7_3.py](https://github.com/TakutoHashimoto/effective_python/blob/main/src/1_7_3.py) ）
   * リストの長さが必要で、配列のようにインデックスを扱う必要がある。ステップが多くて読むのが面倒。
2. `enumerate` を使う（ [1_7_4.py](https://github.com/TakutoHashimoto/effective_python/blob/main/src/1_7_4.py) ）
   * 遅延評価ジェネレータでイテレータをラップする。
   * ループのインデックスとイテレータの次の値の対を `yield` する。
   * カウントを開始する数を指定することができる。デフォルトは0



## 8. イテレータを並列に処理するには `zip` を使う
### Summary
* 組み込み関数 `zip` は、複数のイテレータを並列に処理するのに使う。
* `zip` はタプルを生成する遅延評価ジェネレータなので、無限に長い入力にも使える。
* 異なる長さのイテレータを与えると、`zip` は何のエラーも出さずに出力を最短で停止する。
* 複数のイテレータの長さが異なるときに、最短で停止することなく `zip` するには、組み込みモジュール `itertools` の `zip_longest` 関数を使う。


## 9. `for` ループと `while` ループの後の `else` ブロックは使わない
### Summary
* Pythonには、`for` や `while` のループブロックの直後に `else` ブロックを許す特別な構文がある。
* ループの直後の `else` ブロックは、ループ本体で `break` 文が実行されなかった場合にのみ実行される。
* ループの直後の `else` ブロックは、振る舞いが直感的でなく、誤解を生みやすいので使用しない。


## 10. 代入式で繰り返しを防ぐ
### Summary
* 代入文は、warlus演算子 `:=` を使って変数名への値代入と評価を1つの式で行い、繰り返しをなくす。
* 代入式がより大きな式の一部なら、カッコでくくる必要がある。
* Pythonには `switch/case` 文や `do/while` ループはないものの、それらの機能は代入式を用いて明確に書ける。