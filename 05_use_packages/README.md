# 05. Use Packages

## Exercise

WebAPIなどを利用する処理を簡略化してくれる[`requesets`](http://docs.python-requests.org/en/master/)というパッケージを用いて、著名な機械学習ライブラリである[TensorFlow](https://github.com/tensorflow/tensorflow)のリポジトリのIssueを取得してみます。
データを取得するためのAPIとして、[GitHubのAPI](https://developer.github.com/v3/issues/#list-issues-for-a-repository)を利用します。

パッケージのインストールにあたっては、仮想環境を作成してそこにインストールを行ってください。
最終的に、取得したIssueのタイトルの一覧を表示してください。

## Point

**Package Install**

* Pythonでは様々な機能を持つライブラリが[PyPI](https://pypi.python.org/pypi)というパッケージの管理サイトに登録されています。
* [`pip`](https://pip.pypa.io/en/stable/)というパッケージ管理のツールを使うことで(Python3.4以降では標準で入っています)、ここに登録されているパッケージをインストール、またアンインストールすることができます。
* ただ、いろいろなプログラムを作るたびにインストールをしていると、膨大なパッケージがたまっていくことになり、またどのプログラムがどのパッケージに依存しているのかわからなくなります
* そのため、通常はプログラムごとの環境(仮想環境)を作成し、そこにそのプログラムで必要なパッケージをインストールします。
* `virtualenv`、また`conda`はこの仮想環境を作るためのツールになります。詳細は[こちら](http://qiita.com/icoxfog417/items/e8f97a6acad07903b5b0#python%E3%81%A7%E3%81%AE%E9%96%8B%E7%99%BA%E3%81%AE%E6%B5%81%E3%82%8C)を参照してください。
* 多くのプログラムでは、依存しているパッケージは`requirements.txt`に記載してあります。
* PyCharmなどの統合開発環境では、この仮想環境の作成や読み込みをサポートしています。詳細は各開発環境の設定を参照してください。

**Json**

* Jsonは、Web上でデータのやり取りを行うためのフォーマットの一種です。WebAPIにデータを送る、また受け取るとき多くはJsonの形式でやり取りします。
* Pythonでは標準で[`json`](http://docs.python.jp/3/library/json.html)というパッケージがあり、これを利用することでJsonデータを読んだり書いたりすることができます。

