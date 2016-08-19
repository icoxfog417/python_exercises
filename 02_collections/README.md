# 02. Collections

## Exercise

名前のリストがあります。これをリストの順番に番号をつけて出力してください。また、あなたの名前は`Angy`なので、Angyの時だけ`My name is Angy`と出力してください。

* 名前のリスト: ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
* 期待する出力
 * 1.Bill is my classmate
 * 2.Anne is my classmate
 * 3.My name is Angy
 * 4.Cony is my classmate
 * 5.Daniel is my classmate
 * 6.Occhan is my classmate

## Point

**Array and Tuple**

* Pythonでは、配列は`[]`で定義します。これ以外に、`()`で定義するタプルというものがあります。
* Tupleは、配列と異なり中身が変えられません。今回与えられているリストは、`()`で宣言されているのでタプルであり、よって中身を変えることはできません。

**Utility around Collections**

* `len`関数を利用することで、配列やタプルの長さを取得することができます。
* `range`関数を使用することで、特定の長さの数値列(`range(3)`なら`[0, 1, 2]`)を作ることできます。
* `enumerate`関数を使用することで、[配列のインデックス, 配列の値]を生成することができます

```python
x = [1, 2, 3]
for i, x in enumerate(x):
    print(i, x)
```

* セミコロンを利用することで、配列の特定の位置から処理を行ったり切り出したりすることができます。

```python
x = [1, 2, 3]
x[1:]
> [2, 3]
```

* また、リスト内で処理を行うこともできます。これをリスト内包表記といいます。

```python
[i * 2 for i in range(3)]
> 0, 2, 4
```

また、標準で搭載されている[`collections`](http://docs.python.jp/3/library/collections.html)や[`itertools`](http://docs.python.jp/3.5/library/itertools.html)は非常に高機能であり、複雑な機能を簡単に書くことができます。
そのため、多少複雑な処理は自分で実装する前にこれらのパッケージに機能がないか探してみることをお勧めします。

**String format**

* `format`関数を使用することで、文字列内に値を埋め込むことができます。

```python
print("Hello {0}".format("Angy"))
> Hello Angy
```
