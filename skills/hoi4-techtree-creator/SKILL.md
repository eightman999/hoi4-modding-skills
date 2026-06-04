---
name: hoi4-techtree-creator
description: >
  HOI4 mod用の国家固有テクノロジーツリーを完全なフォルダ構造（tech.txt + GUI + GFX + localisation）で新規作成するスキル。
  使用タイミング: (1) 「[TAG]用テックツリーを作って」「新しい技術ツリーを追加したい」「[country]固有のテクノロジーフォルダを作成」などのリクエスト時。
  (2) 縦型（年が上から下）または横型（年が左から右）レイアウトの選択を含む。
  (3) countrytechtreeview.guiへの追記が必要な場合。SSW_mod/BSM_mod両対応。
---

# HOI4 テクノロジーツリー新規作成スキル

## 作成する全ファイル一覧

| ファイル | 内容 | 操作 |
|---|---|---|
| `common/technologies/[TAG]_[cat].txt` | テック定義 | 新規作成 |
| `interface/countrytechtreeview.gui` | フォルダ表示・タブ・アイテム定義 | **追記** |
| `interface/replace/[gfx].gfx` または新規 .gfx | スプライト定義 | 追記/新規 |
| `gfx/interface/technologies/[cat]/[TAG]/` | テックアイコン画像フォルダ | 新規作成 |
| `localisation/japanese/` + `localisation/english/` | テック名・説明 | 追記 |

---

## Step 0: 参照フォルダの確認（必須）

作業前に必ずユーザーへ確認する:

> **「参照する既存フォルダはどれですか？（例: engnavalfolder, naval_folder, mtgnavalfolder, infantry_folder など）キャンバスサイズや位置間隔が mod・ツリー種類ごとに異なるため、既存フォルダを読んで値を合わせます。」**

参照フォルダが決まったら `interface/countrytechtreeview.gui` の該当 `containerWindowType` を Read して以下を記録する:
- `size { width height }` → キャンバスサイズ
- 年ラベルのピクセル間隔（y または x の差分）
- カテゴリヘッダーの間隔
- `techtree_[ref]_item` / `techtree_[ref]_small_item` の size・position 値

これらを新フォルダのテンプレートに転用する。**GUIテンプレートの数値はあくまで例であり、必ず参照フォルダの実測値を優先すること。**

---

## Step 1: レイアウト選択

**縦型（垂直）** — engnavalfolder スタイル
- 年が**上→下**（左側に年ラベル）
- カテゴリが**左→右**（上部にカテゴリヘッダー）
- 艦船固有ツリーに向く（多カテゴリ × 多年代）

**横型（水平）** — naval_folder / vanilla スタイル
- 年が**左→右**（上部に年ラベル）
- カテゴリが**上→下**
- 少カテゴリ × 時系列チェーンに向く

---

## Step 2: フォルダ名の命名規則

```
[TAG小文字][カテゴリ]folder
例: engnavalfolder, japnavalfolde, gerarmorfolder
```

---

## Step 3: common/technologies/[TAG]_[cat].txt の作成

### 縦型 位置変数（ENG_naval.txt準拠）

```
technologies = {
    # カテゴリ列（左→右）: y変数として使用
    @CAT_A = 0
    @CAT_B = 4
    @CAT_C = 8

    # 年代行（上→下）: x変数として使用
    # NOTE: HOI4の folder position では x=年値, y=カテゴリ値 の順で記述する
    @1930 = 0
    @1935 = 2
    @1940 = 4
    @1945 = 6
    @1950 = 8
    @1955 = 10
    @1960 = 12

    tech_name_here = {
        # ... enable_equipments, path, research_cost, start_year ...
        folder = {
            name = [foldername]
            position = {
                x = @1930    # ← 年変数をxに（縦型では年=x軸）
                y = @CAT_A   # ← カテゴリ変数をyに（縦型ではカテゴリ=y軸）
            }
        }
        categories = { naval_equipment }
    }
}
```

