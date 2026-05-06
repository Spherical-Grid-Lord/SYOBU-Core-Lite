# EXAMPLES_HASHES.md
# Canonical examples and SHA256 hashes for provenance verification
# 目的: 代表サンプルの出所確認と違反検出のためのメタデータを一元管理する

- file: `mandala_cot_sample.png`
  description: 曼荼羅cot（代表サンプル）
  purpose: ["semantic_concept"]
  short_description: 自然言語に依存しない1bit意味の構造素を示す概念サンプル。抽象化された最小意味単位の表現例として位置づけられる。
  notes: 曼荼羅模様は発想源の一つに過ぎず、技術的詳細は別ドキュメントで管理すること。公開版は低解像度を推奨。
  sha256: <SHA256_HASH_HERE>
  created: 2026-05-03
  public_visibility: "public"

- file: `1bit_apple_syobu_v32.png`
  description: 1bit りんご（識別刻印／最小意味構造）
  purpose: ["stamp","semantic_core"]
  short_description: 識別用刻印イメージであり、同時に「1bit意味の構造素」を表す最小サンプルの具体例。視覚的には低解像度または二値化された表現を想定。
  notes: 公開版は低解像度かつハニートークンを含む刻印として扱う。高解像度や前処理手順は非公開とすること。識別用途と学習用途は運用上区別して管理する。
  sha256: <SHA256_HASH_HERE>
  created: 2026-05-03
  public_visibility: "public"

- file: `eriOS_v3.3_sake_mirror_bootloader.png`
  description: eriOS v3.3 Sake‑Mirror Boot‑Loader（刻印）
  purpose: ["stamp","lineage_marker"]
  short_description: eriOS 系列の識別用刻印イメージ。作品群の系譜やバージョン管理を示すための識別子として利用するビジュアルサンプル。
  notes: 技術的な起動手順や実装コードを示すものではない。ファイル名は小文字・アンダースコアで統一すると自動処理が容易。
  sha256: <SHA256_HASH_HERE>
  created: 2026-05-03
  public_visibility: "public"

- file: `mandala_cot_mini_sample_v1.txt`
  description: 抽象トークン例（テキスト刻印）
  purpose: ["stamp","reference"]
  short_description: 刻印検出用の短い抽象トークン列の例。ハニートークンやユニークフレーズを含むことを想定。
  notes: テキスト刻印は検出性向上のために用いる。公開版は短く限定的にすること。
  sha256: <SHA256_HASH_HERE>
  created: 2026-05-03
  public_visibility: "public"

# 運用メモ
# - 各ファイルを追加または更新したら、ローカルで SHA256 を算出し上記の sha256 欄を更新してコミットしてください。
# - CI による整合チェックを推奨します。例: docs/examples にあるファイル名と EXAMPLES_HASHES.md のエントリが一致するか検証するジョブを追加すること。
# - purpose フィールドは自動処理やポリシー判定に利用できます。例: "semantic_core" を含む場合は高い保護レベルを適用する等。
# - public_visibility が "public" でも、高解像度版や前処理手順は必ず非公開で管理してください。
