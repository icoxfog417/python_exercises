# 03. Find Pattern

## Exercise

このファイル(`README.md`)を読み込んで、'##'で始まっている見出しを抽出してください。上手くいけば、以下が得られるはずです。

* ## Exercise
* ## Point

## Point

**File Read**

* `open`関数を利用することで、ファイルを開くことができます。ファイルパス関連の処理は、[`os.path`](http://docs.python.jp/3/library/os.path.html)に便利なものがまとまっています。
* ファイルを読み込み終わった後は、`close`を実行しないとファイルへ接続したままになるので、注意してください。
* `with`ブロックを利用することで、このブロックを抜けたときにファイルへの接続を自動的に閉じることができます。
* ファイルを読み込む際、エンコードに気を付けてください。

```python
with open("README.md", "r", encoding="utf-8") as f:
    for line in f:
        print(line)  ## output line
```

**Pattern Matching**

* `re`モジュールを使うことで、[正規表現](https://msdn.microsoft.com/ja-jp/library/cc392020.aspx)を用いてテキスト内の特定のパターンを抽出することができます(単純な場合、`re`を使わずとも文字列の処理だけで十分可能ではあります)。
* 例えば、以下のように文字列の中から数値を抜き出すことができます。

```python
import re
pattern = re.compile("\d+")  # create pattern to find number sequence
pattern.findall("today's max temparature is 15 and min is 10.")
> ['15', '10']
```

* `re`では、`compile`によってパターンを作成することができます。
* `match`、`search`は一致する一か所(`match`は先頭のみチェック)、`findall`は一致する箇所すべてを検出してくれます。詳細は[ドキュメント](http://docs.python.jp/3.5/library/re.html)を参照してください。

