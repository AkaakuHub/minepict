from mcpi import minecraft
import mcpi.block as block

# 跳びポマシン設置2号
# 必ず絵の上で起動

# 設置高度: 5
# 推奨画像幅: 400程度

# レッドストーンパウダー 55
# リピーター 93
# 水 8
# ディスペンサー 23


def main():
    mc = minecraft.Minecraft.create("localhost")
    player_pos = mc.player.getTilePos()

    # 15x15, 高さ3
    array = [
        [
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ],
        [
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ],
        [
            [None, None, None],
            [None, None, None],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [None, None, None],
            [None, None, None],
        ],
        [
            [None, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [None, None, None],
            [931, 1, 931],
            [931, 1, 931],
            [931, 1, 931],
            [931, 1, 931],
            [931, 1, 931],
            [None, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [None, None, None],
        ],
        [
            [None, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [None, None, None],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [None, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [None, None, None],
        ],
        [
            [None, 1, 55],
            [None, 1, 932],
            [55, 1, 55],
            [932, 1, 932],
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
            [930, 1, 930],
            [55, 1, 55],
            [None, 1, 930],
            [None, 1, 55],
        ],
        [
            [1, 55, 0],
            [None, None, None],
            [55, 1, 55],
            [932, 1, 932],
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0],
            [0, 1, 0],
            [930, 1, 930],
            [55, 1, 55],
            [None, None, None],
            [1, 55, 0],
        ],
        [
            [55, 0, 0],
            [None, None, None],
            [55, 1, 55],
            [932, 1, 932],
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0],
            [0, 1, 0],
            [930, 1, 930],
            [55, 1, 55],
            [None, None, None],
            [55, 0, 0],
        ],
        [
            [933, None, None],
            [None, None, None],
            [55, 1, 55],
            [932, 1, 932],
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0],
            [0, 1, 0],
            [930, 1, 930],
            [55, 1, 55],
            [None, None, None],
            [933, None, None],
        ],
        [
            [55, None, None],
            [936, None, None],
            [55, 1, 55],
            [932, 1, 932],
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
            [930, 1, 930],
            [55, 1, 55],
            [934, None, None],
            [55, None, None],
        ],
        [
            [55, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [None, None, None],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [None, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [55, None, None],
        ],
        [
            [55, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [None, None, None],
            [933, 1, 933],
            [933, 1, 933],
            [933, 1, 933],
            [933, 1, 933],
            [933, 1, 933],
            [None, None, None],
            [None, None, None],
            [55, 1, 55],
            [None, None, None],
            [55, None, None],
        ],
        [
            [55, None, None],
            [None, None, None],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [55, 1, 55],
            [None, None, None],
            [55, None, None],
        ],
        [
            [55, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [None, None, None],
            [55, None, None],
        ],
        [
            [55, None, None],
            [55, None, None],
            [55, None, None],
            [55, 0, 0],
            [55, 0, 0],
            [1, 55, 0],
            [None, 1, 55],
            [None, None, 1],
            [None, 1, 55],
            [1, 55, 0],
            [55, 0, 0],
            [55, 0, 0],
            [55, None, None],
            [55, None, None],
            [55, None, None],
        ],
    ]
    for x in range(0, 15):
        for z in range(0, 15):
            for y in range(0, 3):
                if array[x][z][y] == None:
                    continue
                id = array[x][z][y]
                kind = 0
                if id == 930:
                    id = 93
                    kind = 0
                elif id == 931:
                    id = 93
                    kind = 1
                elif id == 932:
                    id = 93
                    kind = 2
                elif id == 933:
                    id = 93
                    kind = 3
                elif id == 934:
                    id = 93
                    kind = 4
                elif id == 936:
                    id = 93
                    kind = 6

                mc.setBlock(
                    player_pos.x + x - 7,
                    player_pos.y - 5 + y,
                    player_pos.z + z - 7,
                    id,
                    kind,
                )

    # パウダー
    mc.setBlock(player_pos.x + 7, player_pos.y + -2, player_pos.z, 55)
    # 感圧板 70
    mc.setBlock(player_pos.x + 7, player_pos.y + 0, player_pos.z, 70)
    # air 0
    mc.setBlock(player_pos.x + 0, player_pos.y - 1, player_pos.z, 0)
    mc.setBlock(player_pos.x + 0, player_pos.y - 2, player_pos.z, 0)
    # half slab 44
    mc.setBlock(player_pos.x + 7, player_pos.y - 2, player_pos.z + 1, 44, 8)
    mc.setBlock(player_pos.x + 7, player_pos.y - 2, player_pos.z - 1, 44, 8)

    mc.postToChat(
        "Please use CTRL+wheel click to copy dispensers. Then, set redstone powder on them."
    )


main() if __name__ == "__main__" else None
