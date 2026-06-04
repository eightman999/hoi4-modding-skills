# CLAUDE.md (HOI4 Modding 汎用テンプレート)

このファイルは、AIエージェント（Claude Code等）がこのリポジトリ（Hearts of Iron IV MODプロジェクト）で作業する際の共通ガイドラインです。新しいMODプロジェクトを始める際、あるいは既存のプロジェクトにClaudeを導入する際に、このファイルを `CLAUDE.md` にリネームしてプロジェクトのルートディレクトリに配置してください。

*(注意: `<...>` で囲まれた部分は、ご自身のMODプロジェクトに合わせて適宜書き換えてください)*

## MOD概要

* **MOD名:** <MODの名前> (例: HOI4 Alternative History Mod)
* **対応HOI4バージョン:** <1.13.* など、対応するバージョン>
* **主なシステム:**
  * <カスタムシステムの簡単な説明>
  * <カスタムシステムの簡単な説明>

---

## ディレクトリ構造 (標準的なHOI4 MOD構造)

```
<your_mod_directory>/
├── common/
│   ├── national_focus/       # 国家方針（National Focus）定義ファイル
│   ├── ideas/                # 国民精神（Ideas）や法律などの定義
│   ├── decisions/            # ディシジョン定義ファイル
│   ├── characters/           # 歴史的登場人物・将軍・顧問等の定義
│   ├── scripted_effects/     # スクリプト効果（共通処理の切り出し）
│   ├── scripted_triggers/    # スクリプトトリガー（共通条件の切り出し）
│   └── scripted_guis/        # カスタムUI（Scripted GUI）のロジック
├── events/                   # イベント定義ファイル
├── history/
│   ├── countries/            # 各国の初期設定（与党、法律、技術、初期変数の定義）
│   ├── states/               # ステートの初期設定（インフラ、人口、所属国）
│   └── units/                # 初期陸海空軍の編成（OOB）
├── interface/                # UI定義ファイル（.gui）および .gfx 設定ファイル
├── localisation/             # 翻訳YAMLファイル（japanese, english 等）
│   ├── japanese/             # 日本語ローカライズファイル
│   └── english/              # 英語ローカライズファイル
├── gfx/                      # 画像アセット（スプライト、国旗、顔写真、アイコン等）
└── <doc_directory>/          # 各自のデザインノートや資料
```

---

## 命名規則

| コンテキスト | 推奨パターン | 例 |
|---|---|---|
| 国別ファイル | `<TAG>_<name>.txt` | `GER_fascism_rebellion.txt` |
| システム共通ファイル | `_<system_name>.txt` | `_economic_spheres.txt` |
| 変数 / フラグ | `snake_case` (システム接頭辞付きを推奨) | `ea_member_state_flag` |
| GFX定義名 | `GFX_[category]_[name]` | `GFX_idea_economic_growth` |
| ローカライズキー | `[system]_[key]` | `ea_sphere_title` |

---

## HOI4 スクリプティングにおける重要ルール

1. **システムタグ `_` のアポストロフィ囲み:**
   TAGとして特殊タグ `_` を使用する場合は、変数と誤認されるのを防ぐため、必ずシングルクォーテーションで囲んでください。
   * 例: スコープ `'_' = { ... }`、トリガー `tag = '_'`、`NOT = { tag = '_' }`。
2. **存在判定:**
   `country_exists` コマンドは存在しません。国の存在判定には必ず `exists = yes/no` を使用してください。
3. **GUI制限:**
   `parent_window_token` 構文は非推奨です。カスタムGUIを作成する際は使用を避けてください。
4. **ローカライズファイルのエンコーディング:**
   ローカライズ用 `.yml` ファイルは、HOI4ゲームエンジンが正常に読み込めるように、**必ず「UTF-8 with BOM (BOM付き UTF-8)」**で保存してください。

---

## パフォーマンスと最適化のガイドライン

AIエージェントがコードを実装・最適化する際は、以下の原則を厳守してください。

1. **トリガーの早期リターン (Early Return):**
   負荷の高い条件判定を行う前に、軽量な条件判定（`has_country_flag`、`tag = GER` 等）をトリガーブロックの先頭に配置してください。
2. **`hourly`（毎時処理）の最小化:**
   毎時実行されるイベントやオンアクション（`on_actions`）はゲームの動作を著しく重くします。可能な限り `daily`（毎日処理）や特定のトリガー条件に置き換えてください。
3. **`any_state` などの広範な検索の回避:**
   頻繁に実行されるコード内で `any_state` や `any_country` などのグローバル検索スコープを使用するのは避けてください。
4. **フラグによるキャッシュ:**
   ステートの変更や変数の計算結果を country_flag や state_flag でキャッシュし、毎 tick の再計算を防いでください。

---

## デバッグとログの確認方法

* **HOI4 ログの出力場所:**
  * **macOS:** `~/Documents/Paradox Interactive/Hearts of Iron IV/logs/`
  * **Windows:** `C:\Users\<Username>\Documents\Paradox Interactive\Hearts of Iron IV\logs/`
* **デバッグ実行:**
  起動オプションに `-debug` 引数を付与して起動すると、ゲーム内コンソールでの詳細情報表示やリアルタイムエラー確認が可能になります。
