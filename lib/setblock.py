import numpy as np
from PIL import Image
from skimage import color, io
import json
import os
import glob
import math
from tqdm import tqdm

from mcpi import minecraft
import mcpi.block as block

# 除外対象
# チェスト類、シュルカーボックス, エンドポータル、mobの頭
# は遠くで描画されない

# 感圧板、カーペット、階段、雪、リピーター、ケーキ
# は低いから影ができる

# ice, frosted_ice
# は溶ける


def execute(
    mc, player_pos_new, filename, color_json, palette_rgb, width, height, art_altitude
):
    # 画像を読みこむ。
    img_rgb = io.imread(filename)

    img_rgb = np.array(Image.fromarray(img_rgb).resize((width, height)))

    # Lab 色空間に変換する。
    img_lab = color.rgb2lab(img_rgb)
    palette_lab = color.rgb2lab(palette_rgb)

    # 色差を計算する。
    diff = color.deltaE_ciede2000(
        np.expand_dims(img_lab, axis=2), palette_lab.reshape(1, 1, -1, 3)
    )

    # 一番近い色のインデックスを求める。
    indices = diff.argmin(axis=-1)

    # 一番近い色で出力画像を生成する。
    dst_rgb = palette_rgb[indices]

    # この画像をもとにしてマイクラのブロックを設置する
    # dst_rgbを配列に変換
    dst_rgb_array = np.array(dst_rgb)

    # 1ピクセルずつ設置する
    wid = dst_rgb_array.shape[0]
    hei = dst_rgb_array.shape[1]

    for i in range(0, wid):
        for j in range(0, hei):
            x = wid - i - 1
            z = hei - j - 1
            # まず要素から色を取り出し、hexに変換する
            hex = "{:02x}{:02x}{:02x}".format(
                int(dst_rgb_array[x][z][0]),
                int(dst_rgb_array[x][z][1]),
                int(dst_rgb_array[x][z][2]),
            )
            id = ""
            for key in color_json:
                if color_json[key] == hex:
                    id = key
                    break
            # id は例えば "21:1"
            if ":" in id:
                id = int(id.split(":")[0])
                kind = int(key.split(":")[1])
            else:
                id = int(id)
                kind = 0
            mc.setBlock(
                player_pos_new[0] + x, art_altitude, player_pos_new[2] + j, id, kind
            )
            if art_altitude > 4:
                mc.setBlock(
                    player_pos_new[0] + x, art_altitude - 1, player_pos_new[2] + j, 2
                )
    return


def set_from_video(width: int, art_altitude: int) -> int:
    mc = minecraft.Minecraft.create("localhost")

    with open("./database/color_v2.json", "r") as f:
        color_json = json.load(f)

    # RGBに変換する関数
    def hex_to_rgb(hex_string):
        return tuple(int(hex_string[i : i + 2], 16) for i in (0, 2, 4))

    # パレット一覧 (R, G, B)
    palette_rgb = np.array(
        [hex_to_rgb(color_json[key]) for key in color_json],
        dtype=np.uint8,
    )

    output_folder = "tempv/frames/"

    player_pos = mc.player.getPos()

    player_pos_x = math.floor(player_pos.x)
    player_pos_y = math.floor(player_pos.y)
    player_pos_z = math.floor(player_pos.z)
    player_pos_new = [player_pos_x, player_pos_y, player_pos_z]

    frame_files = sorted(glob.glob(output_folder + "*"))
    first_frame = frame_files[0]
    img_rgb = io.imread(first_frame)
    height = int(width * img_rgb.shape[0] / img_rgb.shape[1])

    h = math.tan(math.radians(55)) * max(width, height) / 2 + art_altitude
    mc.player.setPos(player_pos_new[0] + height // 2, h, player_pos_new[2] + width // 2)

    with tqdm(total=len(frame_files), desc="executing") as pbar:
        for i, filename in enumerate(frame_files):
            execute(
                mc,
                player_pos_new,
                filename,
                color_json,
                palette_rgb,
                width,
                height,
                art_altitude,
            )
            pbar.update(1)
    return 0


def set_from_picture(width: int, art_altitude: int) -> int:
    mc = minecraft.Minecraft.create("localhost")
    with open("./database/color_v2.json", "r") as f:
        color_json = json.load(f)

    # RGBに変換する関数
    def hex_to_rgb(hex_string):
        return tuple(int(hex_string[i : i + 2], 16) for i in (0, 2, 4))

    # パレット一覧 (R, G, B)
    palette_rgb = np.array(
        [hex_to_rgb(color_json[key]) for key in color_json],
        dtype=np.uint8,
    )

    files = glob.glob("tempp/*")
    filename = files[0]
    # もしjpgでなければjpgに変換する
    if ".jpg" not in filename:
        img = Image.open(filename)
        img = img.convert("RGB")
        # .がファイル名にあっても大丈夫なように取得
        name_wo_ext = os.path.splitext(filename)[0]
        img.save(f"{name_wo_ext}.jpg", "JPEG")
        filename = f"{name_wo_ext}.jpg"
    # 画像の縦横比を維持して、heightを計算する
    img_rgb = io.imread(filename)
    height = int(width * img_rgb.shape[0] / img_rgb.shape[1])

    player_pos = mc.player.getPos()

    player_pos_x = math.floor(player_pos.x)
    player_pos_y = math.floor(player_pos.y)
    player_pos_z = math.floor(player_pos.z)
    player_pos_new = [player_pos_x, player_pos_y, player_pos_z]

    h = math.tan(math.radians(55)) * max(width, height) / 2 + art_altitude
    mc.player.setPos(player_pos_new[0] + height // 2, h, player_pos_new[2] + width // 2)

    execute(
        mc,
        player_pos_new,
        filename,
        color_json,
        palette_rgb,
        width,
        height,
        art_altitude,
    )
    return 0
