# python exercises

Pythonの基礎的な処理を学ぶためのリポジトリです。

## Setup

以下のソフトウェアをインストールしておいてください

* [Git](https://git-scm.com/)
* [Python (Miniconda)](https://conda.io/miniconda.html)
  * Pythonは3系を使います。
  * [Python公式](https://www.python.org/downloads/)もありますが、Minicondaでのインストールを推奨します。
* プログラムを開発するための、好きなエディタ。以下がおすすめです。
  * [Visual Studio Code](https://code.visualstudio.com/)
  * [PyCharm](https://www.jetbrains.com/pycharm/)

## How to begin

以下が、Exerciseの手順です。GitもPythonも初めて、という方は[Warming-up](https://github.com/icoxfog417/python_exercises#warming-up)を参照してください。

1. 右上にある「Fork」というボタンから、本リポジトリをFork(=コピー)してください。
2. forkしたリポジトリを、`git clone`によって手元の端末に取ってきます。これで準備は完了です。
3. 各フォルダの中にあるREADMEには、そのエクササイズで達成すべき課題が書かれています。Pointで示されているヒントをもとに、処理を完成させてください。
4. エクササイズで実装したコードは、好きな名前で保存してください(なお、`ex`始まりのファイルは`.gitignore`されています)。
5. 各フォルダには、解答例が配置されています。わからない場合は、そちらを参考にしてください。

## Exercises

* [Let's Execute Python](https://github.com/icoxfog417/python_exercises/tree/master/01_execute_python)
  * Pythonプログラムを実行してみよう
* [Collections](https://github.com/icoxfog417/python_exercises/tree/master/02_collections)
  * Pythonで配列のデータを処理してみよう
* [Find Pattern](https://github.com/icoxfog417/python_exercises/tree/master/03_find_pattern)
  * 文字列の中から特定のパターンを見つけてみよう
* [Class](https://github.com/icoxfog417/python_exercises/tree/master/04_class)
  * Pythonのクラスと単体テストについて知ろう
* [Use Packages](https://github.com/icoxfog417/python_exercises/tree/master/05_use_packages)
  * 便利なライブラリを使って処理を実装してみよう
* [Exception & logging](https://github.com/icoxfog417/python_exercises/tree/master/06_exception_logging)
  * 例外を処理し、記録しよう

## Warming-up

本項はGitもPythonも初めて、という方のためにHow to beginの内容をより詳細に解説します。解説は以下の通りとなります。

1. [Gitを理解する](https://github.com/icoxfog417/python_exercises#git%E3%82%92%E7%90%86%E8%A7%A3%E3%81%99%E3%82%8B)
2. [Pythonのコードを書く](https://github.com/icoxfog417/python_exercises#python%E3%81%AE%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E6%9B%B8%E3%81%8F)
3. [Gitでバージョン管理をする](https://github.com/icoxfog417/python_exercises#git%E3%81%A7%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E7%AE%A1%E7%90%86%E3%82%92%E3%81%99%E3%82%8B)

### Gitを理解する

本節の目標は、Gitというソフトウェアの機能とメリットを理解することです。

Gitはファイルのバージョン管理を行うソフトウェアです。Gitでバージョン管理されているフォルダを「リポジトリ(Repository)」と呼び、リポジトリ配下のフォルダ/ファイルのバージョンを管理することができます。Gitリポジトリを共有するサービスは様々ありますが、その一つが「GitHub」です。

「バージョン管理」を行うメリットは多くあります。例えば、バージョン間の差分を比較したり、あるバージョンに戻したりするなどです。「バージョン」は好きなタイミングで作成することができます。Gitでは、最小のバージョン管理の単位を「コミット(commit)」と呼びます。コミットは、好きなタイミングで作成できます。以下は、[本リポジトリのあるコミットの内容です](https://github.com/icoxfog417/python_exercises/commit/2425c0c41b966fd9f30ec1144a668324b73a185b)。前回のコミットと、今回のコミットとの間の差分を見ることができます。

![diff](https://user-images.githubusercontent.com/544269/51301442-916dd900-1a72-11e9-98f8-6f608e58295e.png)

バージョン管理を行うことで、複数人での作業も行いやすくなります。AさんとBさんが一緒に開発する場合、Aさんの修正とBさんの修正を両方反映したい、というケースが当然考えられます。完全に別々のパートを修正していれば簡単ですが、AさんとBさんが同じファイルを修正していた場合、互いの修正が反映されるよう注意深く作業する必要があります。Gitを使えば、この「注意深い作業」はGitが行ってくれます。異なるバージョンの修正を取り込むことを、「マージ(merge)」と呼びます。以下は、私が送られてきた修正をマージした例です。

![pull request](https://user-images.githubusercontent.com/544269/51302740-97fe4f80-1a76-11e9-9117-4811d4f33770.png)

`icoxfog417 merged 2 commits into icoxfog417:master from JeffpanUK:master`と書いてあります。これは、私のバージョン(`icoxfog417:master`)に、修正を送ってきてくれた`JeffpanUK`さんのバージョン(`JeffpanUK:master`)を取り込んだ(=マージした)ことを意味しています。GitHubでリポジトリを公開していると、このように他の人から修正を送ってもらえることがあります。これはオープンソースのメリットです。

修正を行う際はあるバージョンから分岐してそれぞれの修正を行います。先ほどの例ではAさんの修正、Bさんの修正、上の実際のマージの例では`JeffpanUK`さんの修正、といった形です。このような、あるバージョンから分岐した修正内容をその名の通り「ブランチ(branch)」と呼びます。Gitでは、どのブランチがいつ分岐し、どうマージされてきたのかという歴史を参照することが可能です。

![branch](https://user-images.githubusercontent.com/544269/51303246-232c1500-1a78-11e9-9ecc-03b73dc4c387.png)

GitHubでは、ブランチから行われる修正を「プルリクエスト(Pull Request)」と呼びます。

Gitには他にも多くの機能がありますが、基本的な機能は以上となります。学んだことを振り返ってみましょう。

* Gitは、バージョン管理を行うためのツールである。
  * Gitでバージョン管理されているフォルダを「リポジトリ(Repository)」と呼ぶ。
  * GitHubは、リポジトリ共有サービスの一つである。
* バージョンの最小単位を「コミット(commit)」と呼ぶ。コミットは、好きなタイミングで作成することができる。
  * コミットを作成しておくと、コミット間の差異を確認できる。
* あるバージョンから分岐した修正のまとまり(コミットのまとまり)を「ブランチ(branch)」と呼ぶ。
  * ブランチを分岐元に統合することを「マージ(merge)」と呼ぶ。
  * GitHub上ではブランチから行われる修正を「プルリクエスト(Pull Request)」と呼ぶ。

以上が、Gitの解説となります。本節の最後に、実際にGitHubで公開されているリポジトリを手元にダウンロードしてみましょう。

最初に、Gitの設定を行っておきます。これは、変更したのが誰なのかを明らかにするための設定です。名前とメールアドレスを登録しておきましょう。

```
git config --global user.name "git taro" 
git config --global user.email git.taro@example.com
```

まず、本リポジトリをコピーしてあなた専用のリポジトリを作成します。これは、GitHub上では"Fork"というボタンを押すことで実行できます。

![fork button](https://user-images.githubusercontent.com/544269/51303835-e4975a00-1a79-11e9-9632-7efde8140a6a.png)


次に、コピーしたリポジトリをダウンロードします。これは、`git clone`というコマンドで行うことが可能です。`git clone`で指定するURLは、コピーしたリポジトリの以下のボタンから確認できます。

![clone](https://user-images.githubusercontent.com/544269/51303908-1a3c4300-1a7a-11e9-980a-d4fbe6769d24.png)

実行が完了すれば、`python_exercises`というフォルダが作成されており、その中にダウンロードされたソースコードが格納されているはずです。このフォルダはGitによるバージョン管理の対象となっているため、コミットを行うことでバージョンを作成することが可能です。

次節では実際にPythonのコードを書いてみて、コミットにより書いたコードを含む「バージョン」を作成してみます。

### Pythonのコードを書く

本節の目標は、実際にPythonのコードを書くことです。

実際に書くPythonのコードの解説については、[Exercise 1](https://github.com/icoxfog417/python_exercises/tree/master/01_execute_python)の解説を参照してください。実装したコードを、`my_answer_ex01.py`として保存してみましょう。

Pythonの書き方についての気になる点がある場合は、以下資料を参考にしてください。

* [Python チュートリアル](http://docs.python.jp/3/tutorial/index.html)
* [Pythonを書き始める前に見るべきTips](http://qiita.com/icoxfog417/items/e8f97a6acad07903b5b0)


### Gitでバージョン管理をする

本節の目標は、実装した内容をコミットでバージョン管理することです。

Pythonのコードを書いたファイルを作成したら、以下のコマンドを実行してみてください。

`git status`

すると、作成したファイルが表示されると思います。`git status`は、バージョン管理の対象で、変更が行われたファイルを表示してくれます。なお、バージョン管理したくないファイルは`.gitignore`で指定することができます。本リポジトリでは、`ex`で始まるPythonのファイルはバージョン管理をしないようにしています。

では、実際コミットをしてみましょう。コミットの前に、コミットの対象とする変更(=バージョンに含める変更)を指定できます。つまり、複数の変更を行っていても「この変更はこのバージョン(コミット)に含める」「これは含めない」といった切り分けができるということです。以下のコマンドを実行してみましょう。

`git add -A`

`-A`のオプションは、全ての変更をコミット対象とすることを意味します。ファイルを指定したい場合は、`git add`の後に対象のファイルを指定します。`add`によりコミット対象とされたものは「staged (cached)」されたファイルと呼ばれます。`add`したファイルでバージョンを作成する(=コミットを行う)には以下のコマンドを実行します。なお、コマンド中の`commit message`は、このバージョンで行った変更の内容を簡単に記載します。

`git commit -m "commit message"`

コミットメッセージの書き方については、[こちら](https://qiita.com/kawasima/items/feac49a299213e2c8ba6)が参考になります。これでコミットが作成できました！ただ、この変更はあなたの手元でだけ行われており、GitHub上には反映されていません。これを反映するには、`push`を行います。

`git push origin master`

`origin`はGitHub上のリポジトリを表し、`master`はブランチを表しています。`push`は送る操作ですが、送られた変更をローカルにダウンロードしたい場合は`pull`を実行します。他のPCで作業した内容を`push`し、別のPCで作業する際に`pull`する、というのはよく行う処理です。

`git pull origin master`

変更が`push`されているか、ぜひGitHub上で確認してみてください。変更の取り消しなど、より詳細な内容は以下の資料をご参考ください。

* [Git チュートリアル](https://www.atlassian.com/ja/git/tutorial/git-basics)
* [使い始める Git](http://qiita.com/icoxfog417/items/617094c6f9018149f41f)

以上でWarming-upは終了です。この後もExerciseを進めて行ってみてください！
