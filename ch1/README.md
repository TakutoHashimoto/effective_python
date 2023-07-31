# Pythonic 思考
## 使用するPythonのバージョンを知っておく
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

## PEP8スタイルガイドに従う
* Python拡張提案（Enhancement Proposal）#8は、Pythonのコードをどのようにフォーマットするかのスタイルガイド。