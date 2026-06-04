# CLAUDE.md (hoi4-modding-skills)

このファイルは、本リポジトリ（hoi4-modding-skills）で作業する際のAIエージェント向けガイドラインです。

## リポジトリ概要
このプロジェクトは、Hearts of Iron IV (HOI4) のMOD開発を支援するAIエージェント（Claude Code等）用の汎用スキル（Skills）をまとめた配布用リポジトリです。

## 主要コマンド
すべてのスクリプトはPython3で記述されています。

- **すべてのスキルをパッケージング（.skill化）する:**
  ```bash
  python3 package_all.py
  ```
- **特定のスキルを個別にパッケージングする:**
  ```bash
  python3 package_skill.py skills/<skill-directory-name>
  ```
  *(例: `python3 package_skill.py skills/hoi4-event-helper`)*

## ディレクトリ構造
```
hoi4-modding-skills/
├── skills/                      # 各スキルのソースフォルダとビルドされた.skillファイル
│   ├── <skill-name>/            # スキルのソースフォルダ
│   │   ├── SKILL.md             # スキルのトリガー条件と指示（必須）
│   │   ├── references/          # 参照用のmd/html等（任意）
│   │   └── scripts/             # スキルで利用する補助スクリプト（任意）
│   └── <skill-name>.skill       # package_skill.py によって生成されるZIPアーカイブ
├── package_skill.py             # 単一スキル用パッケージングスクリプト
├── package_all.py               # 全スキル用パッケージングスクリプト
├── README.md                    # 配布用ドキュメント
└── CLAUDE.md                    # 本ガイドライン
```

## スキル作成およびメンテナンスのルール
1. **汎用性の維持:** 特定のMODプロジェクト固有のタグ、ID、世界観設定、カスタムスクリプトを直接埋め込まないでください。
2. **命名規則:** スキルのディレクトリ名および生成される `.skill` ファイルは原則として `hoi4-<機能名>-helper` や `hoi4-<機能名>-creator/searcher` のように `hoi4-` から開始してください。
3. **SKILL.md の整備:** 各スキルフォルダには必ず適切なメタデータ（`name`, `description`）を持つフロントマターが含まれた `SKILL.md` を作成してください。
4. **再パッケージングの実行:** スキル内のファイルを修正または追加した後は、必ず `python3 package_all.py` を実行して `.skill` ファイルを更新してください。
