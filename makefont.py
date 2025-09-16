import fontforge

basename = 'OneVine'

asciifont = fontforge.open('original/IntelOneMono-Regular.ttf')
kanjifont = fontforge.open('original/VL-Gothic-Regular.ttf')

asciifont.familyname = basename + " Gothic"
asciifont.weight = "Regular"
asciifont.fontname = basename + "-Gothic-Regular"
asciifont.fullname = basename + " Gothic Font"

savename = asciifont.fontname + '.ttf'

print("kanjifont.os2_typoascent: ", kanjifont.os2_typoascent)
print("kanjifont.hhea_ascent: ", kanjifont.hhea_ascent)
print("kanjifont.ascent: ", kanjifont.ascent)
print("kanjifont.os2_typodescent: ", kanjifont.os2_typodescent)
print("kanjifont.hhea_descent: ", kanjifont.hhea_descent)
print("kanjifont.descent: ", kanjifont.descent)
print()
print("asciifont.os2_typoascent: ", asciifont.os2_typoascent)
print("asciifont.hhea_ascent: ", asciifont.hhea_ascent)
print("asciifont.ascent: ", asciifont.ascent)
print("asciifont.os2_typodescent: ", asciifont.os2_typodescent)
print("asciifont.hhea_descent: ", asciifont.hhea_descent)
print("asciifont.descent: ", asciifont.descent)
print()

# 不要なファミリー名を削除または修正
new_sfnt_names = []
for name in asciifont.sfnt_names:
    # 'name' は (言語, 名前の種類, 値) のタプル
    # ファミリー名やスタイル名のタプルのみを変更または保持する
    if name[1] == 'Family' or name[1] == 'SubFamily':
        new_sfnt_names.append((name[0], name[1], asciifont.familyname))
    else:
        new_sfnt_names.append(name)

# 更新されたsfnt_namesをフォントに設定
asciifont.sfnt_names = new_sfnt_names

halfwidth = asciifont[ord('A')].width
fullwidth = kanjifont[ord('Ａ')].width

 # 全角用の補正値
dx = 190
dy = -60
scale = 1.7 * halfwidth / fullwidth

# kanjifont内の各グリフに対してループ処理
for glyph in kanjifont.glyphs():
    # 全角のみ処理する（kanjifontの中にも半角記号などが存在するがそれは対象外）
    if glyph.width > fullwidth * 0.75 or (glyph.unicode >= 0xff65 and glyph.unicode < 0xffa0):
        if glyph.width < fullwidth * 0.75:
            glyph.transform([scale, 0, 0, scale, dx / 2, dy]) # サイズと位置調整
            glyph.width = halfwidth # 半角サイズ
        else:
            glyph.transform([scale, 0, 0, scale, dx, dy]) # サイズと位置調整
            glyph.width = halfwidth * 2 # 全角サイズ
        try: # 一部のコードポイントが例外になるものがある
            if glyph.unicode in asciifont: # 既存なら消去
                asciifont.selection.select(glyph.unicode)
                asciifont.clear()  # 既存のグリフをクリア
            else: # 追加
                asciifont.createMappedChar(glyph.unicode)
                asciifont.selection.select(glyph.unicode)
            # kanjifontからasciifontへグリフをコピー
            kanjifont.selection.select(glyph.encoding) # グリフを選択
            kanjifont.copy() # 選択したグリフをコピー
            asciifont.paste() # asciifontに新しいグリフとして貼り付け
        except ValueError:
            pass # 無視

# 全グリフのサイズ調整
scale = 1.0 # 大きいほど拡大
if scale != 1.0:
    for glyph in asciifont.glyphs():
        glyph.transform([scale, 0, 0, scale, 0, 0])

# フォント全体の高さ調整
scale = 1.2
asciifont.ascent = round(asciifont.ascent * scale)
asciifont.descent = round(asciifont.descent * scale)

asciifont.os2_typoascent = asciifont.ascent
asciifont.os2_typodescent = -asciifont.descent

scale = 1.0
asciifont.hhea_ascent = round(asciifont.hhea_ascent * scale)
asciifont.hhea_descent = round(asciifont.hhea_descent * scale)


print("newfont.os2_typoascent: ", asciifont.os2_typoascent)
print("newfont.hhea_ascent: ", asciifont.hhea_ascent)
print("newfont.ascent: ", asciifont.ascent)
print("newfont.os2_typodescent: ", asciifont.os2_typodescent)
print("newfont.hhea_descent: ", asciifont.hhea_descent)
print("newfont.descent: ", asciifont.descent)

# 変更を保存
asciifont.generate(savename)

# フォントを閉じる
asciifont.close()
kanjifont.close()
