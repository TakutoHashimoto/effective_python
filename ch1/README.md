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