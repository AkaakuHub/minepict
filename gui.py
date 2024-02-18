import flet as ft

from lib import movie2pict as m2p
from lib import setblock as cvt

import os
import shutil
import time

this_version: str = "1.1"

filepath_v: str = ""
filepath_p: str = ""

isAlreadyFrameExtracted: bool = False

width_v: int = 100
width_p: int = 200

art_altitude: int = 4


def main(page: ft.Page):
    def message_fadeout(obj: ft.Text, message: str):
        if obj.value == message:
            return
        obj.value = message
        obj.color = ft.colors.RED
        obj.update()
        time.sleep(2)
        obj.value = ""
        obj.color = ft.colors.WHITE
        obj.update()

    def pick_files_result_v(e: ft.FilePickerResultEvent):
        global filepath_v, isAlreadyFrameExtracted
        if e.files:
            ft_selected_files_v.value = ", ".join(map(lambda f: f.path, e.files))
            filepath_v = ft_selected_files_v.value
            # はみ出ないように表示だけ短く
            ft_selected_files_v.value = (
                filepath_v[:50] + "..." if len(filepath_v) > 50 else filepath_v
            )
            shutil.rmtree("tempv", ignore_errors=True)
            os.makedirs("tempv", exist_ok=True)
            os.makedirs("tempv/frames", exist_ok=True)
            shutil.copy(filepath_v, "tempv")
            isAlreadyFrameExtracted = False
            ft_status_of_extract_frames.value = ""
            ft_status_of_set_from_video.value = ""
            ft_selected_files_v.update()
            ft_status_of_extract_frames.update()
            ft_status_of_set_from_video.update()
        else:
            message_fadeout(ft_selected_files_v, "ファイルの選択がキャンセルされました")

    def pick_files_result_p(e: ft.FilePickerResultEvent):
        global filepath_p, isAlreadyFrameExtracted
        if e.files:
            ft_selected_files_p.value = ", ".join(map(lambda f: f.path, e.files))
            filepath_p = ft_selected_files_p.value
            # はみ出ないように表示だけ短く
            ft_selected_files_p.value = (
                filepath_p[:50] + "..." if len(filepath_p) > 50 else filepath_p
            )
            shutil.rmtree("tempp", ignore_errors=True)
            os.makedirs("tempp", exist_ok=True)
            shutil.copy(filepath_p, "tempp")
            ft_status_of_set_from_picture.value = ""
            ft_selected_files_p.update()
            ft_status_of_set_from_picture.update()
        else:
            message_fadeout(ft_selected_files_p, "ファイルの選択がキャンセルされました")

    pick_files_dialog_v = ft.FilePicker(on_result=pick_files_result_v)
    pick_files_dialog_p = ft.FilePicker(on_result=pick_files_result_p)
    ft_selected_files_v = ft.Text()
    ft_selected_files_p = ft.Text()

    page.overlay.append(pick_files_dialog_v)
    page.overlay.append(pick_files_dialog_p)

    def do_extract_frames():
        global filepath_v, isAlreadyFrameExtracted
        if filepath_v == "":
            message_fadeout(ft_status_of_extract_frames, "ファイルが選択されていません")
            return
        if isAlreadyFrameExtracted:
            message_fadeout(
                ft_status_of_extract_frames, "すでにフレームは抽出されています"
            )
            return

        video_name = os.path.basename(filepath_v)
        status: int = m2p.extract_frames(video_name)
        # 0なら成功なので、UIに成功したことを表示する
        if status == 0:
            ft_status_of_extract_frames.value = "フレームの抽出に成功しました"
            isAlreadyFrameExtracted = True
        else:
            message_fadeout(ft_status_of_extract_frames, "フレームの抽出に失敗しました")
            isAlreadyFrameExtracted = False
        ft_status_of_extract_frames.update()

    ft_status_of_extract_frames = ft.Text()

    def do_set_from_video():
        global width_v, filepath_v, isAlreadyFrameExtracted
        # print(width_v)
        if not isAlreadyFrameExtracted:
            message_fadeout(ft_status_of_set_from_video, "フレームが抽出されていません")
            return
        ft_status_of_set_from_video.value = "設置中..."
        ft_status_of_set_from_video.update()
        status: int = cvt.set_from_video(width_v, art_altitude)
        if status == 0:
            ft_status_of_set_from_video.value = "設置に成功しました"
            # shutil.rmtree("tempv")
            ft_status_of_set_from_video.update()
        else:
            message_fadeout(ft_status_of_set_from_video, "設置に失敗しました")

    def do_set_from_picture():
        global width_p, filepath_p
        # print(width_p)
        if filepath_p == "":
            message_fadeout(
                ft_status_of_set_from_picture, "ファイルが選択されていません"
            )
            return
        ft_status_of_set_from_picture.value = "設置中..."
        ft_status_of_set_from_picture.update()
        status: int = cvt.set_from_picture(width_p, art_altitude)
        if status == 0:
            ft_status_of_set_from_picture.value = "設置に成功しました"
            # shutil.rmtree("tempp")
            ft_status_of_set_from_picture.update()
        else:
            message_fadeout(ft_status_of_set_from_picture, "設置に失敗しました")

    def change_width_v(e):
        global width_v
        try:
            width_v = int(e.control.value)
        except ValueError:
            return

    def change_width_p(e):
        global width_p
        try:
            width_p = int(e.control.value)
        except ValueError:
            return

    def change_art_altitude(e):
        global art_altitude
        try:
            art_altitude = int(e.control.value)
        except ValueError:
            return

    # これのまとめ方がわからない

    ft_status_of_set_from_video = ft.Text()
    ft_status_of_set_from_picture = ft.Text()

    width_input_v = ft.TextField(
        label="数値", on_change=change_width_v, value=str(width_v)
    )
    width_input_p = ft.TextField(
        label="数値", on_change=change_width_p, value=str(width_p)
    )
    page.title = "Minecraft 画像/動画配置ツール"

    wrapper = ft.Column(
        [
            ft.Text(f"Minecraft 画像/動画配置ツール ver. {this_version}", size=35),
            ft.Text(
                "先にMinecraftを起動してください。\nまた、動画を録画する際はReplay Mod等の使用を推奨します。",
                size=16,
            ),
            ft.Container(
                ft.Row(
                    [
                        ft.Text("設置高度:"),
                        ft.TextField(
                            label="数値",
                            on_change=change_art_altitude,
                            value=str(art_altitude),
                        ),
                    ]
                ),
                padding=12,
            ),
            ft.Row(
                [
                    ft.Stack(
                        [
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text("画像を設置する", size=25),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.ElevatedButton(
                                                                    "1.ファイルを選択",
                                                                    icon=ft.icons.UPLOAD_FILE,
                                                                    on_click=lambda _: pick_files_dialog_p.pick_files(
                                                                        allow_multiple=False,
                                                                        dialog_title="ファイルを選択",
                                                                        allowed_extensions=[
                                                                            ".png",
                                                                            ".jpg",
                                                                            ".jpeg",
                                                                            "PNG",
                                                                            "JPG",
                                                                            "JPEG",
                                                                        ],
                                                                    ),
                                                                ),
                                                                ft_selected_files_p,
                                                            ],
                                                            alignment=ft.MainAxisAlignment.START,
                                                        ),
                                                    ]
                                                ),
                                                # blend_mode=ft.BlendMode.SRC,
                                                # margin=15,
                                                padding=5,
                                                # border_radius=15,
                                            ),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.Text(
                                                                    "ブロック数(横幅):"
                                                                ),
                                                                width_input_p,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                # blend_mode=ft.BlendMode.SRC,
                                                # margin=15,
                                                padding=12,
                                                # border_radius=15,
                                            ),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.ElevatedButton(
                                                                    "2.配置を開始",
                                                                    icon=ft.icons.PLAY_CIRCLE,
                                                                    on_click=lambda _: do_set_from_picture(),
                                                                ),
                                                                ft_status_of_set_from_picture,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                # blend_mode=ft.BlendMode.SRC,
                                                # margin=15,
                                                padding=5,
                                                # border_radius=15,
                                            ),
                                        ],
                                        width=page.width // 2,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                        ],
                        width=page.width // 2,
                        height=page.height - 375,
                        expand=False,
                    ),
                    ft.Stack(
                        [
                            ft.Row(
                                [
                                    ft.Column(
                                        [
                                            ft.Text("動画を設置する", size=25),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.ElevatedButton(
                                                                    "1.ファイルを選択",
                                                                    icon=ft.icons.UPLOAD_FILE,
                                                                    on_click=lambda _: pick_files_dialog_v.pick_files(
                                                                        allow_multiple=False,
                                                                        dialog_title="ファイルを選択",
                                                                        allowed_extensions=[
                                                                            ".mp4",
                                                                            ".mov",
                                                                            "mkv",
                                                                            "webm",
                                                                            "MP4",
                                                                            "MOV",
                                                                            "MKV",
                                                                            "WEBM",
                                                                        ],
                                                                    ),
                                                                ),
                                                                ft_selected_files_v,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                # blend_mode=ft.BlendMode.SRC,
                                                # margin=15,
                                                padding=5,
                                                # border_radius=15,
                                            ),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.ElevatedButton(
                                                                    "2.フレームを抽出",
                                                                    icon=ft.icons.PHOTO_SIZE_SELECT_ACTUAL_OUTLINED,
                                                                    on_click=lambda _: do_extract_frames(),
                                                                ),
                                                                ft_status_of_extract_frames,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                # blend_mode=ft.BlendMode.SRC,
                                                # margin=15,
                                                padding=5,
                                                # border_radius=15,
                                            ),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.Text(
                                                                    "ブロック数(横幅):"
                                                                ),
                                                                width_input_v,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                # blend_mode=ft.BlendMode.SRC,
                                                # margin=15,
                                                padding=12,
                                                # border_radius=15,
                                            ),
                                            ft.Container(
                                                ft.Column(
                                                    [
                                                        ft.Row(
                                                            [
                                                                ft.ElevatedButton(
                                                                    "3.配置を開始",
                                                                    icon=ft.icons.PLAY_CIRCLE,
                                                                    on_click=lambda _: do_set_from_video(),
                                                                ),
                                                                ft_status_of_set_from_video,
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                # blend_mode=ft.BlendMode.SRC,
                                                # margin=15,
                                                padding=5,
                                                # border_radius=15,
                                            ),
                                        ],
                                        width=page.width // 2,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.START,
                            ),
                        ],
                        width=page.width // 2,
                        height=page.height - 375,
                        expand=False,
                    ),
                ]
            ),
            ft.Text(
                "必要環境\nMinecraft: ver.1.12.2\nRaspberryJamMod\n\n推奨MOD\nFlight Speed Modifier",
                size=16,
            ),
        ]
    )
    page.window_width = 1280
    page.window_height = 720
    page.add(wrapper)


ft.app(target=main)
