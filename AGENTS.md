# AI Agent Guidelines (hoi4-modding-skills)

## 目的 / Purpose
- 本ファイルは、本リポジトリ（hoi4-modding-skills）で作業するすべてのAIエージェント（Claude, Gemini, GitHub Copilot, Opencode, Codex等）向けの共通作業指針です。
- このリポジトリは、HOI4のMOD開発向けAIエージェントスキルの配布パッケージです。

## 開始時の必須手順 (Required First Steps)
1. 編集を開始する前に、必ず本ファイルおよび `CLAUDE.md` を読むこと。
2. `git status --short --branch` を実行し、作業ツリーの状態を確認すること。
3. 作業を行う際は、適切なトピックブランチ（例: `feature/add-new-skill`）を作成または切り替えて作業すること。
4. `main` ブランチへ直接プッシュしないこと。

## リポジトリ構成
- `skills/`: 各スキルのソースフォルダ、およびビルド済みの `.skill` パッケージファイル
- `.opencode/`: Opencodeエージェント用構成アセット
- `package_skill.py`: 単一のスキルフォルダを `.skill` (zip) にビルドするスクリプト
- `package_all.py`: すべてのスキルフォルダを一括でビルドするスクリプト
- `README.md`: パッケージの利用方法ドキュメント
- `CLAUDE.md`: Claude Code用の個別ガイダンス
- `CLAUDE_template.md`: HOI4 MOD開発プロジェクト向け `CLAUDE.md` のテンプレート
- `AGENTS_template.md`: HOI4 MOD開発プロジェクト向け `AGENTS.md` のテンプレート

## 開発・パッケージングフロー
- スキル定義（`SKILL.md` や参照用ファイル）を追加または修正した場合は、必ず以下のコマンドを実行してビルド（パッケージング）を行ってください。
  ```bash
  python3 package_all.py
  ```
- スキルのソースは `skills/<スキル名>/` ディレクトリ内に配置し、メタデータ、トリガー条件、指示を `SKILL.md` に定義してください。

## AI-Specific Notes
- **Claude / Cursor / Gemini**: ルートにある `CLAUDE.md` を参照してください。
- **Opencode**: `.opencode/AGENTS.md` を参照してください。
- **GitHub Copilot**: 本ファイル（`AGENTS.md`）に記載されたルールを遵守してください。
