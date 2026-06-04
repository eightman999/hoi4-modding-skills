# Hearts of Iron IV Modding AI Agent Skills

このパッケージは、Hearts of Iron IV (HOI4) のMOD開発を支援するために設計された、AIエージェント（Claude Code 等）向けの汎用スキル集です。
特定のMODプロジェクト（SSW等）に依存せず、すべてのHOI4 MOD開発で汎用的に利用できるスキルがまとめられています。

## 収録スキル一覧 (全21種)

| スキル名 | 説明 |
| :--- | :--- |
| `hoi4-decisions-helper` | ディシジョンの作成と管理の対話的支援 |
| `hoi4-decisions-searcher` | 既存のディシジョンの検索・参照 |
| `hoi4-event-helper` | イベント（country_event, news_event等）の対話的作成とローカライズ作成 |
| `hoi4-event-searcher` | 既存のイベント定義の検索・参照 |
| `hoi4-focus-searcher` | 国家方針（National Focus）の検索 |
| `hoi4-gfx-searcher` | GFX定義や画像アセットパスの検索 |
| `hoi4-gui` | Scripted GUIおよびインターフェース（.gui）ファイルの作成・最適化支援 |
| `hoi4-idea-creator` | 国民精神（Ideas）の構造化定義と作成 |
| `hoi4-image-asset-creator` | 画像アセット（TGA/DDS等）の生成、調整、適用支援 |
| `hoi4-modifier-maker` | 補正（Modifiers/Dynamic Modifiers）ブロックの対話的作成 |
| `hoi4-modifier-searcher` | 利用可能な補正の検索・参照 |
| `hoi4-nf-creator` | 国家方針（National Focus）ツリーおよび個別フォーカスの作成 |
| `hoi4-on-actions-helper` | `on_actions` 定義とイベントトリガーの構成支援 |
| `hoi4-opinion-modifiers-helper` | 外交関係・評価補正（Opinion Modifiers）の作成・管理 |
| `hoi4-scripted-effect-maker` | スクリプト効果（Scripted Effects）の定義・作成 |
| `hoi4-scripted-effect-searcher` | 既存のスクリプト効果の検索 |
| `hoi4-scripted-localisation-helper` | スクリプト化されたローカライズの作成・統合 |
| `hoi4-scripted-triggers-helper` | スクリプトトリガー（Scripted Triggers）の定義・作成 |
| `hoi4-techtree-creator` | 技術ツリー（Tech Tree）の構成と定義の作成 |
| `hoi4-unit-design-creator` | 師団・艦船設計（Unit/Ship Design）の作成支援 |
| `hoi4-variable-helper` | 変数（Variables）や配列（Arrays）操作のロジック構築支援 |

## 使用方法

### AIエージェントへの導入方法

本スキル群は、AIエージェント（例：Claude Code等）に読み込ませて使用します。

1. **`.skill` ファイルを配置する場合**
   - 各スキルの `.skill` ファイルは、ZIP圧縮されたアーカイブ形式です。
   - 使用するプロジェクト（MOD開発ディレクトリ）の直下に `.claude/skills/` ディレクトリを作成し、そこに使用したいスキルの `.skill` ファイル（例：`hoi4-event-helper.skill`）をコピーしてください。

2. **ディレクトリとして配置する場合**
   - `.skill` ファイルを展開したディレクトリ（または `skills/` 配下にある各スキルフォルダ）を直接 `.claude/skills/` 以下に配置しても動作します。

### スキルのパッケージング方法

スキル内容を編集し、再度 `.skill` ファイル（zipアーカイブ）を生成する場合は、付属のスクリプトを使用します。

- **特定のスキルをパッケージングする場合:**
  ```bash
  python3 package_skill.py skills/<スキルフォルダ名>
  ```
  （例：`python3 package_skill.py skills/hoi4-modifier-maker` を実行すると、`skills/hoi4-modifier-maker.skill` が生成されます）

- **すべてのスキルを一括パッケージングする場合:**
  ```bash
  python3 package_all.py
  ```

---
本パッケージは配布用にまとめられたものです。MOD作成時のAIエージェントの作業精度向上にご活用ください。
