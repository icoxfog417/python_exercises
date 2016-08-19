# 04. Class

## Exercise

名前を覚える対話ボットのクラスを作成します。今回は、エクササイズの開始にあたり下記のコードをコピーしてファイルを作成してください。
そして、`WRITE YOUR CODE HERE`となっているところに、コードを記載してください。

```python
# -*- coding: utf-8 -*-
import unittest


class Bot():

    def __init__(self, owner_name):
        """
        WRITE YOUR CODE HERE
        """

    def reply(self, call):
        """
        WRITE YOUR CODE HERE
        """


class TestBot(unittest.TestCase):

    def test_bot_reply(self):
        bot = Bot("Angy")
        self.assertEqual("Hello", bot.reply("Hi, I'm Bill.'"))
        self.assertEqual("Hello my Boss!", bot.reply("Hi, I'm Angy."))


if __name__ == "__main__":
    unittest.main()

```

このコードの中には、テストのためのコードがついています。最終的に`python`コマンドで実行してテストが通ればOKです。

## Point

**Class**

* Pythonでは、クラスは`class`宣言により作成を行います。
* `class`の中では、関数の第一引数は常に`self`、自分自身になります。この`self`を通じて、自分の持つ関数を呼び出すことができます。
* `__init__`は、クラスの初期化を行うための特別な関数になります。

クラスを作成することのメリットは、内部状態が持てるということです。このほか、関数をまとめる目的で使用されることもあります。

**Unit Test**

* Pythonでは、`unittest.TestCase`を継承することで簡単にテストを作成することができます。`unittest.TestCase`には、様々なテスト用メソッドが登録されており継承によりそれを活用することができます。
* テストは`unittest.main()`で実行します。詳細は[ドキュメント](http://docs.python.jp/3/library/unittest.html)を参照してください。


