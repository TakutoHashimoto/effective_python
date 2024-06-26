# Pythonic 思考
## 1. 使用するPythonのバージョンを知っておく
### Summary
* 最新バージョンのPythonは3。しっかりサポートされているこのバージョンをプロジェクトに使うべきだ。
* システムのコマンドラインで実行するPythonが、期待している最新バージョンであることを確認する。
* 2020年1月でサポートがなくなったので、Python2は避ける。

---

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
### Summary
* Pythonのコードを書くときには常にPEP8スタイルガイドに従う。
* より大きなコミュニティの共通スタイルを共有することで、他の人との協働作業が捗る。
* 一貫したスタイルを用いることで、自分のコードを後で修正しやすくなる。

---

Python拡張提案（Enhancement Proposal）#8は、Pythonのコードをどのようにフォーマットするかのスタイルガイド。

#### 空白
* インデントには、タブではなく空白を使う。
* 構文上意味を持つレベルのインデントには、4個の空白を使う。
* 各行は、長さが79文字かそれ以下とする。
* 長い式を続けるために次の行を使うときは、通常のインデントから4個の追加空白を使ってインデントする。
* ファイルでは、関数とクラスでは、空白2行で分ける。
* クラスでは、メソッドは、空白行で分ける。
* 辞書では、キーとコロンの間には空白を置かず、同じ行に値を書く場合には値の前に空白を1つ置く。
* 変数代入前の前後には、空白を1つ、必ず1つだけ置く。
* 型ヒント（型アノテーション）では、変数名の直後にコロンを置き、型情報の前に空白を1つ置く。

#### 名前付け
* 関数、変数、属性は、`lowercase_underscore` のように小文字でアンダースコアを挟む。
* プロテクテッド（保護）属性は、`_leading_underscore` のようにアンダースコアを先頭に付ける。
* プライベート属性は、`__double_underscore` のようにアンダースコアを2つ先頭に付ける。
* クラスと例外は、`CapitalizedWord` のように先頭を大文字にする。
* モジュールでの定数は、`ALL_CAPS` のようにすべて大文字でアンダースコアを挟む。
* クラスのインスタンスメソッドは、（オブジェクトを参照する）第1パラメータの名前に `self` を使う。
* クラスメソッドは、（クラスを参照する）第1パラメータの名前に `cls` を使う。

#### 式と文
* 式の否定（`if not a is b`）ではなく、内側の項の否定（`if a is not b`）を使う。
* コンテナやシーケンスの長さ（`if len(somelist) == 0`）を使って、空値（`[]` や `''` など）かどうかをチェックしない。`if not somelist` を使って、空値が暗黙的に `False` と評価されることを使う。
* 上と同じことを、非空値（`[1]` や `hi` など）にも使う。非空値について、文 `if somelist` は暗黙的に `True` と評価される。
* `if` 文、`for` ループ、`while` ループ、`except` 複合文を1行で書かない。明確になるよう複数行にする。
* 式が1行に収まらない場合は、カッコで括って、複数行にして、読みやすいようにインデントする。
* `\` で行分けするよりは、カッコを使って複数の式を囲む方が良い。

#### インポート
* `import` 文は（`from x import y` も含めて）常にファイルの先頭に置く。
* インポートするときは、常にモジュールの絶対名を使い、現モジュールのパスからの相対名を使わない。例えば、モジュール `foo` をパッケージ `bar` からインポートするときには、`import foo` ではなく `from foo import bar` を使う。
* 相対インポートを使わなければならないときは、明示的な構文 `from . import foo` を使う。
* インポートは次の順番で行う。それぞれの部分では、アルファベット順にインポートする。
  * 標準ライブラリモジュール
  * サードパーティモジュール
  * 自分の作成したモジュール


## 3. bytesとstrの違いを知っておく
**※※あまり理解できていない※※**

### Summary
* `bytes` は8ビット値の列を含み、`str` はUnicodeコードポイントの文字列を含む。
* ヘルパー関数を使って、操作する入力が（8ビット値、UTF-8符号化文字、Unicodeコードポイントなど）期待している文字列型になっていることを確かめる。
* `bytes` と `str` は、`>`, `==`, `+`, `%` などのような演算子では一緒に使えない。
* ファイルにバイナリデータを読み書きするには、常に（`'rb'` または `'wb'` のような）バイナルモードでオープンする。
* ファイルにUnicodeデータを読み書きするには、システムのデフォルトのテキスト符号化に注意する必要がある。問題が生じないように、`open` では `encoding` パラメータを明示的に指定する。

---

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
### Summary
* `%` 演算子を使うCスタイルフォーマット文字列では、予想しない動作や読みにくさの問題に悩まされる。
* `str.format` メソッドは、フォーマット指定子のミニ言語に有用な概念を導入しているが、その他ではCスタイルフォーマット文字列の間違いを繰り返しているので避けるべきだ。
* `f` 文字列では、Cスタイルフォーマット文字列の大きな問題を解く新しい構文で、文字列中のフォーマット変数を扱う。
* `f` 文字列では、フォーマット指定子にどんなPython式も書けるので、簡潔かつ強力だ。

---

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