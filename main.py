import pyautogui
from PIL import Image, ImageDraw, ImageFilter
import tkinter as tk
import pygetwindow as gw
from pynput import mouse

def on_click(x, y, button, pressed):
    # TODO クリックしたウィンドウのスクリーンショットを撮る
    ss = pyautogui.screenshot()
    ss_pass = 'screenshot/ss.png'
    ss.save(ss_pass)
    print('スクリーンショットを保存しました。')

    if not pressed:
        # Stop listener
        return False

def ss_btn_click():
    # スクリーンショットを撮影するウィンドウのクリック待ち
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()


    # TODO ショートカットキーの設定
    # TODO 範囲指定をするか
    # TODO ウィンドウサイズの設定
    # TODO 透明度の設定
    # TODO ウィンドウを閉じるときファイルを削除するか


if __name__ == '__main__':
    # マウスカーソルが画面の隅に移動するとスクリプト強制終了（安全機構）
    pyautogui.FAILSAFE = True  # デフォルトで有効

    # ウィンドウ生成
    # TODO 最前面チェックあり
    root = tk.Tk()
    root.geometry("150x100")
    root.resizable(True, True)
    root.title('スクリーンショット透明化くん')

    # 撮影ボタン
    btn_ss = tk.Button(root, width=10, height=5, text='開　始', command=ss_btn_click)
    btn_ss.pack()

    root.mainloop()
