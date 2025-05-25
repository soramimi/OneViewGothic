# HackVine Gothic

プログラミング用のラテン文字と日本語を組み合わせたカスタムモノスペースフォント

![sample image](https://soramimi.github.io/HackVineGothic/sample.png)

## 概要

HackVine Gothicは以下の2つのフォントを融合した複合フォントです：
- **Hack** - ソースコード専用に設計されたタイプフェース
- **VL Gothic** - 高品質な日本語フォント

これにより、適切なモノスペース特性を維持しながら、日本語文字（漢字、ひらがな、カタカナ）への優れたサポートを提供する、統一感のあるコーディング用フォントが実現されます。

## 特徴

- **モノスペース設計** - コードエディタやターミナルに最適
- **ASCII文字** - Hackフォントからの清潔で読みやすいラテン文字
- **日本語文字** - VL Gothicからの日本語テキストの完全サポート
- **一貫したメトリクス** - 統一されたアセント、ディセント、行間
- **プログラミング最適化** - ソースコードの可読性を重視した設計

## 前提条件

- **FontForge** - フォントのビルドに必要
- **Python** - ビルドスクリプトの実行用
- **Make** - Makefileの使用（オプション）

## フォントのビルド

### Makeを使用（推奨）

```bash
# ソースフォントのダウンロードとビルド
make

# システムへのフォントのインストール
make install

# フォント情報の表示
make scan

# 生成されたファイルのクリーンアップ
make clean
```

### 手動ビルド

```bash
# ソースフォントが利用可能であることを確認
python makefont.py
```

## インストール

### Windows
1. 上記の手順でフォントをビルドする
2. `HackVine-Gothic-Regular.ttf`を右クリック
3. 「インストール」または「すべてのユーザー用にインストール」を選択

### macOS
1. `HackVine-Gothic-Regular.ttf`をダブルクリック
2. Font Bookで「フォントをインストール」をクリック

### Linux
```bash
# ユーザーフォントディレクトリにコピー
cp HackVine-Gothic-Regular.ttf ~/.local/share/fonts/

# フォントキャッシュの更新
fc-cache -fv
```

## 使用方法

エディタやターミナルで「HackVine Gothic」をフォントファミリーとして設定してください。

### 主要なエディタでの設定

**VS Code**
```json
{
    "editor.fontFamily": "HackVine Gothic, monospace"
}
```

**Vim/Neovim**
```vim
set guifont=HackVine\ Gothic:h12
```

**Emacs**
```elisp
(set-face-attribute 'default nil :font "HackVine Gothic-12")
```

## ソースフォント

- **Hack**: [Source Foundry Hack](https://sourcefoundry.org/hack/)
- **VL Gothic**: [VL Gothic Font Family](http://vlgothic.dicey.org/)

## ライセンス

このプロジェクトは異なるライセンスのフォントを組み合わせています：
- HackフォントはMITライセンスでライセンスされています
- VL GothicはBSDスタイルのライセンスでライセンスされています

使用条件については、元のフォントライセンスを参照してください。

## 貢献

フォント生成プロセスやドキュメントの改善について、イシューの作成やプルリクエストの提出をお気軽にお願いします。

## トラブルシューティング

### FontForgeが見つからない
FontForgeがインストールされ、PATHで利用可能であることを確認してください。

### ビルドが失敗する
両方のソースフォントが`original/`ディレクトリに存在することを確認してください。`make download`を実行して自動的に取得することができます。

### アプリケーションでフォントが表示されない
システムのフォントキャッシュを更新してみてください：
- Windows: アプリケーションを再起動
- macOS: Font Bookを再起動
- Linux: `fc-cache -fv`を実行
