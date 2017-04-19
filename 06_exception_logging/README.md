# 06. Exception and Logging

## Exercise

例外の処理と、そのロギングの手法を学びます。  
ロギング用の関数は用意しているので、例外を処理してその内容を出力してみてください。

```python
from logging import getLogger, StreamHandler, DEBUG


def create_logger(name, log_level):
    """create logger"""
    logger = getLogger(name if name else __file__)
    handler = StreamHandler()
    handler.setLevel(log_level)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger


def main():
    """show how to handle and log the exception"""

    logger = create_logger("my_logger", DEBUG)
    logger.info("Now try to open file that does not exist!")

    #WRITE YOUR CODE HERE: below script will cause the Exception!
        with open("not_exist_file.txt") as f:
            lines = f.readlines()

    #WRITE YOUR CODE HERE: handle the exception

if __name__ == "__main__":
    main()

```

## Point

**[Exception](https://docs.python.jp/3/tutorial/errors.html)**

* Pythonでは、`try` ~ `except`により、例外の検出とハンドリングを行います。
* なお、例外を発生させる場合は`raise`を使用します。
* `Exception`クラスを継承することで、カスタムの例外クラスを作成することができます。

**[logging](https://docs.python.jp/3/library/logging.html)**

* Pythonにはデフォルトでログ用のパッケージが用意されていますが、これをそのまま利用するのは好ましくありません。
* `logging`はイメージとしてはグローバルインスタンスのような存在で、エラーレベルの設定などを変えるとそれを使用している全依存ライブラリにも影響します。
* そのため、`getLogger`により個別のロギング用インスタンスを作成することが好ましいです。
* なお、`import logging`を行うとうっかりグローバルな`logging`を使ってしまいそうになるので、素のimportは控えた方が賢明です。この点については、[こちらの記事](http://qiita.com/amedama/items/b856b2f30c2f38665701)に詳しく記載されています。
