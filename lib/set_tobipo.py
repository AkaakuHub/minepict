from mcpi import minecraft
import mcpi.block as block

# 跳びポマシン設置1号
# 必ず絵の上で起動

# 設置高度: 4
# 推奨画像幅: 200程度


def main():
    mc = minecraft.Minecraft.create("localhost")
    player_pos = mc.player.getTilePos()

    array = [
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ],
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ],
        [
            [1, 23, 23, 23, 1],
            [23, 8, 0, 8, 23],
            [23, 0, 0, 0, 23],
            [23, 8, 0, 8, 23],
            [1, 23, 23, 23, 1],
        ],
        [
            [55, 55, 55, 55, 55],
            [55, 1, 1, 1, 55],
            [55, 1, 0, 1, 55],
            [55, 1, 1, 1, 55],
            [55, 55, 55, 55, 55],
        ],
        [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, 0, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
        ],
        [
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, None, None, None],
            [None, None, 70, None, None],
        ],
    ]
    for x in range(-2, 3):
        for z in range(-2, 3):
            for y in range(0, 6):
                if array[y][x + 2][z + 2] == None:
                    continue
                kind = 0
                if z == -2:
                    kind = 3
                elif z == 2:
                    kind = 2
                elif x == -2:
                    kind = 5
                elif x == 2:
                    kind = 4
                mc.setBlock(
                    player_pos.x + x,
                    player_pos.y + y - 5,
                    player_pos.z + z,
                    array[y][x + 2][z + 2],
                    kind,
                )
    mc.postToChat("Please set TNTs.")


main() if __name__ == "__main__" else None
