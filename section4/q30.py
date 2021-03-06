# coding: utf-8
import MeCab

# neko.txtを形態素解析してneko.txt.mecabに保存
def parse_txt():

    with open('neko.txt') as data_file, \
            open('neko.txt.mecab', mode='w') as out_file:

        # *1
        mecab = MeCab.Tagger()
        out_file.write(mecab.parse(data_file.read()))

# 形態素解析結果のジェネレータ *2
def fix_mecab():

    with open('neko.txt.mecab') as parsed_file:

        morphemes = [] # morphemeは日本語で形態素という意味。モーフィム。各形態素を辞書化したものでできた1文。
        for line in parsed_file:

            # 表層形とそれ以外をタブで分ける *3
            cols = line.split('\t')
            # 区切りがなければ終了
            if(len(cols) < 2):
                return
            # 表層形以外の部分をカンマで分ける *4
            rest_cols = cols[1].split(',')

            # 辞書を作成し、リストに追加 *5
            morpheme = {
                'surface': cols[0],
                'base': rest_cols[6],
                'pos': rest_cols[0],
                'pos1': rest_cols[1]
            }
            morphemes.append(morpheme)

            # 品詞細分類1(pos1)、すなわちrest_cols[1]が'句点'なら文の終わりと判定 *6
            if rest_cols[1] == '句点':
                yield morphemes # 関数内でreturnの代わりにyieldを使うと、次の呼び出し時にそこから再開される
                morphemes = []

# 形態素解析
parse_txt()

# linesは1文の各形態素を辞書化したものが集まったリスト(となる。ジェネレータなのでちょっと違う)
lines = fix_mecab()

for line in lines:
    print(line)

# # 先頭3つの要素表示
# for i, line in enumerate(lines):
#     if i == 3:
#         break
#     print(line)