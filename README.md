# 背景

  スライドを使ったオンデマンド授業において、スライドを共有せず、動画(例: .mp4)だけを共有する授業がある
  動画の再生時間を調整してスライドを確認するのは面倒だ

# 動機

  動画からスライドを抽出?したい

# 目的
    
  動画の再生時間を調整してスライドを確認する手間を削減する

# 手法

  python の opencv を用いて、動画から一定間隔でフレームを抽出する
  抽出したフレームを pdf ファイルに結合する
  
# 今後の課題

  スライドの重複をなくす

  <!-- 前のフレームと現在のフレームを比較して、差分がなければ、現在のフレームを保存しない -->
0
