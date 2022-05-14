# ダブルアップゲームを想定したプログラム。
# 各回で、より確率が高い選択肢を教えてくれる。


# クラス宣言 ---------------------------------------------------------------------

# カードの枚数管理を行うクラス
class Cards:
    def __init__(self):
        self.num_cards = [4] * 13

    def remove(self, card_rank, num_remove):
        if num_remove < 0:
            return -1

        self.num_cards[card_rank - 1] -= num_remove
        if self.num_cards[card_rank - 1] < 0:
            self.num_cards[card_rank - 1] = 0
        return 0
    
    def getNumOf(self,card_rank):
        return self.num_cards[card_rank - 1]

    def countTotal(self):
        return sum(self.num_cards)


# 関数宣言 -----------------------------------------------------------------------

def readCardRank():
    rank = 0
    usr_input = None
    while( rank < 1 or 13 < rank):
        if usr_input != None:
            print("再入力してください")

        usr_input = input("トランプの数字を入力:")
        if usr_input.isdigit():
            rank = int(usr_input)
    
    return rank


def countCardsHigherThan(base_rank, cards):
    if base_rank == 1: # highest rank
        return 0

    num = cards.getNumOf(card_rank = 1)
    for card_rank in range(base_rank + 1, 14):  # rangeの仕様 range(i, j)=[i, i+1, ..., j-1], if(j<=i)=[null]
        num += cards.getNumOf(card_rank)
    return num

def countCardsLowerThan(base_rank, cards):
    if base_rank == 1: # highest rank
        return cards.countTotal() - cards.getNumOf(card_rank = 1)

    num = 0
    for card_rank in range(2, base_rank):       # rangeの仕様 range(i, j)=[i, i+1, ..., j-1], if(j<=i)=[null]
        num += cards.getNumOf(card_rank)
    return num


def select(selection):
    # 現在は表示するのみだが、自動的に選択するようにしたい。
    print(selection + "\n")


def loseBet(selection):
    # 未実装 ( 結果を手入力するくらいならCtrl + c で良い )
    # 画像認識を実装予定
    return 0


# メイン -------------------------------------------------------------------------

def main():
    stack = Cards() # stack of cards = 山札

    for times in range(10):
        base_rank = readCardRank()
        stack.remove(base_rank, 1)

        n_higher_cards = countCardsHigherThan(base_rank, stack)
        n_lower_cards  = countCardsLowerThan(base_rank, stack)
        print("higher: %d, lower: %d" %(n_higher_cards, n_lower_cards))

        if(n_higher_cards > n_lower_cards):
            selection = "high"
        else:
            selection = "low"
        select(selection)
        
        if(loseBet(selection)):
            break

main()
