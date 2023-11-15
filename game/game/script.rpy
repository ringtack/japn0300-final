﻿# このファイルにはゲームのスクリプトを記述します。


# Ren'Py のスクリプトは、インデント（行頭の空白）によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター（台詞を表示するオブジェクト）を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。

init:
  # shaking
  transform shaking:
      linear 0.1 xoffset -2 yoffset 2
      linear 0.1 xoffset 3 yoffset -3
      linear 0.1 xoffset 2 yoffset -2
      linear 0.1 xoffset -3 yoffset 3
      linear 0.1 xoffset 0 yoffset 0
      repeat

define mc = Character(u'私')


# label ステートメント（文）はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。

# ゲームは start ラベルからスタートします。

label start:

    # INTRODUCTION

    scene home room
    with fade
    pause 0.5

    show telephone at shaking
    pause 0.5

    "「リング、リング。。。」"

    "私の電車が聞こえます。「もしもし、（友達の名前）です。今のパーチー、もう何か作った。六時に始まるよ。」"

    hide telephone

    show mc tired at center

    with dissolve

    "。。。"

    mc "ああ、忘れちゃった。。。"


    # These display lines of dialogue.

    mc "今日は（他の友達）の誕生日だから、食べ物を作って、パーティーに何か持って行こうと思っている。"

    mc "材料を買った方がいいよ。。。"

    hide mc tired with None
    show mc happy at center

    mc "じゃ、料理しよう！"

    return




    # 背景を表示します。デフォルトではプレースホルダー（仮画像）を使用しますが、
    # images ディレクトリーにファイル（ファイル名は "bg room.png" や "bg room.jpg"）
    # を追加することで表示できます。

    # scene bg room

    # スプライト（立ち絵）を表示します。ここではプレースホルダーを使用していますが、
    # images ディレクトリーに "eileen happy.png" などと命名したファイルを追加すると
    # 表示することができます。

    # at ステートメントは画像の表示する位置を調整します。
    # at center は中央に下揃えで表示します。これは省略しても同じ結果になります。
    # その他に at right、at left などがデフォルトで定義されています。

    # show eileen happy at center

    # トランジション（画面遷移効果）を使って表示を画面に反映させます。
    # 台詞を表示するか with None を使うと、トランジション無しで直ちに表示します。

    # with dissolve

    # 音楽を再生します。
    # game ディレクトリーに "music.ogg" などのファイルを追加すると再生できます。

    # play music "music.ogg"

    # 以下は台詞を表示します。

    # e "Ren'Py の新しいゲームを作成しました。"

    # e "ストーリー、画像、音楽を追加すれば、世界にリリースすることができます！"

    # return でゲームを終了します。

    # return