### 横型 位置変数（vanilla style）

```
technologies = {
    # 年代列（左→右）: x変数として使用
    @1936 = 0
    @1939 = 6
    @1942 = 12
    @1945 = 18

    # カテゴリ行（上→下）: y変数として使用
    @ROW_1 = 0
    @ROW_2 = 4
    @ROW_3 = 8

    tech_name_here = {
        folder = {
            name = [foldername]
            position = { x = @1936  y = @ROW_1 }
        }
    }
}
```

---

## Step 4: countrytechtreeview.gui への追記

**追記箇所は3か所ある。** 詳細テンプレートは `references/gui-templates.md` を参照。

### 4-1. フォルダ本体（techtreeviewコンテナ直下）
既存の最後のフォルダ (`containerWindowType { name = "electronics_folder" ... }`) の **直後** に追記。

縦型テンプレート → `references/gui-templates.md` の **[VERTICAL_FOLDER]** セクション
横型テンプレート → `references/gui-templates.md` の **[HORIZONTAL_FOLDER]** セクション

### 4-2. タブボタン（ファイル ~5596行付近）
`buttonType { name = "engnavalfolder_tab" ... }` のような既存タブの近くに追記:

```gui
buttonType = {
    name = "[foldername]_tab"
    position = { x = 610 y = 0 }    # 同系統タブと同じxを使う（上書き表示で国家別切替）
    quadTextureSprite = "GFX_naval_folder_tab"
    frame = 1
    clicksound = ui_research_tab_naval
}
```

### 4-3. アイテム定義（ファイル末尾 ~7000行以降）
`techtree_engnavalfolder_item` / `techtree_engnavalfolder_small_item` を参考にコピー:
- `name = "techtree_[foldername]_small_item"` → 72x72の小アイコン
- `name = "techtree_[foldername]_item"` → フル幅の詳細表示

テンプレート → `references/gui-templates.md` の **[ITEM_DEFS]** セクション

---

## Step 5: GFXスプライト定義

`interface/replace/_ssw_Tech_[TAG].gfx` (新規) または既存の `.gfx` ファイルに追記:

```
spriteTypes = {
    spriteType = {
        name = "GFX_[techname]_medium"
        textureFile = "gfx/interface/technologies/[cat]/[TAG]/[image].png"
    }
    # 各テックごとに1エントリ
}
```

**画像仕様:** PNG, 67×67px 推奨（medium アイコン）

---

## Step 6: ローカライズ

`localisation/japanese/ssw_[tag]_techtree_l_japanese.yml`:
```yaml
l_japanese:
 [techname]: "[テック表示名]"
 [techname]_desc: "[説明文]"
 [FOLDER_TITLE_KEY]: "[ツリータイトル]"
```

同内容を `localisation/english/ssw_[tag]_techtree_l_english.yml` にも作成（英訳または仮名でOK）。

---

## 位置座標の計算式

縦型（engnavalfolder準拠、1単位≒70px）:
- 年ラベルの pixel Y = `年x変数値 * 70`（左側年ラベルのy位置）
- カテゴリヘッダーの pixel X ≈ `120 + カテゴリy変数値 * 70`（上部ヘッダーのx位置）
- ツリーキャンバスサイズ: `width = (最大y値 + 4) * 70`, `height = (最大x値 + 4) * 70`

横型（vanilla準拠）:
- 年ラベルの pixel X ≈ `300 + year_step * ~350`
- カテゴリは上部から約100px間隔

---

## 注意事項

- `countrytechtreeview.gui` へ追記する際は `}` の対応を必ず確認する
- タブの `position.x` は同系統タブと**同じ値**にすることで国家別フォルダの切替表示が機能する
- `techtree_[foldername]_item` / `small_item` のname命名は **`techtree_` prefix + フォルダ名 + `_item`/`_small_item`** が必須
- 詳細GUIテンプレートは必ず `references/gui-templates.md` を読み込んでから作業する
